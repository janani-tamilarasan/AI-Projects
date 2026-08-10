from langgraph.graph import StateGraph, START, END

from app.agents.billing_state import BillingState

from app.agents.billing_nodes import (
    billing_llm_node,
    billing_tool_node
)


def should_continue(state: BillingState):
    """
    Decide whether the Billing Agent should call a tool
    or finish the workflow.
    """

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"


def create_billing_graph():
    """
    Create and compile the Billing Agent workflow.
    """

    graph = StateGraph(BillingState)

    # LLM node
    graph.add_node(
        "billing_llm",
        billing_llm_node
    )

    # Tool node
    graph.add_node(
        "billing_tools",
        billing_tool_node
    )

    # START → LLM
    graph.add_edge(
        START,
        "billing_llm"
    )

    # LLM → Tool OR END
    graph.add_conditional_edges(
        "billing_llm",
        should_continue,
        {
            "tools": "billing_tools",
            "end": END
        }
    )

    # Tool → LLM
    graph.add_edge(
        "billing_tools",
        "billing_llm"
    )

    return graph.compile()