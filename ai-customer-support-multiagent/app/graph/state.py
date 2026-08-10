from typing import TypedDict

class SupportState(TypedDict):
    customer_id: str
    ticket: str
    category: str
    agent_result: str
    final_response: str