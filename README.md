#  E-Commerce Management System

ShopSphere is a console-based E-Commerce Management System developed using **Python**. This project was created to practice Object-Oriented Programming (OOP), modules, packages, file handling, and real-world business logic.

The application allows users to manage products, customers, shopping carts, orders, payments, notifications, and reports from a single menu-driven interface. All data is stored in JSON files, so there is no need for any external database.

---

# Features

### Product Management
- Add new products
- View all products
- Search products by ID, name, category, or brand
- Update product details
- Delete products
- Low stock alerts

---

### Customer Management
- Add customers
- View customer details
- Search customers
- Update customer information
- Delete customers

---

### Shopping Cart
- Add products to cart
- Remove products from cart
- View cart items
- Calculate total amount
- Apply discount coupons

Supported Coupons:
- SAVE10
- SAVE20
- NEWUSER50

---

### Order Management
- Place new orders
- Cancel orders
- View all orders
- Automatic total calculation
- Coupon support

---

### Payment System

Implemented using **Polymorphism**.

Supported payment methods:
- UPI Payment
- Card Payment
- Cash Payment

Users can choose any payment method during checkout.

---

### Notification System

After every successful order, the system automatically sends:

- Email Notification
- SMS Notification
- WhatsApp Notification

---

### Reports

Generate useful business reports such as:

- Total Products
- Most Expensive Product
- Cheapest Product
- Out of Stock Products
- Total Customers
- Active Customers
- Total Orders
- Total Revenue
- Average Order Value
- Highest Order Value
- Top Selling Products

---

### JSON Data Storage

The project stores data locally using JSON files.

- products.json
- customers.json
- orders.json

Whenever data is added, updated, or deleted, it is automatically saved.

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON File Handling
- Modules & Packages
- Exception Handling

---

# Project Structure

```
ecommerce_system/
│
├── main.py
│
├── products/
│   ├── product.py
│   ├── product_manager.py
│   └── inventory.py
│
├── customers/
│   ├── customer.py
│   └── customer_manager.py
│
├── orders/
│   ├── order.py
│   └── order_manager.py
│
├── payments/
│   ├── payment.py
│   ├── upi.py
│   ├── card.py
│   └── cash.py
│
├── notifications/
│   ├── email.py
│   ├── sms.py
│   └── whatsapp.py
│
├── reports/
│   └── report_manager.py
│
└── data/
    ├── products.json
    ├── customers.json
    └── orders.json

# Project Workflow

1. Add products to the inventory.
2. Register customers.
3. Add products to the shopping cart.
4. Apply a coupon if available.
5. Choose a payment method.
6. Complete the payment.
7. Receive confirmation notifications.
8. View reports and sales information.

---

# Learning Objectives

This project helped me understand:

- Python OOP Concepts
- Classes & Objects
- Inheritance
- Polymorphism
- Encapsulation
- Modules
- Packages
- File Handling with JSON
- Exception Handling
- Dictionary, List & Tuple Usage
- Building a real-world console application

---

# Future Improvements

Some features that can be added in the future:

- Login & Authentication
- Admin Dashboard
- Database Integration (MySQL)
- Barcode Support
- Product Images
- Invoice Generation (PDF)
- Email API Integration
- Online Payment Gateway
- GUI using Tkinter or PyQt
- Web Version using Django or Flask

