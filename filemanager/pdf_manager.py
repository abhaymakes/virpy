from fpdf import FPDF
from datetime import datetime

class PDFManager(FPDF):


    is_first_page = True
    when = datetime.now()

    def header(self):
        if self.is_first_page:  
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "Automated VirusTotal Report", 0, 1)
            self.set_font("Arial", "I", 8)  
            self.cell(0, 10, f"Generated on {self.when.strftime("%d %B, %Y at %I:%M %p")}", 0, 1)

    def add_report(self, data):

        # Add fields
        fields = [
            ("SHA256 Hash", data.get("file_hash", "N/A")),
            ("Analysis", data.get("analysis", "N/A")),
            ("Reputation", str(data.get("community_score", "N/A"))),
            ("File Type", str(data.get("file_type", "N/A"))),
            ("File Size", str(data.get("file_size", "N/A"))),
            ("File Name", data.get("file_name", "N/A")),
            ("Last Analysis Date", data.get("file_last_analysis", "N/A")),
        ]

        for field, value in fields:
            self.set_font("Arial", "B", 10)
            self.cell(50, 6, f"{field}")
            self.set_font("Arial", "", 10)
            self.cell(0, 6, value, 0, 1)

        self.ln(5)  # Add space between reports

        # Add a divider
        self.set_draw_color(200, 200, 200)  # Set gray color
        self.line(10, self.get_y(), 200, self.get_y())  # Draw a line
        self.ln(5)  # Add space after the divider

        self.is_first_page = False


