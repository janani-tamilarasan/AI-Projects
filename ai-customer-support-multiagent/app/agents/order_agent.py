from app.graph.state import SupportState


def order_agent(state: SupportState):

    ticket = state["ticket"]

    response = (
        f"Order Agent received the ticket: {ticket}. "
        "The order status needs to be investigated."
    )

    return {
        "agent_result": response
    }