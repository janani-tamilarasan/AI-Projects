from app.llm import llm
from app.tools.billing_tools import get_payment_details

from langgraph.prebuilt import ToolNode


# Give Gemini access to the billing tool
billing_llm = llm.bind_tools(
    [get_payment_details]
)


def billing_llm_node(state):
    """
    Billing Agent LLM.

    Gemini receives the conversation and decides
    whether it needs to call the billing tool.
    """

    response = billing_llm.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# LangGraph executes tool calls through this node
billing_tool_node = ToolNode(
    [get_payment_details]
)