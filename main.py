from google.adk.agents import Agent
from tools.extract_pdf import ExtractPDFTool
from tools.categorize import CategorizeTool
from tools.update_notion import UpdateNotionTool
from tools.adjust_budget import AdjustBudgetTool
from tools.send_digest import SendDigestTool

agent = Agent(
    tools=[
        ExtractPDFTool(),
        CategorizeTool(),
        UpdateNotionTool(),
        AdjustBudgetTool(),
        SendDigestTool(),
    ],
    description="An autonomous finance agent that extracts, categorizes, budgets, and reports transactions.",
    evaluation={"metric": "cost_efficiency", "objective": "minimize_cost"},
    agentspace={
        "display_name": "Finance Tracker Agent",
        "tags": ["finance", "automation", "budgeting"]
    }
)

if __name__ == "__main__":
    agent.run()