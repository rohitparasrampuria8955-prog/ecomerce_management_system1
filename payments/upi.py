"""upi.py - UPI Payment implementation"""
from .payment import Payment


class UPIPayment(Payment):
    def pay(self):
        print(f"Processing UPI payment of {self.amount}...")
        print("UPI Payment Successful")
        return True
