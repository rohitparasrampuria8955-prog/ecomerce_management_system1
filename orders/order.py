"""
order.py
Defines the Order class.
"""


class Order:
    def __init__(self, order_id, customer_id, products, total_amount, order_date, payment_status="Pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = products              # list of product names
        self.total_amount = total_amount
        self.order_date = order_date
        self.payment_status = payment_status  # "Paid" / "Pending" / "Cancelled"

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "products": self.products,
            "amount": self.total_amount,
            "order_date": self.order_date,
            "status": self.payment_status
        }

    @staticmethod
    def from_dict(order_id, data):
        return Order(
            order_id,
            data.get("customer_id"),
            data.get("products", []),
            data.get("amount", 0),
            data.get("order_date", ""),
            data.get("status", "Pending")
        )

    def __str__(self):
        return (f"Order#{self.order_id} | Customer:{self.customer_id} | "
                f"Products:{', '.join(self.products)} | Amount:{self.total_amount} | "
                f"Status:{self.payment_status}")
