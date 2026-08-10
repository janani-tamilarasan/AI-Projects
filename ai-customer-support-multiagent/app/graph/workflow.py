from langgraph.graph import StateGraph, START, END

from .state import SupportState
from .nodes import supervisor, route_ticket

from app.agents.billing_agent import billing_agent
from app.agents.order_agent import order_agent
from app.agents.technical_agent import technical_agent
from app.agents.general_agent import general_agent


def create_support_graph():

    graph = StateGraph(SupportState)

    # -------------------------
    # Add Nodes
    # -------------------------

    graph.add_node(
        "supervisor",
        supervisor
    )

    graph.add_node(
        "billing_agent",
        billing_agent
    )

    graph.add_node(
        "order_agent",
        order_agent
    )

    graph.add_node(
        "technical_agent",
        technical_agent
    )

    graph.add_node(
        "general_agent",
        general_agent
    )

    # -------------------------
    # START
    # -------------------------

    graph.add_edge(
        START,
        "supervisor"
    )

    # -------------------------
    # Supervisor → Agent
    # -------------------------

    graph.add_conditional_edges(
        "supervisor",
        route_ticket,
        {
            "billing_agent": "billing_agent",
            "order_agent": "order_agent",
            "technical_agent": "technical_agent",
            "general_agent": "general_agent"
        }
    )

    # -------------------------
    # Agents → END
    # -------------------------

    graph.add_edge(
        "billing_agent",
        END
    )

    graph.add_edge(
        "order_agent",
        END
    )

    graph.add_edge(
        "technical_agent",
        END
    )

    graph.add_edge(
        "general_agent",
        END
    )

    return graph.compile()