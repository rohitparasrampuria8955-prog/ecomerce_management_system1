"""
main.py
E-Commerce Management System - ShopSphere
Console-based application tying together all packages/modules.

Run with:  python main.py
"""

from products.product_manager import ProductManager
from products import inventory
from customers.customer_manager import CustomerManager
from orders.order_manager import OrderManager
from reports.report_manager import ReportManager

from payments.upi import UPIPayment
from payments.card import CardPayment
from payments.cash import CashPayment

from notifications.email import send_email
from notifications.sms import send_sms
from notifications.whatsapp import send_whatsapp


# ---------------------------------------------------------------------------
# Helper functions for safe input handling (STEP 11 - Exception Handling)
# ---------------------------------------------------------------------------
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# ---------------------------------------------------------------------------
# Product Management Menu
# ---------------------------------------------------------------------------
def product_menu(pm):
    while True:
        print("""
--- Product Management ---
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            pid = get_int("Product ID: ")
            name = input("Name: ")
            category = input("Category (Electronics/Fashion/Books/Furniture/Sports/Accessories): ")
            price = get_float("Price: ")
            stock = get_int("Stock: ")
            brand = input("Brand: ")
            rating = get_float("Rating: ")
            pm.add_product(pid, name, category, price, stock, brand, rating)

        elif choice == 2:
            pm.view_products()

        elif choice == 3:
            key = input("Search by ID / Name / Category / Brand: ")
            pm.search_product(key)

        elif choice == 4:
            pid = get_int("Product ID to update: ")
            print("Leave blank to skip a field.")
            price_str = input("New Price: ")
            stock_str = input("New Stock: ")
            rating_str = input("New Rating: ")
            price = float(price_str) if price_str else None
            stock = int(stock_str) if stock_str else None
            rating = float(rating_str) if rating_str else None
            pm.update_product(pid, price, stock, rating)

        elif choice == 5:
            pid = get_int("Product ID to delete: ")
            pm.delete_product(pid)

        elif choice == 6:
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Customer Management Menu
# ---------------------------------------------------------------------------
def customer_menu(cm):
    while True:
        print("""
--- Customer Management ---
1. Add Customer
2. View Customers
3. Search Customer
4. Update Customer
5. Delete Customer
6. Back to Main Menu
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            cid = get_int("Customer ID: ")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            cm.add_customer(cid, name, email, phone, address)

        elif choice == 2:
            cm.view_customers()

        elif choice == 3:
            key = input("Search by ID / Name / Phone: ")
            cm.search_customer(key)

        elif choice == 4:
            cid = get_int("Customer ID to update: ")
            print("Leave blank to skip a field.")
            name = input("New Name: ") or None
            email = input("New Email: ") or None
            phone = input("New Phone: ") or None
            address = input("New Address: ") or None
            cm.update_customer(cid, name, email, phone, address)

        elif choice == 5:
            cid = get_int("Customer ID to delete: ")
            cm.delete_customer(cid)

        elif choice == 6:
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Shopping Cart Menu
# ---------------------------------------------------------------------------
def cart_menu(om):
    while True:
        print("""
--- Shopping Cart ---
1. Add Product To Cart
2. Remove Product From Cart
3. View Cart
4. Calculate Total
5. Back to Main Menu
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            pid = get_int("Product ID to add: ")
            om.add_to_cart(pid)
        elif choice == 2:
            pid = get_int("Product ID to remove: ")
            om.remove_from_cart(pid)
        elif choice == 3:
            om.view_cart()
        elif choice == 4:
            coupon = input("Coupon code (leave blank if none): ") or None
            total = om.calculate_total(coupon)
            print(f"Total Amount: {total}")
        elif choice == 5:
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Order Management Menu
# ---------------------------------------------------------------------------
def order_menu(om, cm):
    while True:
        print("""
--- Order Management ---
1. Place Order
2. Cancel Order
3. View Orders
4. Back to Main Menu
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            cid = get_int("Customer ID: ")
            if not cm.get_customer(cid):
                print(f"Customer ID {cid} not found.")
                continue
            if not om.cart:
                print("Your cart is empty. Add products first (Shopping Cart menu).")
                continue

            coupon = input("Coupon code (leave blank if none): ") or None

            print("Select Payment Method: 1. UPI  2. Card  3. Cash")
            pchoice = get_int("Enter choice: ")
            amount = om.calculate_total(coupon)

            payment_map = {1: UPIPayment, 2: CardPayment, 3: CashPayment}
            payment_cls = payment_map.get(pchoice)
            if not payment_cls:
                print("Invalid payment method.")
                continue

            payment = payment_cls(amount)   # STEP 5 - Polymorphism: same pay() call, different behaviour
            success = payment.pay()

            order = om.place_order(cid, success, coupon)
            if order:
                customer = cm.get_customer(cid)
                send_email(customer.email if customer else None,
                           f"Order #{order.order_id} confirmed.")
                send_sms(customer.phone if customer else None,
                         f"Order #{order.order_id} confirmed.")
                send_whatsapp(customer.phone if customer else None,
                              f"Order #{order.order_id} confirmed.")

        elif choice == 2:
            oid = get_int("Order ID to cancel: ")
            om.cancel_order(oid)

        elif choice == 3:
            om.view_orders(cm)

        elif choice == 4:
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Reports Menu
# ---------------------------------------------------------------------------
def reports_menu(rm, om, pm):
    while True:
        print("""
--- Reports ---
1. Product Report
2. Customer Report
3. Sales Report
4. Low Stock Warning
5. Top Selling Products
6. Back to Main Menu
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            rm.product_report()
        elif choice == 2:
            rm.customer_report()
        elif choice == 3:
            rm.sales_report()
        elif choice == 4:
            inventory.check_low_stock(pm)
        elif choice == 5:
            inventory.top_selling_products(om, pm)
        elif choice == 6:
            break
        else:
            print("Invalid choice.")


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------
def main():
    product_manager = ProductManager()
    customer_manager = CustomerManager()
    order_manager = OrderManager(product_manager)
    report_manager = ReportManager(product_manager, customer_manager, order_manager)

    while True:
        print("""
================================
      E-COMMERCE SYSTEM
================================
1. Product Management
2. Customer Management
3. Shopping Cart
4. Order Management
5. Payment System (via Order Management)
6. Notifications (automatic on order)
7. Reports
8. Save Data
9. Exit
""")
        choice = get_int("Enter choice: ")

        if choice == 1:
            product_menu(product_manager)
        elif choice == 2:
            customer_menu(customer_manager)
        elif choice == 3:
            cart_menu(order_manager)
        elif choice == 4:
            order_menu(order_manager, customer_manager)
        elif choice == 5:
            print("Payments are processed automatically during 'Place Order'.")
        elif choice == 6:
            print("Notifications are sent automatically once an order is placed.")
        elif choice == 7:
            reports_menu(report_manager, order_manager, product_manager)
        elif choice == 8:
            product_manager.save_data()
            customer_manager.save_data()
            order_manager.save_data()
        elif choice == 9:
            print("Saving data before exit...")
            product_manager.save_data()
            customer_manager.save_data()
            order_manager.save_data()
            print("Thank you for using ShopSphere E-Commerce System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-9).")


if __name__ == "__main__":
    main()
