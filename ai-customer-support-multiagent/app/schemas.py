from pydantic import BaseModel
from typing import Literal


class TicketRequest(BaseModel):
    customer_id: str
    ticket: str


class TicketClassification(BaseModel):
    category: Literal[
        "billing",
        "order",
        "technical",
        "general"
    ]