from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from langchain_core.messages import SystemMessage, HumanMessage

from src.core.entity.finance_state import State
from src.core.graph.graph_creation import create_agent
from src.core.helpers.load_prompt import load_prompt

app = FastAPI(title="Monthly Stock Picker - Full Workflow")

# -------------------------------
# Template setup
# -------------------------------
templates = Jinja2Templates(directory="src/templates")

# -------------------------------
# Globals for workflow
# -------------------------------
workflow_state: State = None
agent = None

# -------------------------------
# Run full agent workflow in stages
# -------------------------------
def run_full_agent_workflow(state: State, approved: bool = None):
    global agent
    if agent is None:
        agent = create_agent()  # compiled graph

    # Update approval if provided
    if approved is not None:
        state["approved"] = approved
        state["awaiting_approval"] = False
        state["current_step"] = "buy_stock"

    # If already awaiting approval, don’t rerun
    if state.get("current_step") == "awaiting_approval" and state.get("investment_instruments"):
        return state

    # Run the agent graph only once
    final_state = agent.invoke(state)
    return final_state


# -------------------------------
# Serve HTML
# -------------------------------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------------------
# API Endpoint for workflow
# -------------------------------
@app.post("/run_workflow")
async def run_workflow(approved: str = Query(default=None)):
    global workflow_state

    # Convert approval string to boolean
    approved_bool = None
    if approved is not None:
        approved_bool = approved.lower() in ["true", "1", "yes", "y"]

    # Initialize workflow state if not started
    if workflow_state is None:
        system_prompt = load_prompt("system_prompt_transaction_analyzer.txt")
        user_prompt = load_prompt("user_prompt_transaction_analyzer.txt")
        human_prompt = user_prompt.format(test_pdf="data/transactions_november.pdf")

        workflow_state = State(
            messages=[
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ],
            total_savings=None,
            formatted_savings=None,
            user_age=35,
            insured=False,
            portfolio=None,
            investment_instruments=None,
            executed_order=None,
            investment_execution=None,
            awaiting_approval=True,
            approved=None,
            progress=0,
            current_step="stock_picker",
            status_message="Running Stock Picker..."
        )

    # Run workflow once per approval stage
    workflow_state = run_full_agent_workflow(workflow_state, approved=approved_bool)

    # Update status messages
    if workflow_state.get("awaiting_approval"):
        workflow_state["status_message"] = "Human approval required."
    elif workflow_state.get("current_step") == "buy_stock":
        workflow_state["status_message"] = "Executing stock purchase..."
    else:
        workflow_state["status_message"] = "Workflow complete."

    return JSONResponse(content={
        "total_savings": workflow_state.get("total_savings"),
        "portfolio": workflow_state.get("portfolio"),
        "suggested_stocks": workflow_state.get("investment_instruments"),
        "awaiting_approval": workflow_state.get("awaiting_approval"),
        "approved": workflow_state.get("approved"),
        "executed_order": workflow_state.get("executed_order"),
        "investment_execution": workflow_state.get("investment_execution"),
        "status_message": workflow_state.get("status_message")
    })
