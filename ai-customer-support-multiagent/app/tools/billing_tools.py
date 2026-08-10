from langchain_core.tools import tool


@tool
def get_payment_details(order_id: str):
    """
    Get payment information for a specific order.
    """

    payments = {
        "ORD123": {
            "order_id": "ORD123",
            "amount": 2500,
            "payment_status": "duplicate",
            "currency": "INR"
        },
        "ORD456": {
            "order_id": "ORD456",
            "amount": 1500,
            "payment_status": "successful",
            "currency": "INR"
        },
        "ORD789": {
            "order_id": "ORD789",
            "amount": 3200,
            "payment_status": "failed",
            "currency": "INR"
        }
    }

    return payments.get(
        order_id,
        {
            "order_id": order_id,
            "payment_status": "not_found"
        }
    )