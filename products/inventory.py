"""
inventory.py
Advanced Feature: Inventory Alerts (Low Stock Warning) and Top Selling Products.
"""

LOW_STOCK_THRESHOLD = 5


def check_low_stock(product_manager):
    """Display Low Stock Warning for products with stock < 5."""
    low_stock_items = [p for p in product_manager.products.values() if p.stock < LOW_STOCK_THRESHOLD]
    if not low_stock_items:
        print("All products have sufficient stock.")
        return
    print("\n*** Low Stock Warning ***")
    for p in low_stock_items:
        print(f"{p.name} - Only {p.stock} left in stock!")


def top_selling_products(order_manager, product_manager, top_n=5):
    """Generate a report of top selling products based on order history."""
    sales_count = {}
    for order in order_manager.orders.values():
        for pname in order.products:
            sales_count[pname] = sales_count.get(pname, 0) + 1

    if not sales_count:
        print("No sales data available yet.")
        return

    sorted_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
    print("\n*** Top Selling Products ***")
    for name, count in sorted_sales[:top_n]:
        print(f"{name} - {count} unit(s) sold")
