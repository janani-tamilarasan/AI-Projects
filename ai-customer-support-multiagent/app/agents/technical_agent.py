from app.graph.state import SupportState


def technical_agent(state: SupportState):

    ticket = state["ticket"]

    response = (
        f"Technical Agent received the ticket: {ticket}. "
        "The technical issue needs to be investigated."
    )

    return {
        "agent_result": response
    }