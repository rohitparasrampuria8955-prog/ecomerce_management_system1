"""
customer.py
Defines User (base class), Customer, and Admin.
Demonstrates: OOP Inheritance (STEP 10)
"""


class User:
    """Base class for anyone using the system."""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_role(self):
        return "User"

    def __str__(self):
        return f"[{self.display_role()}] {self.id} - {self.name}"


class Customer(User):
    """A registered customer. Inherits from User."""
    def __init__(self, id, name, email, phone, address, active=True):
        super().__init__(id, name)
        self.email = email
        self.phone = phone
        self.address = address
        self.active = active          # used for Active/Inactive customer report
        self.wishlist = []            # Advanced Feature - Wishlist (list)

    def display_role(self):
        return "Customer"

    # ---------- Advanced Feature: Wishlist ----------
    def add_to_wishlist(self, product_name):
        if product_name not in self.wishlist:
            self.wishlist.append(product_name)
            print(f"{product_name} added to wishlist.")

    def remove_from_wishlist(self, product_name):
        if product_name in self.wishlist:
            self.wishlist.remove(product_name)
            print(f"{product_name} removed from wishlist.")

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "active": self.active,
            "wishlist": self.wishlist
        }

    @staticmethod
    def from_dict(customer_id, data):
        c = Customer(
            customer_id,
            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("address"),
            data.get("active", True)
        )
        c.wishlist = data.get("wishlist", [])
        return c


class Admin(User):
    """An administrative user. Inherits from User (polymorphic role)."""
    def __init__(self, id, name):
        super().__init__(id, name)

    def display_role(self):
        return "Admin"
