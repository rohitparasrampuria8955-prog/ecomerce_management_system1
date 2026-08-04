"""card.py - Card Payment implementation"""
from .payment import Payment


class CardPayment(Payment):
    def pay(self):
        print(f"Processing Card payment of {self.amount}...")
        print("Card Payment Successful")
        return True
