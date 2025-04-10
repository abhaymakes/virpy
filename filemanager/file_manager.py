import os
import sys
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.prompt import Confirm, Prompt

# File types for the report
from filemanager.pdf_manager import PDFManager
from filemanager.docx_manager import DOCXManager
from filemanager.db_manager import DBManager

class FileManager:

    def __init__(self, logger, file_format: str, analysis_mode = "file"):
        self.logger = logger
        self.file_type = ""
        self.file_name = "report"
        self.file_object = None
        self.mode = analysis_mode
        self.console = None
        self.when = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.IS_FILE = self.mode == "file"
        self.IS_URL = self.mode == "url"
        self.IS_IP = self.mode == "ip"

        self.pdf_path = Path(f"{self.when}.pdf")
        self.docx_path = Path(f"{self.when}.docx")
        self.db_path = Path(f"{self.when}.db")

        self.pdf_manager = None
        self.docx_manager = None
        self.db_manager = None



        if file_format == "pdf":
            if not (self.handle_existing_file(self.pdf_path, "PDF")):
                self.pdf_manager = PDFManager(analysis_mode=self.mode)
                self.pdf_manager.add_page()
                self.logger.info("PDF Manager initialized.")

        # Handle DOCX file
        if file_format == "docx":
            if not (self.handle_existing_file(self.docx_path, "DOCX")):
                self.docx_manager = DOCXManager(analysis_mode=self.mode)
                self.logger.info("DOCX Manager initialized.")

        # Handle DB file
        if file_format == "db":
            if not (self.handle_existing_file(self.db_path, "DB")):
                self.db_manager =  DBManager(analysis_mode=self.mode)
                self.logger.info("DB Manager initialized.")
            else:
                self.db_manager =  DBManager()
                self.logger.info("DB Manager initialized.") 

    def create_file(self, file_type: str = "csv"):
        """_summary_

        Args:
            file_type (str, optional): File type used to save the data, can be "docx", "db", "csv", "pdf". Defaults to "csv".

        Returns:
            File: The file returned will be used to store the analysis data in.
        """
        self.file_type = file_type
        if file_type == "csv":
            self.file_name = f"{self.when}.csv"
        
        if self.file_exists(self.file_name):

            self.file_object = open(self.file_name, "a+")

            continue_with_existing_file = Confirm.ask("[bold green]Output file already exists, do you want to use it?", console=self.console)
            if continue_with_existing_file:
                self.logger.warning(f"Using existing file {self.file_name}")
                return self.file_object
            else:
                self.logger.warning("Exiting program, either delete/copy the existing output file or use it instead.")
                self.exit()


        else:
            try:

                with open(self.file_name, "w") as f:

                    if self.IS_FILE:
                        f.write("Hash,Positives,Community Score,File Type,File Size,File Name,Last Analysis\n")
                    elif self.IS_URL:
                        f.write("URL,Positives,Registrar,Creation Date,Last Analysis,Community Score\n")
                    elif self.IS_IP:
                        f.write("IP,Positives,Country,Last Analysis\n")


                self.file_object = open(self.file_name, "a+")
                self.logger.info(
                    f"Initialized file: {self.file_name}"
                )
            except FileNotFoundError:
                self.logger.error(
                    "Failed to create the results file!"
                )

            self.file_object = open(self.file_name, "a+")
            return self.file_object

    def close_file(self):
        if self.file_object:
            try:

                self.file_object.close()
                self.logger.info(
                    f"Closing file {self.file_name}\n"
                )
            except Exception as e:
                self.logger.error(f"\nError closing file\n")

    def save_csv(self, data, file):
        if self.IS_FILE:
            data_format = f"{data['file_hash']},{data['analysis']}, {data['community_score']},{data['file_type']},{data['file_size']},{data['file_name']},{data['last_analysis']}\n"
        elif self.IS_URL:
            data_format = ",".join([value for key, value in data.items()]) + "\n"        
        elif self.IS_IP:
            data_format = ",".join([value for key, value in data.items()]) + "\n"

        file.write(data_format)

    def add_db_report(self, data):
        self.db_manager.add_report(data=data)

    def save_db(self):
        self.db_manager.save_db()

    def add_docx_report(self, data):
        self.docx_manager.add_report(data=data)

    def save_docx(self):
        self.docx_manager.save("report.docx")

    def add_pdf_report(self, data):
            self.pdf_manager.add_report(data=data)

    def save_pdf(self):
        self.pdf_manager.output(f"{self.file_name}.pdf")

    def exit(self):
        sys.exit()

    def file_exists(self, file_path):
        return os.path.isfile(file_path)

    def handle_existing_file(self, file_path, file_type):
        if self.file_exists(file_path):
            answer = Confirm.ask(
                f"[bold orange]A {file_type} output file already exists. Continue?[/] "
                f"[bold red]This will replace the file with a new one.[/]",
                console=self.console
            )
            if answer:
                return True
            else:
                self.exit()
        
        else:
            return False