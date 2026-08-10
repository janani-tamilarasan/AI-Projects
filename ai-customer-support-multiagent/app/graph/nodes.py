from .state import SupportState
from app.llm import llm
from app.schemas import TicketClassification

def analyze_ticket(state: SupportState):

    ticket = state["ticket"].lower()

    if "payment" in ticket or "charged" in ticket or "refund" in ticket:
        category = "billing"

    elif "order" in ticket or "delivery" in ticket or "shipping" in ticket:
        category = "order"

    elif "login" in ticket or "error" in ticket or "crash" in ticket:
        category = "technical"

    else:
        category = "general"

    return {
        "category": category
    }

def route_ticket(state: SupportState):

    category = state["category"]

    if category == "billing":
        return "billing_agent"

    elif category == "order":
        return "order_agent"

    elif category == "technical":
        return "technical_agent"

    else:
        return "general_agent"

def supervisor(state: SupportState):

    ticket = state["ticket"]

    structured_llm = llm.with_structured_output(
        TicketClassification
    )

    result = structured_llm.invoke(
        f"""
        You are the supervisor of an AI customer support system.

        Classify the following customer support ticket into exactly
        one of these categories:

        - billing
        - order
        - technical
        - general

        Ticket:
        {ticket}

        Return only the classification.
        """
    )

    return {
        "category": result.category
    }