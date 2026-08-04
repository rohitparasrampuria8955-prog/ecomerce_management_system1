"""
product_manager.py
Handles all business logic for managing products: add, view, search,
update, delete, and JSON load/save.
"""

import json
import os
from .product import Product, CATEGORIES

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")


class ProductManager:
    def __init__(self):
        self.products = {}   # {product_id: Product}
        self.load_data()

    # ---------------- File Handling ----------------
    def load_data(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    raw = json.load(f)
                    for pid_str, data in raw.items():
                        self.products[int(pid_str)] = Product.from_dict(int(pid_str), data)
        except (json.JSONDecodeError, FileNotFoundError):
            self.products = {}

    def save_data(self):
        raw = {str(pid): p.to_dict() for pid, p in self.products.items()}
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(raw, f, indent=4)
        print("Product data saved successfully.")

    # ---------------- Features ----------------
    def add_product(self, product_id, name, category, price, stock, brand, rating):
        if product_id in self.products:
            print("Error: Product ID already exists.")
            return
        if category not in CATEGORIES:
            print(f"Invalid Category. Allowed categories: {CATEGORIES}")
            return
        try:
            product = Product(product_id, name, category, price, stock, brand, rating)
            self.products[product_id] = product
            print("Product added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        print(f"{'ID':<6}{'Name':<15}{'Price':<10}{'Stock':<8}")
        print("-" * 40)
        for p in self.products.values():
            print(p)

    def search_product(self, key):
        """Search by ID, Name, Category, or Brand."""
        results = []
        if str(key).isdigit() and int(key) in self.products:
            results.append(self.products[int(key)])
        else:
            key_lower = str(key).lower()
            for p in self.products.values():
                if (key_lower in p.name.lower() or
                        key_lower in p.category.lower() or
                        key_lower in p.brand.lower()):
                    results.append(p)

        if not results:
            print(f"No product found matching '{key}'.")
        else:
            print(f"{'ID':<6}{'Name':<15}{'Price':<10}{'Stock':<8}")
            print("-" * 40)
            for p in results:
                print(p)
        return results

    def update_product(self, product_id, price=None, stock=None, rating=None):
        product = self.products.get(product_id)
        if not product:
            print(f"Product ID {product_id} not found.")
            return
        try:
            if price is not None:
                product.set_price(price)
            if stock is not None:
                if stock < 0:
                    raise ValueError("Stock cannot be negative")
                product.stock = stock
            if rating is not None:
                product.rating = rating
            print("Product updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print(f"Product ID {product_id} not found.")

    def get_product(self, product_id):
        return self.products.get(product_id)

    def reduce_stock(self, product_id, qty=1):
        product = self.products.get(product_id)
        if product and product.stock >= qty:
            product.stock -= qty
            return True
        return False
