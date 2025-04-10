from google.adk.tools import Tool

class AdjustBudgetTool(Tool):
    def run(self, *, transactions: list) -> list:
        total_by_cat = {}
        actions = []
        for txn in transactions:
            cat = txn["category"]
            total_by_cat[cat] = total_by_cat.get(cat, 0) + txn["amount"]
        if total_by_cat.get("Dining", 0) > 300:
            actions.append({"from": "Dining", "to": "Groceries", "amount": 100})
        return actions