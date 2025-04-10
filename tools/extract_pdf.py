from google.adk.tools import Tool
from google.cloud import documentai_v1 as documentai
from google.api_core.client_options import ClientOptions
import os

class ExtractPDFTool(Tool):
    def run(self, *, file_path: str) -> list:
        project_id = os.getenv("GCP_PROJECT_ID")
        location = os.getenv("GCP_LOCATION", "us")  # e.g. "us" or "eu"
        processor_id = os.getenv("DOCUMENT_AI_PROCESSOR_ID")

        # Read PDF
        with open(file_path, "rb") as f:
            content = f.read()

        client = documentai.DocumentProcessorServiceClient(
            client_options=ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        )
        name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

        request = {
            "name": name,
            "raw_document": {
                "content": content,
                "mime_type": "application/pdf",
            },
        }

        result = client.process_document(request=request)
        document = result.document

        # Basic parsing from text blocks
        lines = document.text.split("\n")
        transactions = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    amount = float(parts[-1].replace("$", "").replace(",", ""))
                    date = parts[0]
                    description = " ".join(parts[1:-1])
                    transactions.append({
                        "date": date,
                        "description": description,
                        "amount": amount
                    })
                except ValueError:
                    continue

        return transactions
