"""
customer_manager.py
Handles all business logic for managing customers.
"""

import json
import os
from .customer import Customer

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "customers.json")


class CustomerManager:
    def __init__(self):
        self.customers = {}   # {customer_id: Customer}
        self.load_data()

    # ---------------- File Handling ----------------
    def load_data(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    raw = json.load(f)
                    for cid_str, data in raw.items():
                        self.customers[int(cid_str)] = Customer.from_dict(int(cid_str), data)
        except (json.JSONDecodeError, FileNotFoundError):
            self.customers = {}

    def save_data(self):
        raw = {str(cid): c.to_dict() for cid, c in self.customers.items()}
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(raw, f, indent=4)
        print("Customer data saved successfully.")

    # ---------------- Features ----------------
    def add_customer(self, customer_id, name, email, phone, address):
        if customer_id in self.customers:
            print("Error: Customer ID already exists.")
            return
        self.customers[customer_id] = Customer(customer_id, name, email, phone, address)
        print("Customer added successfully.")

    def view_customers(self):
        if not self.customers:
            print("No customers available.")
            return
        print(f"{'ID':<6}{'Name':<15}{'Phone':<15}{'Email':<25}")
        print("-" * 60)
        for c in self.customers.values():
            print(f"{c.id:<6}{c.name:<15}{c.phone:<15}{c.email:<25}")

    def search_customer(self, key):
        results = []
        if str(key).isdigit() and int(key) in self.customers:
            results.append(self.customers[int(key)])
        else:
            key_lower = str(key).lower()
            for c in self.customers.values():
                if key_lower in c.name.lower() or key_lower in c.phone:
                    results.append(c)

        if not results:
            print(f"No customer found matching '{key}'.")
        else:
            for c in results:
                print(c)
        return results

    def update_customer(self, customer_id, name=None, email=None, phone=None, address=None):
        customer = self.customers.get(customer_id)
        if not customer:
            print(f"Customer ID {customer_id} not found.")
            return
        if name:
            customer.name = name
        if email:
            customer.email = email
        if phone:
            customer.phone = phone
        if address:
            customer.address = address
        print("Customer updated successfully.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print("Customer deleted successfully.")
        else:
            print(f"Customer ID {customer_id} not found.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)
