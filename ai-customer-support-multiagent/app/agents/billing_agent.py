from langchain_core.messages import HumanMessage

from app.agents.billing_workflow import create_billing_graph


# Create Billing Agent graph once
billing_graph = create_billing_graph()


def billing_agent(state):
    """
    Adapter between the Main Support Graph
    and the Billing Agent subgraph.
    """

    ticket = state["ticket"]

    # Convert SupportState ticket into BillingState messages
    result = billing_graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=ticket
                )
            ]
        }
    )

    # Last message should contain the final LLM response
    final_message = result["messages"][-1]

    return {
        "agent_result": final_message.content
    }