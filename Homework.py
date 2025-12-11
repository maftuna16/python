from datetime import datetime



#PRODUCT

class Product:
    def init(self, id, name, price, quantity, rating):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating

    def update_price(self, new_price):
        self.price = new_price

    def show_info(self):
        print(f"ID: {self.id}, Nomi: {self.name}, Narxi: {self.price}, "
              f"Soni: {self.quantity}, Reyting: {self.rating}")



#CART

class Cart:
    def init(self):
        self.products = []  # (product, amount)
        self.total_price = 0

    def add_product(self, product, amount=1):
        if product.quantity < amount:
            raise ValueError("Omborda yetarli mahsulot yo'q!")

        self.products.append((product, amount))
        product.quantity -= amount
        self.calculate_total()

    def remove_product(self, product_id):
        found = False
        for item in self.products:
            if item[0].id == product_id:
                # mahsulotni omborga qaytarish
                item[0].quantity += item[1]
                self.products.remove(item)
                found = True
                break
        if not found:
            print("Bu mahsulot savatda yo‘q.")
        self.calculate_total()

    def clear_cart(self):
        for product, amount in self.products:
            product.quantity += amount
        self.products = []
        self.total_price = 0

    def calculate_total(self):
        self.total_price = sum(p.price * a for p, a in self.products)

    def is_empty(self):
        return len(self.products) == 0



#ORDER

class Order:
    def init(self, order_id, cart):
        if cart.is_empty():
            raise ValueError("Bo'sh savat bilan buyurtma yaratilmaydi.")

        self.id = order_id
        self.status = "Yaratildi"
        self.cart = cart
        self.created_at = datetime.now()
        self.total_price = cart.total_price

    def confirm_order(self):
        self.status = "Tasdiqlandi"

    def update_status(self, new_status):
        self.status = new_status

    def show_info(self):
        print(f"Buyurtma ID: {self.id}, Status: {self.status}, "
              f"Vaqti: {self.created_at}, Jami: {self.total_price}")



#CUSTOMER

class Customer:
    def init(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.cart = Cart()
        self.orders = []

    def add_to_cart(self, product, amount=1):
        try:
            self.cart.add_product(product, amount)
        except ValueError as e:
            print("Xato:", e)

    def remove_from_cart(self, product_id):
        self.cart.remove_product(product_id)

    def create_order(self, order_id):
        try:
            new_order = Order(order_id, self.cart)
            new_order.confirm_order()
            self.orders.append(new_order)
            self.cart = Cart()  # yangi bo'sh savat
        except ValueError as e:
            print("Xato:", e)

    def show_order_history(self):
        if not self.orders:
            print("Buyurtmalar tarixi bo'sh.")
        for order in self.orders:
            order.show_info()



# STORE

class Store:
    def init(self, name):
        self.name = name
        self.products = []
        self.customers = []
        self.sold_products = []

    def add_product(self, product):
        self.products.append(product)

    def register_customer(self, customer):
        self.customers.append(customer)

    def search_product(self, name):
        result = [p for p in self.products if name.lower() in p.name.lower()]
        return result

        def top_rated(self):
            sorted_products = sorted(self.products, key=lambda x: x.rating, reverse=True)
            return sorted_products[:5]

        def add_sold_record(self, product, amount):
            self.sold_products.append((product.name, amount))

        def sold_report(self):
            print("\n--- Sotilgan mahsulotlar hisobot ---")
            if not self.sold_products:
                print("Hali sotuv bo‘lmagan.")
            for name, amount in self.sold_products:
                print(f"{name} — {amount} dona")



#MISOL SIFATIDA ISHLATISH


    if name == "main":
        store = Store("Online Market")

        p1 = Product(1, "Olma", 5000, 50, 4.8)
        p2 = Product(2, "Banana", 8000, 30, 4.5)
        store.add_product(p1)
        store.add_product(p2)

        user = Customer(1, "Maftuna", "maftuna@example.com")
        store.register_customer(user)

        user.add_to_cart(p1, 3)
        user.add_to_cart(p2, 2)

        user.create_order(101)

        user.show_order_history()