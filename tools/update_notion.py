from google.adk.tools import Tool
from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))
DB_ID = os.getenv("NOTION_TRANSACTIONS_DB")

class UpdateNotionTool(Tool):
    def run(self, *, transactions: list) -> str:
        for txn in transactions:
            notion.pages.create(
                parent={"database_id": DB_ID},
                properties={
                    "Date": {"date": {"start": txn["date"]}},
                    "Description": {"title": [{"text": {"content": txn["description"]}}]},
                    "Amount": {"number": txn["amount"]},
                    "Category": {"select": {"name": txn["category"]}},
                },
            )
        return "Transactions pushed to Notion"