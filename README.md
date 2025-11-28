🧠 AIStockTrader_Zerodha
========================

**AIStockTrader_Zerodha** is an experimental **Agentic AI Proof of Concept (POC)** that autonomously analyzes financial transactions, calculates monthly savings, allocates investments across asset classes, and executes stock purchases via **Zerodha APIs** --- with **human approval in the loop**.

This project demonstrates a complete production-ready workflow combining **LangChain-based AI agents**, **Zerodha API automation**, and **FastAPI web interface** to create an intelligent, interactive AI-driven trading system.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python"> 
   <img src="https://img.shields.io/badge/LangChain-LangGraph%20Enabled-orange?logo=openai&logoColor=white" alt="LangChain LangGraph"> 
  <img src="https://img.shields.io/badge/Framework-Agentic%20AI-yellow?logo=ai&logoColor=white" alt="Agentic AI">
  <img src="https://img.shields.io/badge/Zerodha-Enabled-blue?logo=telegram&logoColor=white" alt="Zerodha API">
  <img src="https://img.shields.io/badge/KiteConnect-API%20Integrated-red?logo=cloudflare&logoColor=white" alt="KiteConnect API">
  <img src="https://img.shields.io/badge/FastAPI-0.110+-brightgreen?logo=fastapi&logoColor=white" alt="FastAPI"> 
  <img src="https://img.shields.io/badge/Status-POC%20Experiment-lightgrey" alt="Status">
</p>



🎯 Problem Statement
--------------------

Personal finance and investment decision-making present several challenges:

### 1\. **Time-Consuming Manual Analysis**

-   Individual investors spend hours analyzing transaction statements
-   Manual portfolio allocation decisions lack systematic guidance
-   Stock selection requires extensive research across multiple sources

### 2\. **Information Overload**

-   Multiple financial instruments and investment options available
-   Difficulty in determining optimal asset class allocation
-   Lack of data-driven personalized investment recommendations

### 3\. **Execution Friction**

-   Manual order placement is time-consuming and error-prone
-   Lack of automated, audit-tracked investment workflows
-   Need for reliable approval mechanisms before automated actions

### 4\. **Trust & Transparency Issues**

-   Users want to understand AI's reasoning before approval
-   Lack of transparent decision-making in investment tools
-   Need for human-in-the-loop controls for financial decisions

* * * * *

✨ Solution Overview
-------------------

AIStockTrader_Zerodha solves these challenges through an **intelligent, transparent, and human-controlled AI workflow**:

```
📄 Transaction Analysis → 💡 Smart Allocation → 📊 Stock Selection → ✅ Human Approval → 💹 Automated Execution

```

**Key Innovation:** Multi-agent LangGraph workflow with human-in-the-loop approval, combining AI automation with user trust and control.

* * * * *

🚀 Key Features
---------------

### ✅ Agentic Workflow

-   **Multi-agent pipeline** powered by LangGraph for complex reasoning
-   **Specialized agents** for transaction analysis, portfolio allocation, and stock selection
-   **Collaborative agent communication** with shared state management
-   **Tool-augmented agents** with access to financial data and APIs

### ✅ Human-in-the-Loop Approval

-   **User review stage** before any trade execution
-   **Clear decision transparency** showing AI reasoning and recommendations
-   **Approval/Rejection workflow** handled via intuitive web UI
-   **Audit trail** of all approval decisions and their timestamps

### ✅ Autonomous Stock Purchase

-   **Zerodha API integration** for real-time order placement
-   **POC simulation mode** for testing without real capital
-   **Order confirmation popups** with execution details
-   **Comprehensive action logging** of all trades and results

### ✅ Interactive Web Dashboard

-   **Real-time workflow visualization** showing each processing stage
-   **Step-by-step AI reasoning** displayed for transparency
-   **Clean, intuitive interface** optimized for quick decision-making
-   **Mobile-responsive design** for accessibility
-   **Live status updates** via WebSocket-ready architecture

### ✅ Configurable AI Logic

-   **Prompt template system** for customizable AI behavior
-   **Easy parameter tuning** without code changes
-   **Flexible agent instructions** for different investment strategies
-   **Temperature and model selection** for fine-tuning AI output

### ✅ Security & Reliability

-   **Secure credential management** via environment variables
-   **Secret key handling** with comprehensive .gitignore
-   **API key encryption** for Zerodha and LLM providers
-   **Rate limiting and backoff strategies** for API calls

* * * * *

🏗️ Architecture
----------------

### System Overview Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Frontend (Web UI)                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  HTML5 + JavaScript                                      │  │
│  │  - Transaction Upload Interface                          │  │
│  │  - Real-time Workflow Status Display                     │  │
│  │  - Approval Decision Buttons                             │  │
│  │  - Order Confirmation Notifications                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────────┘
                         │ HTTP/WebSocket
┌────────────────────────▼────────────────────────────────────────┐
│              Backend (FastAPI Server)                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  API Routes & State Management                           │  │
│  │  - POST /upload - Process transaction files              │  │
│  │  - GET /status - Retrieve workflow state                 │  │
│  │  - POST /approve - Submit approval decision              │  │
│  │  - GET /results - Fetch execution results                │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│         AI Agent Orchestration (LangGraph)                      │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Multi-Agent Pipeline                                    │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │  │
│  │  │ Transaction  │→ │  Portfolio   │→ │    Stock     │   │  │
│  │  │   Analyzer   │  │  Allocator   │  │   Picker     │   │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │  │
│  │         ↓                ↓                   ↓           │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │     Shared State (Finance Data Model)            │   │  │
│  │  │  - Savings Amount, Portfolio Allocation          │   │  │
│  │  │  - Investment Recommendations, Approval Status   │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ LLM API │    │ Finance │    │ Zerodha │
    │(Groq)   │    │  Tools  │    │   API   │
    └─────────┘    └─────────┘    └─────────┘

```

### Component Architecture

```
AIStockTrader_Zerodha/
│
├── src/
│   ├── api/
│   │   └── server.py                    # FastAPI backend, routes, WebSocket
│   │
│   ├── templates/
│   │   ├── index.html                   # Main web UI
│   │   ├── styles.css                   # UI styling
│   │   └── client.js                    # Frontend logic
│   │
│   ├── core/
│   │   ├── entity/
│   │   │   └── finance_state.py         # State model definition
│   │   │
│   │   ├── graph/
│   │   │   └── graph_creation.py        # LangGraph workflow creation
│   │   │
│   │   ├── helpers/
│   │   │   ├── load_prompt.py           # Prompt template loader
│   │   │   └── pdf_processor.py         # Transaction PDF parsing
│   │   │
│   │   ├── nodes/
│   │   │   ├── transaction_analyzer.py  # Transaction analysis node
│   │   │   ├── portfolio_allocator.py   # Asset allocation node
│   │   │   ├── stock_picker.py          # Stock selection node
│   │   │   ├── approval_node.py         # Human approval node
│   │   │   └── execution_node.py        # Order execution node
│   │   │
│   │   ├── tools/
│   │   │   ├── zerodha_tools.py         # Zerodha API wrapper
│   │   │   ├── financial_tools.py       # Financial calculations
│   │   │   └── data_tools.py            # Data retrieval tools
│   │   │
│   │   ├── prompts/
│   │   │   ├── system_prompt_*.txt      # System prompts for agents
│   │   │   └── user_prompt_*.txt        # User prompts for agents
│   │   │
│   │   └── utils/
│   │       ├── logger.py                # Logging configuration
│   │       ├── error_handler.py         # Error handling utilities
│   │       └── retry_handler.py         # Retry mechanism with backoff
│   │
│   ├── data/
│   │   └── transactions_november.pdf    # Sample transaction file
│   │
│   └── config.py                        # Configuration & LLM initialization
│
├── tests/
│   ├── test_agents.py                   # Agent unit tests
│   ├── test_api.py                      # API endpoint tests
│   ├── test_error_handling.py           # Error scenario tests
│   └── test_integration.py              # End-to-end workflow tests
│
├── logs/
│   └── app.log                          # Application logs
│
├── Dockerfile                           # Container configuration
├── docker-compose.yaml                  # Multi-container orchestration
├── requirements.txt                     # Python dependencies
├── .env.example                         # Environment template
├── .gitignore                           # Git ignore rules
├── LICENSE                              # License information
└── README.md                            # This file

```

* * * * *

🔄 System Workflow
------------------

The entire workflow follows a state machine pattern with five distinct stages:

### Stage 1️⃣: **Transaction Analysis Agent**

**Purpose:** Extract financial insights from user transactions

**Process:**

1.  User uploads bank statement or transaction PDF
2.  PDF is parsed and converted to text
3.  LLM agent analyzes transactions with financial reasoning
4.  Agent calculates total monthly savings using agent tools
5.  Results stored in shared workflow state

**State Output:**

```
{
    "monthly_transactions": [...],
    "total_income": 50000,
    "total_expenses": 37500,
    "monthly_savings": 12500,
    "current_step": "analyze_portfolio"
}

```

**AI Prompt Used:** `system_prompt_transaction_analyzer.txt`

**Error Handling:** PDF parsing failures trigger graceful error messages with retry options

* * * * *

### Stage 2️⃣: **Portfolio Allocator Agent**

**Purpose:** Recommend optimal asset class allocation based on savings

**Process:**

1.  Receives monthly savings amount from previous stage
2.  Applies financial heuristics and AI reasoning
3.  Allocates savings across asset classes:
    -   Equity (60%) - Growth-oriented
    -   Debt (30%) - Stability-focused
    -   Gold (10%) - Hedge against inflation
4.  Generates allocation explanation for transparency
5.  Updates workflow state with allocation details

**State Output:**

```
{
    "portfolio_allocation": {
        "equity": {"percentage": 60, "amount": 7500},
        "debt": {"percentage": 30, "amount": 3750},
        "gold": {"percentage": 10, "amount": 1250}
    },
    "allocation_reasoning": "...",
    "current_step": "select_stocks"
}

```

**AI Prompt Used:** `system_prompt_portfolio_allocator.txt`

* * * * *

### Stage 3️⃣: **Stock Picker Agent**

**Purpose:** Select specific stocks for equity allocation

**Process:**

1.  Receives equity allocation amount from portfolio agent
2.  Queries mock stock database or live APIs for recommendations
3.  Applies selection criteria:
    -   Market cap, sector diversity, performance metrics
4.  Recommends specific stocks with reasoning
5.  Prepares order details for human review

**State Output:**

```
{
    "investment_instruments": [
        {
            "tradingsymbol": "INFY",
            "company_name": "Infosys",
            "allocation_amount": 3750,
            "price": 1850,
            "quantity": 2,
            "reasoning": "..."
        },
        {
            "tradingsymbol": "TCS",
            "company_name": "Tata Consultancy",
            "allocation_amount": 3750,
            "price": 3500,
            "quantity": 1,
            "reasoning": "..."
        }
    ],
    "current_step": "awaiting_approval"
}

```

* * * * *

### Stage 4️⃣: **Human Approval Node**

**Purpose:** Enable user review and decision-making before execution

**Process:**

1.  Workflow pauses at this stage
2.  Web UI displays all recommendations with full reasoning
3.  User reviews:
    -   Transaction analysis
    -   Portfolio allocation breakdown
    -   Specific stock selections
4.  User clicks **Approve** or **Reject**
5.  Approval decision is timestamped and logged

**UI Interaction Flow:**

```
[Show Analysis] → [Display Allocation] → [List Stocks]
                                              ↓
                              [Approve Button] [Reject Button]

```

**Audit Trail:** All approvals logged with timestamp and user context

* * * * *

### Stage 5️⃣: **Stock Purchase Agent**

**Purpose:** Execute approved trades through Zerodha API

**Process:**

1.  If approved, agent receives confirmed stock list
2.  For each stock, creates market order:
    -   Calls Zerodha API to place order
    -   Implements retry logic with exponential backoff
    -   Handles API errors gracefully
3.  Captures order confirmation or error details
4.  Displays popup notification with results

**Order Execution Details:**

```
{
    "order_id": "230810000000001",
    "tradingsymbol": "INFY",
    "quantity": 2,
    "price": 1850,
    "status": "COMPLETED",
    "timestamp": "2025-11-28T14:30:00Z",
    "execution_details": {...}
}

```

**Error Scenarios Handled:**

-   Network timeouts → Retry with backoff
-   Insufficient funds → Graceful failure message
-   API rate limiting → Queue and retry
-   Zerodha AMO restrictions → Fallback to manual order

* * * * *

🎨 User Interface Design
------------------------

### Design Philosophy

The UI prioritizes **simplicity, transparency, and quick decision-making** through:

1.  **Clear Visual Hierarchy** - Most important information first
2.  **Real-time Feedback** - Users see workflow progress instantly
3.  **Decision Support** - All necessary information for informed approval
4.  **Minimal Friction** - One-click actions where possible

### Main UI Sections

#### 1\. **Upload Section**

```
┌─────────────────────────────────────┐
│  📤 Upload Transaction Statement    │
│  ┌─────────────────────────────────┐│
│  │ Drag & Drop or Click to Upload  ││
│  │ Supported: PDF, CSV              ││
│  └─────────────────────────────────┘│
│  [Start Analysis →]                 │
└─────────────────────────────────────┘

```

**Design Decisions:**

-   Drag-and-drop for ease of use
-   Format flexibility (PDF primary, CSV backup)
-   Clear call-to-action button

#### 2\. **Workflow Status Display**

```
┌─────────────────────────────────────┐
│  📊 Workflow Progress               │
│  ✅ Transaction Analysis Complete   │
│  ✅ Portfolio Allocation Complete   │
│  ✅ Stock Selection Complete        │
│  ⏳ Awaiting Your Approval...       │
└─────────────────────────────────────┘

```

**Design Decisions:**

-   Status indicators (✅ ⏳ ❌) for quick scanning
-   Sequential progress display
-   Milestones clearly marked

#### 3\. **Analysis Results Display**

```
┌──────────────────────────────────────────┐
│ 💰 Financial Analysis                    │
├──────────────────────────────────────────┤
│ Monthly Income:        ₹50,000           │
│ Monthly Expenses:      ₹37,500           │
│ Monthly Savings:       ₹12,500           │
│                                          │
│ 📊 Recommended Allocation                │
│ - Equity (60%):        ₹7,500            │
│ - Debt (30%):          ₹3,750            │
│ - Gold (10%):          ₹1,250            │
└──────────────────────────────────────────┘

```

**Design Decisions:**

-   Color-coded money values for clarity
-   Breakdown shows exact amounts
-   Icons aid quick understanding

#### 4\. **Stock Recommendations Display**

```
┌──────────────────────────────────────────┐
│ 📈 Recommended Stocks                    │
├──────────────────────────────────────────┤
│ 1. INFY (Infosys)                        │
│    - Allocation: ₹3,750                  │
│    - Current Price: ₹1,850               │
│    - Quantity: 2 shares                  │
│    - Reason: Growth leader in IT sector  │
│                                          │
│ 2. TCS (Tata Consultancy)                │
│    - Allocation: ₹3,750                  │
│    - Current Price: ₹3,500               │
│    - Quantity: 1 share                   │
│    - Reason: Stable dividend yield       │
└──────────────────────────────────────────┘

```

**Design Decisions:**

-   Card-based layout for multiple items
-   AI reasoning displayed for transparency
-   Clear financial metrics

#### 5\. **Approval Decision Section**

```
┌──────────────────────────────────────────┐
│ ✅ APPROVE THIS PLAN                     │
│    Proceed with stock purchase           │
│    [APPROVE →] [REJECT →]                │
│                                          │
│ ℹ️  This action will execute trades      │
│    on your Zerodha account               │
│    Review all details above before      │
│    making a decision                     │
└──────────────────────────────────────────┘

```

**Design Decisions:**

-   Prominent buttons for key decisions
-   Warning disclaimer for financial actions
-   Simple yes/no flow

#### 6\. **Execution Results Display**

```
┌──────────────────────────────────────────┐
│ ✅ ORDERS EXECUTED SUCCESSFULLY          │
├──────────────────────────────────────────┤
│ Order #1: INFY - 2 shares @ ₹1,850       │
│ Status: ✅ COMPLETED                      │
│ Order ID: 230810000000001                │
│                                          │
│ Order #2: TCS - 1 share @ ₹3,500         │
│ Status: ✅ COMPLETED                      │
│ Order ID: 230810000000002                │
│                                          │
│ Total Investment: ₹7,500                 │
│ [View Zerodha Portfolio →]               │
└──────────────────────────────────────────┘

```

**Design Decisions:**

-   Success confirmation with visual cues
-   Order details for reference
-   Link to broker dashboard for verification

### UI Interaction Flows

**Happy Path:**

```
Upload → Analyze → Review → Approve → Execute → Success

```

**Rejection Path:**

```
Upload → Analyze → Review → Reject → [Ask for Modifications]

```

**Error Path:**

```
Upload → Error → Show Message → [Retry] or [Cancel]

```

### Responsive Design Considerations

-   **Desktop (1024px+):** Full multi-column layout with side panels
-   **Tablet (768-1024px):** Stacked sections with collapsible panels
-   **Mobile (< 768px):** Single-column layout with swipe gestures

* * * * *

⚙️ Technical Stack
------------------

| Layer | Technology | Purpose | Rationale |
| --- | --- | --- | --- |
| **Frontend** | HTML5 + CSS3 | Web interface | Simple, no build step required |
| **Frontend Logic** | JavaScript (Vanilla) | Client-side interactions | Lightweight, no framework overhead |
| **Backend Framework** | FastAPI 0.115+ | REST API server | Fast, modern, auto-docs |
| **Backend Runtime** | Python 3.10+ | Application runtime | Rich ecosystem, AI/ML libraries |
| **AI Orchestration** | LangGraph | Multi-agent workflow | State machine, tool calling |
| **LLM Provider** | Groq (Llama 3.3) | Language model inference | Fast, cost-effective |
| **LLM Framework** | LangChain | Agent prompting, tools | Proven patterns, wide adoption |
| **Finance API** | Zerodha Kiteconnect | Stock trading | India's largest retail broker |
| **Document Processing** | PyPDF2 | Transaction PDF parsing | Lightweight, reliable |
| **Data Manipulation** | Pandas | Financial data handling | Standard in finance domain |
| **Logging** | Loguru | Application logging | Structured, colorized logs |
| **Environment Config** | python-dotenv | Secrets management | Standard practice |
| **Server Deployment** | Uvicorn | ASGI server | FastAPI standard |
| **Containerization** | Docker | Application packaging | Reproducible deployment |
| **Orchestration** | Docker Compose | Multi-service setup | Local development + testing |

* * * * *

📦 Installation & Setup
-----------------------

### Prerequisites

Before starting, ensure you have:

-   **Python 3.10 or higher** installed
-   **Git** for version control
-   **pip** package manager
-   **API Keys:**
    -   Groq API key (for LLM)
    -   Zerodha API credentials (for trading)

### Step 1: Clone the Repository

```
git clone https://github.com/yourusername/AIStockTrader_Zerodha.git
cd AIStockTrader_Zerodha

```

### Step 2: Create Virtual Environment

```
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

```

### Step 3: Install Dependencies

```
pip install -r requirements.txt

```

This installs:

-   `fastapi>=0.115.0` - Web framework
-   `uvicorn[standard]>=0.30.0` - ASGI server
-   `langchain-groq` - LLM integration
-   `langgraph` - Agent orchestration
-   `kiteconnect` - Zerodha API
-   `PyPDF2` - PDF parsing
-   `loguru` - Logging
-   `python-dotenv` - Configuration
-   `pandas` - Data handling
-   `jinja2` - Template rendering

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```
cp .env.example .env

```

Edit `.env` with your credentials:

```
# LLM Configuration
GROQ_API_KEY=your_groq_api_key_here
GROQ_LLM_MODEL=llama-3.3-70b-versatile

# Zerodha Configuration
ZERODHA_API_KEY=your_zerodha_api_key
ZERODHA_SECRET_KEY=your_zerodha_secret_key
REQUEST_TOKEN_FROM_URL=https://kite.zerodha.com/connect/login?v=3&api_key=API_KEY
ZERODHA_ACCESS_TOKEN=your_zerodha_access_token

# Application Configuration
DEBUG=True
LOG_LEVEL=INFO
ENVIRONMENT=development

```

### Step 5: Run the Application

```
uvicorn src.api.server:app --reload --host 0.0.0.0 --port 8000

```

**Output:**

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete

```

### Step 6: Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:8000

```

* * * * *


**Custom Error Handling Framework**
===================================

🔥 Custom Exception Framework
-----------------------------

To improve reliability and make debugging easier, the project now includes a **centralized custom exception hierarchy** located in:

`src/utils/exceptions.py`

### ⭐ Key Features

-   Provides **clear, meaningful error types** instead of generic exceptions

-   Allows the retry system to differentiate between retryable and non-retryable failures

-   Makes debugging easier by showing **high-level, human-readable messages**

### 📌 Available Exceptions

| Exception Name | Purpose |
| --- | --- |
| **AppError** | Base class for all app errors |
| **PDFReadError** | PDF extraction failures |
| **ZerodhaAPIError** | Problems calling Zerodha APIs / LTP fetch |
| **ToolExecutionError** | Generic tool-level failure |
| **RetryableError** | Forces retry mechanism |

### 📘 Why we need this

-   Clear separation of failure types

-   Better error propagation in agents

-   Unified error handling across the system



**Retry System With Exponential Backoff**
=========================================

🔁 Exponential Backoff Retry Framework
--------------------------------------

A reusable `@retry` decorator has been added to automatically retry failing operations.

📍 File:

`src/utils/retry.py`

### ⭐ Features

-   Retry unstable functions (e.g., network calls, API requests)

-   Exponential backoff (`delay → delay * backoff`)

-   Optional jitter to prevent retry storms

-   Logs all retry attempts

-   Supports custom retryable exception types

### 📌 Example Usage

`@retry(max_attempts=5, delay=2, backoff=2, retry_on=(ZerodhaAPIError,))
def fetch_prices():
    return kite.ltp(['NSE:INFY'])`

### 📘 Why we need this

-   Makes your agents **fault tolerant**

-   Prevents instant failures on temporary API issues

-   Ensures stable and smooth execution



**Centralized Structured Logging System**
=========================================

📝 Central Logging System (Console + File Logs)
-----------------------------------------------

A production-grade logging system has been added using **Loguru**.

📍 File:

`src/utils/logger.py`

### ⭐ Features

-   Colorized, detailed console logs

-   Persistent file logging (`logs/app.log`)

-   Automatic log rotation (10MB max → zipped rotate)

-   Backtrace + diagnose mode for debugging

-   Zero `print()` calls --- entire app uses `logger`

### 📌 Example

`from src.utils.logger import logger

logger.info("Starting stock suggestion tool...")
logger.success("Order placement complete")
logger.error("Failed to fetch Zerodha data")`

### 📘 Why we need this

-   Helps track errors quickly

-   Works seamlessly inside FastAPI + agents

-   Enables auditability for production

**Test Suite (pytest)**
=======================

🧪 Automated Test Suite Added
-----------------------------

A complete test suite is now added under:

`tests/`

### Tests cover:

-   PDF reader tool

-   Portfolio builder logic

-   Retry decorator behavior

-   Stock suggestion tool

-   Core utilities

### ⭐ Run Tests

`pytest -v`

### 📘 The above tests ensure

-   Ensures agents and tools work as expected

-   Reduces regressions as features grow

-   Makes CI/CD-ready

**Docker & Docker Compose Support**
===================================

🐳 Dockerized Deployment Ready
------------------------------

The project now supports full containerization.

### 📁 Files Added

-   `Dockerfile`

-   `docker-compose.yml`

### ⭐ How to Run (Local or Production)

`docker-compose up --build`

### Mounted volumes

-   `./data → /app/data`

-   `./logs → /app/logs`

### 🧰 Why this matters

-   Consistent environment

-   Easy to run anywhere

-   Cloud/server deployment-ready

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




* * * * *

🔐 Zerodha API Integration Guide
================================

This project integrates with the **Zerodha KiteConnect API** for accessing live market data, fetching LTPs, and placing buy orders.\
To use these features, you must configure your **environment variables** correctly.

* * * * *

🧩 Required Environment Variables
=================================

Create a `.env` file in the project root:

```
# Zerodha API
KITE_API_KEY=your_api_key
KITE_API_SECRET=your_api_secret
KITE_REQUEST_TOKEN=your_request_token

# Optional
KITE_ACCESS_TOKEN=your_access_token

```

### Meaning of Each Variable

| Variable | Purpose | Required |
| --- | --- | --- |
| `KITE_API_KEY` | Identifies your app on Zerodha | ✔ |
| `KITE_API_SECRET` | Secret used to generate session token | ✔ |
| `KITE_REQUEST_TOKEN` | Temporary token obtained after login | ✔ |
| `KITE_ACCESS_TOKEN` | Permanent session token (once generated) | Optional (auto-generated if not provided) |

* * * * *

🧭 Step-by-Step: How to Obtain Zerodha API Credentials
======================================================

Follow these steps carefully.

1️⃣ Create a Zerodha Developer Account
--------------------------------------

1.  Go to **<https://developers.kite.trade/>**

2.  Log in using your regular Zerodha credentials.

3.  Subscribe to the **KiteConnect API** (paid monthly).

4.  Create a **new app**.

You will immediately get:

-   **API Key**

-   **API Secret**

Add these to `.env`.

* * * * *

2️⃣ Generate Daily Request Token (Manual Step)
----------------------------------------------

Zerodha requires you to generate a **new request token each day**.

To generate it:

1.  Open the login URL:

```
https://kite.trade/connect/login?api_key=YOUR_API_KEY

```

1.  Log in using:

-   Zerodha User ID

-   Password

-   Pin

1.  After login, you will be redirected to your **redirect URL**.\
    It will look like this:

```
https://your-redirect-url.com/?status=success&request_token=abcd1234efgh5678

```

1.  Copy the value of `request_token`.\
    Example:

```
KITE_REQUEST_TOKEN=abcd1234efgh5678

```

* * * * *

3️⃣ Generate `access_token` (Once per day)
------------------------------------------

In your project code, session generation is done via:

```
data = kite.generate_session(request_token, api_secret=API_SECRET)
kite.set_access_token(data["access_token"])

```

You can print the value or log it for reference:

```
logger.info(f"Access Token: {data['access_token']}")

```

Add it to `.env` if you want persistent usage:

```
KITE_ACCESS_TOKEN=your_access_token

```

* * * * *

🛠 How the Project Uses Zerodha API Internally
==============================================

### 📌 Fetching Live Market Prices

Used in:

```
src/core/tools/stock_suggest.py

```

Wrapped with retry logic:

```
@retry(max_attempts=6, delay=2)
def _safe_ltp_call(kite, symbols):
    return kite.ltp(symbols)

```

* * * * *

### 📌 Placing Live Orders

Used in:

```
src/core/tools/stock_buy.py

```

Example:

```
order = kite.place_order(
    tradingsymbol=symbol,
    exchange="NSE",
    quantity=quantity,
    transaction_type="BUY",
    order_type="MARKET",
    product="CNC"
)

```

Includes:

-   structured logs

-   retry for network/API errors

-   custom ZerodhaAPIError for failures

* * * * *

⚠️ Important Notes About Zerodha API
-------------------------------------

-   **Request token expires every few minutes**, so you must generate it daily.

-   **Access token expires at the end of each trading day**.

-   Zerodha does NOT allow auto-login --- must authenticate manually.

-   You must subscribe to **KiteConnect API (₹500/month)**.

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

