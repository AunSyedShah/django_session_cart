from django.conf import settings


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(
            settings.CART_SESSION_ID
        )  # if cart exists return, otherwise None
        if (
            not self.cart
        ):  # if cart is not already initialized, initialize it with empty dicts
            self.cart = self.session[settings.CART_SESSION_ID] = {}
            self.save()

    def save(self):
        self.session.modified = True

    def add_product(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:  # if product is not already in cart, add it
            self.cart[product_id] = {"quantity": 1, "price": str(product.price)}
            self.save()
            return {
                "message": f"product with id {product_id} added initially",
                "quantity": self.cart[product_id]["quantity"],
            }
        else:
            self.cart[product_id]["quantity"] += 1
            self.save()
            return {
                "message": f"product with id {product_id} increment by 1",
                "quantity": f"{self.cart[product_id]['quantity']}",
            }
