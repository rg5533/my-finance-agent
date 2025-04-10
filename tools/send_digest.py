from google.adk.tools import Tool
import sendgrid
from sendgrid.helpers.mail import Mail
import os

class SendDigestTool(Tool):
    def run(self, *, transactions: list, adjustments: list) -> str:
        summary = "Finance Digest:\n"
        for txn in transactions:
            summary += f"{txn['date']} - {txn['description']} - ${txn['amount']} - {txn['category']}\n"
        if adjustments:
            summary += "\nBudget Adjustments:\n"
            for adj in adjustments:
                summary += f"Moved ${adj['amount']} from {adj['from']} to {adj['to']}\n"
        sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
        message = Mail(
            from_email=os.getenv("FROM_EMAIL"),
            to_emails=os.getenv("TO_EMAIL"),
            subject='Monthly Budget Update',
            plain_text_content=summary
        )
        sg.send(message)
        return "Email sent"