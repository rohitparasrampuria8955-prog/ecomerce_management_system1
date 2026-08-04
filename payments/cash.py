"""cash.py - Cash Payment implementation"""
from .payment import Payment


class CashPayment(Payment):
    def pay(self):
        print(f"Processing Cash payment of {self.amount}...")
        print("Cash Payment Successful")
        return True
