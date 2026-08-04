"""
payment.py
Base class for all payment types. STEP 5 - Polymorphism.
"""


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        raise NotImplementedError("Subclasses must implement pay()")
