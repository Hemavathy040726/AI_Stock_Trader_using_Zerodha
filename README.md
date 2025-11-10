🧠 AIStockTrader_Zerodha
========================

**AIStockTrader_Zerodha** is an experimental **Agentic AI Proof of Concept (POC)** that autonomously analyzes financial transactions, calculates monthly savings, allocates investments across asset classes, and executes stock purchases via **Zerodha APIs** --- with **human approval in the loop**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.110+-brightgreen?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/LangChain-LangGraph%20Enabled-orange?logo=openai&logoColor=white" alt="LangChain LangGraph">
  <img src="https://img.shields.io/badge/Framework-Agentic%20AI-yellow?logo=ai&logoColor=white" alt="Agentic AI">
  <img src="https://img.shields.io/badge/Status-POC%20Experiment-lightgrey" alt="Status">
</p>

<p align="center">
  <a href="https://fastapi.tiangolo.com" target="_blank">
    <img src="https://img.shields.io/badge/Powered%20by-FastAPI-green?style=for-the-badge&logo=fastapi&logoColor=white">
  </a>
  <a href="https://python.org" target="_blank">
    <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white">
  </a>
  <a href="https://www.zerodha.com" target="_blank">
    <img src="https://img.shields.io/badge/Zerodha%20Integration-Enabled-lightblue?style=for-the-badge&logo=zerodha&logoColor=white">
  </a>
</p>


It demonstrates the integration of **LangChain-based AI agents**, **Zerodha API automation**, and **FastAPI web interface** to form a fully interactive AI-driven trading workflow.

* * * * *

🚀 Features
-----------

✅ **Agentic Workflow**

-   Multi-agent pipeline powered by LangGraph.

-   Agents perform PDF transaction analysis, portfolio allocation, and stock selection.

✅ **Human-in-the-Loop Approval**

-   Before executing trades, the AI waits for human confirmation.

-   Approval flow handled via a clean web UI.

✅ **Autonomous Stock Purchase**

-   Executes trades through Zerodha API (POC simulation or real integration).

-   Logs all actions and results in the system state.

✅ **Interactive Web Dashboard**

-   Built with FastAPI + HTML + JS.

-   Displays AI reasoning, suggested stocks, and final order execution results.

-   Includes popup notifications for executed orders.

✅ **Configurable Prompts**

-   AI reasoning logic is defined through prompt templates:

    -   `system_prompt_transaction_analyzer.txt`

    -   `user_prompt_transaction_analyzer.txt`

* * * * *

🧩 Architecture Overview
------------------------

```
AIStockTrader_Zerodha/
│
├── src/
│   ├── api/
│   │   └── server.py               # FastAPI backend + web routes
│   │
│   ├── templates/
│   │   └── index.html              # Frontend web UI
│   │
│   ├── core/
│   │   ├── entity/
│   │   │   └── finance_state.py    # Shared workflow state definition
│   │   ├── graph/
│   │   │   └── graph_creation.py   # LangGraph agent workflow creation
│   │   ├── helpers/
│   │   │   └── all helpers     # Utility to load prompt templates
│   │   └── nodes/
│   │   |   └── all agent nodes with tool nodes  # Core agent logic
│   │   └── tools/
│   │           └── all tools definition # tools used by agents
│   │
│   └── data/
│       └── transactions_november.pdf # Sample transaction file
│
└── README.md

```

* * * * *

🧠 Workflow Summary
-------------------

### 1️⃣ Transaction Analyzer Agent

Reads and interprets the uploaded bank statement or PDF of monthly transactions to determine **total monthly savings**.

### 2️⃣ Portfolio Allocator Agent

Allocates savings into asset classes (Equity, Debt, Gold, etc.) using simple AI-based heuristics.

### 3️⃣ Stock Picker Agent

Fetches stock recommendations (from mock data or live APIs) and proposes an equity investment strategy.(we address only stocks here)

### 4️⃣ Human Approval Stage

Displays the AI's decision and waits for human input --- *Approve* or *Reject*.

### 5️⃣ Stock Purchase Agent

If approved, executes the trade through Zerodha's API (real or simulated), then displays the result in UI.

* * * * *

🌐 Web Interface
----------------

A simple and elegant UI is served via **FastAPI**.

### ▶️ Run Workflow

Click **Start Workflow** to let the AI analyze transactions and suggest investments.

### 🧾 Approval

When prompted, click **Approve** or **Reject**.\
If approved, the agent will attempt to execute the order and display a popup notification with order details.

* * * * *

⚙️ Installation & Setup
-----------------------

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/AIStockTrader_Zerodha.git
cd AIStockTrader_Zerodha

```

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate     # (Linux/macOS)
.venv\Scripts\activate        # (Windows)

```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt

```

### 4️⃣ Run the Server

```
uvicorn src.api.server:app --reload

```

Then open your browser and visit:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000/)**

* * * * *

🧰 Tech Stack
-------------

| Layer | Technology | Purpose |
| --- | --- | --- |
| **Frontend** | HTML + JS | Interactive web UI |
| **Backend** | FastAPI | Handles workflow execution |
| **AI Engine** | LangChain + LangGraph | Multi-agent workflow |
| **Finance Logic** | Python + Zerodha APIs | Trade simulation / execution |
| **State Management** | Custom `State` class | Tracks agent data flow |

* * * * *

🧪 Example Output
-----------------

```
💰 Total Savings: ₹12,500
📊 Portfolio: {'Equity': 60%, 'Debt': 30%, 'Gold': 10%}
📈 Suggested Stocks: [{'tradingsymbol': '364D100926-TB', 'price': 94.75}]
⏳ Awaiting Approval: True
✅ Approved: True
💹 Executed Order: Stock purchase executed ❌ Failed to place order: AMO not allowed.
📌 Status: Executing stock purchase...

```

* * * * *

🧭 Future Enhancements
----------------------

-   🔗 Zerodha Complete Trading

-   🔄 Support for multiple brokers (Groww, AngelOne, Upstox)

-   🧠 Reinforcement learning--based allocation logic

-   📈 Portfolio visualization dashboard

-   🔒 End-to-end encryption of transaction data

* * * * *

⚠️ Disclaimer
-------------

This project is a **proof of concept (POC)** for educational and research purposes.\
It should **not be used for live trading without appropriate risk controls** and regulatory compliance.

* * * * *

👩‍💻 Author
------------

**Hema R.**\
AI Researcher | Python Developer

* * * * *
