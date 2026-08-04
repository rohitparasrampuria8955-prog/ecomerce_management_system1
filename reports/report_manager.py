"""
report_manager.py
STEP 7 - Generates Product, Customer, and Sales reports.
"""


class ReportManager:
    def __init__(self, product_manager, customer_manager, order_manager):
        self.product_manager = product_manager
        self.customer_manager = customer_manager
        self.order_manager = order_manager

    # ---------------- Product Report ----------------
    def product_report(self):
        products = list(self.product_manager.products.values())
        print("\n--- Product Report ---")
        print(f"Total Products: {len(products)}")

        if not products:
            return

        most_expensive = max(products, key=lambda p: p.get_price())
        cheapest = min(products, key=lambda p: p.get_price())
        out_of_stock = [p for p in products if p.stock == 0]

        print(f"Most Expensive Product: {most_expensive.name} ({most_expensive.get_price()})")
        print(f"Cheapest Product: {cheapest.name} ({cheapest.get_price()})")
        print(f"Out Of Stock Products: {len(out_of_stock)}")
        for p in out_of_stock:
            print(f"   - {p.name}")

    # ---------------- Customer Report ----------------
    def customer_report(self):
        customers = list(self.customer_manager.customers.values())
        print("\n--- Customer Report ---")
        print(f"Total Customers: {len(customers)}")

        active = [c for c in customers if c.active]
        inactive = [c for c in customers if not c.active]
        print(f"Active Customers: {len(active)}")
        print(f"Inactive Customers: {len(inactive)}")

    # ---------------- Sales Report ----------------
    def sales_report(self):
        orders = [o for o in self.order_manager.orders.values() if o.payment_status != "Cancelled"]
        print("\n--- Sales Report ---")
        print(f"Total Orders: {len(orders)}")

        if not orders:
            print("Total Revenue: 0")
            return

        try:
            total_revenue = sum(o.total_amount for o in orders)
            average_order_value = total_revenue / len(orders)
            highest_order_value = max(o.total_amount for o in orders)

            print(f"Total Revenue: {total_revenue:.2f}")
            print(f"Average Order Value: {average_order_value:.2f}")
            print(f"Highest Order Value: {highest_order_value:.2f}")
        except ZeroDivisionError:
            print("Not enough data to calculate averages.")
