from fastapi import FastAPI

from app.graph.workflow import create_support_graph
from app.schemas import TicketRequest


app = FastAPI(
    title="AI Customer Support Multi-Agent System"
)


graph = create_support_graph()


@app.get("/")
def root():
    return {
        "message": "AI Customer Support API is running"
    }


@app.post("/tickets")
def create_ticket(request: TicketRequest):

    initial_state = {
        "customer_id": request.customer_id,
        "ticket": request.ticket,
        "category": "",
        "agent_result": "",
        "final_response": ""
    }

    result = graph.invoke(initial_state)

    return {
        "customer_id": result["customer_id"],
        "ticket": result["ticket"],
        "category": result["category"],
        "agent_result": result["agent_result"]
    }