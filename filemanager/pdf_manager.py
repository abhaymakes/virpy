from fpdf import FPDF
from datetime import datetime
from helper import Helper

class PDFManager(FPDF):
    
    def __init__(self, analysis_mode = "file", orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)

        self.mode = analysis_mode
        self.helper =Helper()

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
        fields = self.helper.get_data_fields(data=data, mode=self.mode)

        for field, value in fields:
            self.set_font("Arial", "B", 10)
            self.cell(50, 6, f"{field}")
            self.set_font("Arial", "", 10)
            self.cell(0, 6, value, 0, 1)

        self.ln(5) 

        # Add a divider
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

        self.is_first_page = False