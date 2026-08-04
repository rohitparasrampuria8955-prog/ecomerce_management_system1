"""
product.py
Defines the Product class.
Demonstrates: OOP, Encapsulation (private __price attribute with getter/setter)
"""

# STEP 8 - Tuple of allowed categories
CATEGORIES = (
    "Electronics",
    "Fashion",
    "Books",
    "Furniture",
    "Sports",
    "Accessories"
)


class Product:
    """Represents a single product in the store."""

    def __init__(self, product_id, name, category, price, stock, brand, rating=0.0):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.__price = 0          # STEP 9 - private/encapsulated attribute
        self.set_price(price)     # goes through validation
        self.stock = stock
        self.brand = brand
        self.rating = rating
        self.reviews = []         # Advanced Feature - list of ratings given by customers

    # ---------- Encapsulation: getter / setter for price ----------
    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price is None or price <= 0:
            raise ValueError("Price must be a positive number")
        self.__price = price

    # ---------- Advanced Feature: Product Reviews ----------
    def add_review(self, rating_value):
        if 1 <= rating_value <= 5:
            self.reviews.append(rating_value)
            self.rating = round(sum(self.reviews) / len(self.reviews), 2)
        else:
            raise ValueError("Rating must be between 1 and 5")

    # ---------- Conversion helpers for JSON file storage ----------
    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "price": self.__price,
            "stock": self.stock,
            "brand": self.brand,
            "rating": self.rating,
            "reviews": self.reviews
        }

    @staticmethod
    def from_dict(product_id, data):
        p = Product(
            product_id,
            data.get("name"),
            data.get("category"),
            data.get("price", 1),
            data.get("stock", 0),
            data.get("brand", "Unknown"),
            data.get("rating", 0.0)
        )
        p.reviews = data.get("reviews", [])
        return p

    def __str__(self):
        return f"{self.product_id:<6}{self.name:<15}{self.get_price():<10}{self.stock:<8}"
