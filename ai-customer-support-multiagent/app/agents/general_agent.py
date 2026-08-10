from app.graph.state import SupportState


def general_agent(state: SupportState):

    ticket = state["ticket"]

    response = (
        f"General Support Agent received the ticket: {ticket}. "
        "We will review your request."
    )

    return {
        "agent_result": response
    }