# FIle with stuff that help the program or couldn't fit inside the rest of the files
from bs4 import BeautifulSoup
from dateutil import parser, tz
import logging
from colorlog import ColoredFormatter

class Helper:
    def __init__(self):
        pass

    def parse_basic_data(self, html_content):
        """_summary_

        Args:
            html_content (_type_): HTML document string

        Returns:
            Dict: Returns a dictionary with all the basic data for the hash
        """

        self.basic_data = {}

        soup = BeautifulSoup(html_content, "html.parser")


        file_hash = soup.find("div", {"class": "file-id"})

        positives_text = soup.find("div", {"class": "hstack gap-2 fw-bold text-danger"})

        file_type = soup.find("a", {"class": "badge rounded-pill bg-info-alt text-info-alt"})

        file_size = soup.find("a", {"class": "text-nowrap"})

        last_analysis_date = soup.find("vt-ui-time-ago").get("data-tooltip-text")

        common_file_name = soup.find("div", {"class": "file-name text-truncate"}).find("a")

        self.basic_data["file_hash"] = file_hash.text.strip()
        self.basic_data["analysis"] = positives_text.text.replace("\n", "").strip()
        try:
            self.basic_data["file_type"] = file_type.text.strip()
        except:
            self.basic_data["file_type"] = "Unknown"

        self.basic_data["file_name"] = common_file_name.text.strip()
        self.basic_data["file_size"] = file_size.text.strip()
        self.basic_data["last_analysis"] = self.convert_utc_to_local(last_analysis_date.strip())

        return self.basic_data
    
    def parse_url_data(self, html_content):
        """_summary_

        Args:
            html_content (_type_): HTML document string

        Returns:
            Dict: Returns a dictionary with all the basic data for the domain/URL
        """

        self.url_data = {}

        soup = BeautifulSoup(html_content, "html.parser")

        positives = soup.find("div", {"class": "hstack gap-2 fw-bold text-danger"}).text

        url = soup.find("div", {"class": "vstack gap-2 align-self-center text-truncate me-auto"}).find("div", {"class": "text-truncate"}).text

        details_div = soup.find("div", {"class": "hstack gap-4"}).find_all("div", recursive=False)

        registrar_exists = details_div[2].find("div", {"class": "text-body-tertiary"}).text

        try:
            creation_date = details_div[4].find("vt-ui-time-ago").get("data-tooltip-text")
        except AttributeError:
            creation_date = "N/A"

        last_analysis = soup.find("div", {"class": "hstack gap-4"}).find_all("vt-ui-time-ago")[-1].get("data-tooltip-text")


        if registrar_exists == "Registrar":
            self.url_data['registrar'] = details_div[2].find("a").text.replace("\n", "").strip()
        else:
            self.url_data['registrar'] = "Unknown"


        self.url_data['url'] = self.format_text(url)
        self.url_data['analysis'] = self.format_text(positives)
        self.url_data['creation_date'] = self.format_text(creation_date)
        self.url_data['last_analysis'] = self.convert_utc_to_local(last_analysis.strip())

        print(self.url_data)

        return self.url_data

    
    def convert_utc_to_local(self, date_string):
        """_summary_

        Args:
            date_string (_type_): string date

        Returns:
            str: A string representation of the date_string to local time
        """
        p = parser.parse(date_string)

        local_time = p.astimezone(tz.tzlocal())

        return local_time.strftime("%d %B %Y at %I:%M %p")


    def format_text(self, text: str):
        return text.replace("\n", "").strip()
    
    def get_community_score(self, text_content):
        """_summary_

        Args:
            driver (_type_): Selenium websriver

        Returns:
            int: Community score of the hash
        """ 
        try:
            community_score = text_content.strip().split("Community Score")[1].strip()
            return community_score
        except AttributeError:
            return 0
        

    def get_basic_data(self, driver):
        """_summary_

        Args:
            driver (_type_): Selenium websriver

        Returns:
            dict: Dict with the basic file data
        """

        content = driver.execute_script(
            """return document.querySelector("#view-container > file-view").shadowRoot.querySelector("#report > vt-ui-file-card").shadowRoot.innerHTML""")
        
        return self.parse_basic_data(content)
    
    def get_url_data(self, driver):
        """_summary_

        Args:
            driver (_type_): Selenium websriver

        Returns:
            dict: Dict with the basic URL analysis data
        """

        content = driver.execute_script(
            """return document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#report > vt-ui-domain-card").shadowRoot.innerHTML""")

        return self.parse_url_data(content)

    def get_logger(self): 
        """
        Setting up the logger with colorlog formatting.
        """

        # Defining the log format
        log_format = "%(log_color)s%(levelname)-8s: %(message)s%(reset)s"
        formatter = ColoredFormatter(log_format)

        # Configuring stream handler with color formatting
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.NOTSET)
        stream_handler.setFormatter(formatter)

        # Creating logger instance
        logger = logging.getLogger("VirusTotalTool")
        logger.setLevel(logging.NOTSET)
        logger.addHandler(stream_handler)



        return logger

    def is_file_hash(input_value):
        return len(input_value) in (32, 64) and all(c in "0123456789abcdefABCDEF" for c in input_value)

    def is_domain(input_value):
        return "." in input_value and not input_value.replace(".", "").isdigit()

    def is_ip(input_value):
        return all(part.isdigit() and 0 <= int(part) <= 255 for part in input_value.split("."))