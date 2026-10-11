from django.urls import path
from .views import home, product_detail, add_to_cart, cart, remove_from_cart, update_cart


urlpatterns = [
    path("", home, name="home"),
    path("product/<slug:slug>/", product_detail, name="product_detail"),
    path("cart/add/<slug:slug>/", add_to_cart, name="add_to_cart"),
    path("cart/", cart, name="cart"),
    path("cart/remove/<slug:slug>/", remove_from_cart, name="remove_from_cart"),
    path("cart/update/<slug:slug>/", update_cart, name="update_cart"),
]