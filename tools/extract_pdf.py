from google.adk.tools import Tool

class ExtractPDFTool(Tool):
    def run(self, *, file_path: str) -> list:
        return [
            {"date": "2025-03-01", "description": "Uber Eats", "amount": 42.15},
            {"date": "2025-03-02", "description": "Whole Foods", "amount": 95.00},
            {"date": "2025-03-05", "description": "Netflix", "amount": 15.99},
        ]