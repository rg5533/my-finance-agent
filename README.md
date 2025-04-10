# Finance Tracker Agent using Google ADK & Vertex AI

This project demonstrates how to build a fully autonomous, tool-driven AI agent using the **Google Agent Development Kit (ADK)** and deploy it to **Vertex AI Agents Runtime**.

## 🔧 Features

- Parses bank statement PDFs using Document AI (mocked)
- Categorizes transactions using Vertex AI LLM
- Updates and adjusts monthly budgets in Notion
- Sends email digest with budget insights
- Evaluation and deployment integrated with Vertex AI

## 📁 Project Structure

```
.
├── main.py                     # Agent definition and runtime
├── agent.yaml                  # Deployment config for ADK
└── tools/
    ├── extract_pdf.py          # Parses PDF bank statements
    ├── categorize.py           # LLM-based transaction categorization
    ├── update_notion.py        # Writes transactions to Notion
    ├── adjust_budget.py        # Budget logic for reallocation
    └── send_digest.py          # Sends finance summary email
```

## 🚀 Getting Started

1. **Install ADK**
   ```bash
   pip install google-agent-sdk
   ```

2. **Set environment variables**
   - `NOTION_TOKEN`
   - `NOTION_TRANSACTIONS_DB`
   - `SENDGRID_API_KEY`
   - `FROM_EMAIL`
   - `TO_EMAIL`

3. **Run locally**
   ```bash
   python main.py
   ```

4. **Deploy to Vertex AI**
   ```bash
   adk deploy
   ```

## 📊 Evaluation

This agent is configured to track **cost efficiency** using:
```python
evaluation={"metric": "cost_efficiency", "objective": "minimize_cost"}
```

## 📦 Built With

- Google ADK
- Vertex AI
- Notion API
- SendGrid
- Python 3.10+

---

Made for learning, scaling, and rethinking what agents can do.

