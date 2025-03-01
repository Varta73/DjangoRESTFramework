from config.settings import STRIPE_API_KEY
import stripe


stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создание продукта"""

    product = stripe.Product.create(name=product.title)
    return product


def create_stripe_price(amount):
    """Создание цены"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product_data={"name": "Payment"},
    )
    return price


def create_stripe_link(price):
    """Создание сессии на оплату"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def status_payment(id_session):
    """Статус оплаты"""
    payment_status = stripe.checkout.Session.retrieve(
        id_session,
    )
    return payment_status["payment_status"]
