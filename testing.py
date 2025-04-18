# Inbuilt
import time
import argparse
import re

# External
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich_gradient import Gradient
from rich.console import Console
from rich.prompt import Prompt
from rich_argparse import RichHelpFormatter
from fake_useragent import UserAgent

# Internal
from filemanager.file_manager import FileManager
from vpn.vpn_manager import VPNManager
from helper import Helper

# Selenium
import selenium
from selenium import webdriver
import selenium.common
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions

ANALYSIS_TYPES = ["file", "url", "ip"]
OUTPUT_FORMAT = ["csv", "pdf", "db", "docx"]

arg_parser = argparse.ArgumentParser(
    description="Advanced tool to automatically analyze and generate malware reports using VirusTotal without an API key.",
    formatter_class=RichHelpFormatter,
)

arg_parser.add_argument(
    "--mode",
    "-m",
    help="Select type of analysis. (default: file)",
    default="file",
    choices=ANALYSIS_TYPES,
)
arg_parser.add_argument(
    "--output",
    "-of",
    help="Select output file format. (default: csv)",
    default="csv",
    choices=OUTPUT_FORMAT,
)
arg_parser.add_argument(
    "--input",
    "-if",
    help="Select .txt file with the hashes, urls, or ips.",
    required=True,
)
arg_parser.add_argument(
    "--delay", "-dl", help="Set custom delay between requests.", default=3, type=int
)
arg_parser.add_argument(
    "--skip-vpn",
    "-sv",
    help="Skip using VPN in case of captcha. Note: This makes the tool only work for ~40 requests.",
    default=False,
)
arg_parser.add_argument(
    "--headless",
    "-hl",
    help="Pass this if you want to run chrome driver in headless mode. (Not Recommended)",
    action="store_true",
)

args = arg_parser.parse_args()

IS_CSV = args.output == "csv"
IS_PDF = args.output == "pdf"
IS_DB = args.output == "db"
IS_DOCX = args.output == "docx"

IS_FILE_SCAN = args.mode == "file"
IS_URL_SCAN = args.mode == "url"
IS_IP_SCAN = args.mode == "ip"

console = Console()
helper = Helper()

logger = helper.get_logger()

console.print(
    Gradient(
        """
██╗   ██╗██╗██████╗    ██████╗ ██╗   ██╗
██║   ██║██║██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║   ██║██║██████╔╝   ██████╔╝ ╚████╔╝ 
╚██╗ ██╔╝██║██╔══██╗   ██╔═══╝   ╚██╔╝  
 ╚████╔╝ ██║██║  ██║██╗██║        ██║   
  ╚═══╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝  

[-] Created by Abhay
""",
        colors=["#CB9DF0", "#F0C1E1", "#FDDBBB"],
    )
)


analysis_progress_bar = Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
)

# Class Instances and helpers
file_manager = FileManager(logger=logger, file_format=args.output, analysis_mode=args.mode)
file_manager.console = analysis_progress_bar.console
vpn_manager = VPNManager(logger=logger)
user_agent = UserAgent()
user_string = user_agent.chrome


# File stuff
with open(args.input, "r") as hash_file:
    total_target = hash_file.readlines()

if IS_CSV:
    result_file = file_manager.create_file()


def initialize_driver():
    """
    Initialize Chrome driver and return it.
    """
    options = webdriver.ChromeOptions()

    options.add_argument(f"--user-agent={user_string}")

    if args.headless:
        options.add_argument(f"--headless")

    options.add_argument(f"--log-level=3")

    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    return driver


def switch_vpn_and_reinitialize_driver(current_driver):
    """
    Switch VPN servers and reinitialize the Chrome driver to continue analysis.
    """
    current_driver.quit()
    vpn_manager.connect_random_server()
    time.sleep(5)
    return initialize_driver()


driver = initialize_driver()


def scan_file_hash(input_data):
    target = input_data.strip()
    driver.get(f"https://www.virustotal.com/gui/file/{target}")

    time.sleep(args.delay)

    element = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="view-container"]/file-view')
        )
    )

    community_score = driver.execute_script(
        'return document.querySelector("#view-container > file-view").shadowRoot.querySelector("#report").shadowRoot.querySelector("div > div.row.mb-4.d-none.d-lg-flex > div.col-auto > vt-ioc-score-widget").shadowRoot.querySelector("div > span > span.badge.rounded-pill.fs-6.fw-normal.hstack.align-self-auto.pe-2.bg-opacity-10.bg-danger > span.ms-2.me-1.text-danger")'
    )

    basic_data = helper.get_basic_data(driver=driver)
    try:
        basic_data["community_score"] = community_score.text
    except AttributeError:
        basic_data["community_score"] = 0

    return basic_data


def scan_domain(input_data):
    target = input_data.strip()
    target = helper.extract_domain(input_data)
    driver.get(f"https://www.virustotal.com/gui/domain/{target}")

    time.sleep(args.delay)

    element = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="view-container"]/domain-view')
        )
    )

    community_score = driver.execute_script(
        """document.querySelector("#view-container > domain-view").shadowRoot.querySelector("div > div > div.col-auto.d-none.d-md-block > vt-ioc-score-widget").shadowRoot.querySelector("div > span").textContent"""
    )

    print(community_score)
    final_score = helper.get_community_score(community_score)

    basic_data = helper.get_url_data(driver=driver)

    try:
        basic_data["community_score"] = "0" if final_score == "•" else str(final_score)
    except AttributeError:
        basic_data["community_score"] = "0"

    # print("BASIC DATA", basic_data)
    return basic_data


def scan_ip(input_data):
    target = input_data.strip()
    driver.get(f"https://www.virustotal.com/gui/ip-address/{target}")

    time.sleep(args.delay)

    # community_score = driver.execute_script(
    #     """return document.querySelector("#view-container > ip-address-view").shadowRoot.querySelector("div > div > div.col-auto.d-none.d-md-block > vt-ioc-score-widget").shadowRoot.querySelector("div > span").textContent"""
    # )

    # final_score = helper.get_community_score(community_score)

    basic_data = helper.get_ip_data(driver=driver)

    # try:
    #     basic_data["community_score"] = "0" if final_score == "•" else str(final_score)
    # except AttributeError:
    #     basic_data["community_score"] = "0"
    
    # print(basic_data)

    return basic_data

with analysis_progress_bar as progress:
    """Main loop to perform the analysis"""

    try:
        analysis_task = progress.add_task("[green]Analyzing", total=len(total_target))

        for index, target in enumerate(total_target):
            target = target.strip()

            if "captcha" in driver.current_url:
                print(driver.current_url)
                # el = driver.find_element(By.XPATH, '//*[@id="captchaContainer"]')
                console.print(
                    f"Encountered a captcha, trying to reinitialize VPN and drivers\n"
                )
                console.print(
                    "[yellow]Switching VPN and reinitializing WebDriver...[/yellow]\n"
                )
                total_target.append(target)
                driver = switch_vpn_and_reinitialize_driver(driver)
                continue

            else:
                
                if IS_FILE_SCAN:
                    analyzed_data = scan_file_hash(target)
                elif IS_URL_SCAN:
                    analyzed_data = scan_domain(target)
                elif IS_IP_SCAN:
                    analyzed_data = scan_ip(target)


                if IS_CSV:
                    file_manager.save_csv(data=analyzed_data, file=result_file)

                elif IS_PDF:
                    file_manager.add_pdf_report(data=analyzed_data)

                elif IS_DOCX:
                    file_manager.add_docx_report(data=analyzed_data)

                elif IS_DB:
                    file_manager.add_db_report(data=analyzed_data)

            progress.update(analysis_task, advance=1)

    finally:
        if IS_CSV:
            file_manager.close_file()

        elif IS_PDF:
            file_manager.save_pdf()

        elif IS_DOCX:
            file_manager.save_docx()

        elif IS_DB:
            file_manager.save_db()

        driver.quit()
        console.print("[bold green]Finished analysis.")
