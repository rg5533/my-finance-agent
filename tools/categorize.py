from google.adk.tools import Tool
from vertexai.preview.language_models import TextGenerationModel

llm = TextGenerationModel.from_pretrained("text-bison")

class CategorizeTool(Tool):
    def run(self, *, transactions: list) -> list:
        categorized = []
        for txn in transactions:
            prompt = f"Categorize '{txn['description']}' of ${txn['amount']} into: Dining, Groceries, Entertainment, Bills, Travel, Other."
            category = llm.predict(prompt=prompt, temperature=0).text.strip()
            txn["category"] = category
            categorized.append(txn)
        return categorized