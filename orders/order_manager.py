
import json
import os
from datetime import date
from .order import Order

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "orders.json")


COUPONS = {
    "SAVE10": 10,
    "SAVE20": 20,
    "NEWUSER50": 50
}


class OrderManager:
    def __init__(self, product_manager):
        self.product_manager = product_manager
        self.cart = []          # STEP 3 - Shopping Cart implemented using a LIST
        self.orders = {}        # {order_id: Order}
        self.next_order_id = 1001
        self.load_data()
        if self.orders:
            self.next_order_id = max(self.orders.keys()) + 1

    # ---------------- Shopping Cart (List) ----------------
    def add_to_cart(self, product_id):
        product = self.product_manager.get_product(product_id)
        if not product:
            print(f"Product ID {product_id} not found.")
            return
        if product.stock <= 0:
            print(f"{product.name} is out of stock.")
            return
        self.cart.append(product)
        print(f"{product.name} added to cart.")

    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item.product_id == product_id:
                self.cart.remove(item)
                print(f"{item.name} removed from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("Your Cart:")
        for item in self.cart:
            print(f" - {item.name} ({item.get_price()})")

    def calculate_total(self, coupon_code=None):
        total = sum(item.get_price() for item in self.cart)
        if coupon_code:
            discount_pct = COUPONS.get(coupon_code.upper())
            if discount_pct:
                discount = total * discount_pct / 100
                total -= discount
                print(f"Coupon '{coupon_code.upper()}' applied: -{discount_pct}% ({discount:.2f} off)")
            else:
                print("Invalid coupon code. No discount applied.")
        return round(total, 2)

    def clear_cart(self):
        self.cart = []

    # ---------------- Order Processing ----------------
    def place_order(self, customer_id, payment_method, coupon_code=None):
        if not self.cart:
            print("Cart is empty. Add products before placing an order.")
            return None

        total = self.calculate_total(coupon_code)
        product_names = [item.name for item in self.cart]

        # reduce stock for each purchased item
        for item in self.cart:
            self.product_manager.reduce_stock(item.product_id, 1)

        order = Order(
            self.next_order_id,
            customer_id,
            product_names,
            total,
            str(date.today()),
            "Paid" if payment_method else "Pending"
        )
        self.orders[order.order_id] = order
        self.next_order_id += 1
        self.clear_cart()
        print(f"Order #{order.order_id} placed successfully. Total: {total}")
        return order

    def cancel_order(self, order_id):
        order = self.orders.get(order_id)
        if not order:
            print(f"Order ID {order_id} not found.")
            return
        order.payment_status = "Cancelled"
        print(f"Order #{order_id} has been cancelled.")

    def view_orders(self, customer_manager=None):
        if not self.orders:
            print("No orders placed yet.")
            return
        print(f"{'OrderID':<10}{'Customer':<15}{'Products':<30}{'Amount':<10}{'Status':<10}")
        print("-" * 80)
        for order in self.orders.values():
            cust_name = order.customer_id
            if customer_manager:
                c = customer_manager.get_customer(order.customer_id)
                cust_name = c.name if c else order.customer_id
            print(f"{order.order_id:<10}{str(cust_name):<15}{', '.join(order.products):<30}"
                  f"{order.total_amount:<10}{order.payment_status:<10}")

    # ---------------- File Handling ----------------
    def load_data(self):
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    raw = json.load(f)
                    for oid_str, data in raw.items():
                        self.orders[int(oid_str)] = Order.from_dict(int(oid_str), data)
        except (json.JSONDecodeError, FileNotFoundError):
            self.orders = {}

    def save_data(self):
        raw = {str(oid): o.to_dict() for oid, o in self.orders.items()}
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump(raw, f, indent=4)
        print("Order data saved successfully.")
