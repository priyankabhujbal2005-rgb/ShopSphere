from django.shortcuts import render, get_object_or_404
from .models import Product, CartItem


def home(request):
    products = Product.objects.filter(is_available=True)

    context = {
        "products": products
    }

    return render(request, "home.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }

    return render(request, "product_detail.html", context)


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart_item, created = CartItem.objects.get_or_create(
        session_key=session_key,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, "cart.html", {
        "message": f"{product.name} added to your cart."
    })

def cart(request):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart_items = CartItem.objects.filter(
        session_key=session_key
    )

    return render(request, "cart.html", {
        "cart_items": cart_items
    })

def remove_from_cart(request, slug):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart_item = get_object_or_404(
        CartItem,
        session_key=session_key,
        product__slug=slug
    )

    cart_item.delete()

    return render(request, "cart.html", {
        "message": "Item removed from your cart."
    })

def update_cart(request, slug):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key

    cart_item = get_object_or_404(
        CartItem,
        session_key=session_key,
        product__slug=slug
    )

    quantity = int(request.GET.get("quantity", 1))

    if quantity <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    cart_items = CartItem.objects.filter(
        session_key=session_key
    )

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "message": "Cart updated successfully."
    })