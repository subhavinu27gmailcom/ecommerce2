from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem
from shopapp.models import Product


# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    print("12cart",cart)
    return cart
def add_cart(request,product_id):

    product=Product.objects.get(id=product_id)
    print("17product",product,"17product_id",product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        print("20cart",cart)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request))
        print("24cart", cart)
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            print(" 27cart_item.product.stock is",  cart_item.product.stock)
            cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        print("36cart_item",type(cart_item),cart_item)
        cart_item.save()
    print("38product", product, "38product_id", product_id)
    return redirect('cart:cart_detail')
def cart_detail(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,active=True)
        print("44cart_items",cart_items,_cart_id(request))
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))
def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(cart=cart,product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart:cart_detail')
