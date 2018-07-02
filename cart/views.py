# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from cart.models import OrderItem
from django.utils import timezone
from .forms import PostForm


def add_to_cart(request, **kwargs):
    product = Product.objects.get(id=kwargs.get('item_id', ''))
    status = OrderItem.objects.get_or_create(product=product)

    if status:
        messages.info(request, "Item " + product.name + " added to Cart.")
        return redirect(reverse('product:list_products'))
    else:
        messages.error(request, "Error to add in the Cart.")
        return redirect(reverse('product:list_products'))


def view_cart(request):
    orders = OrderItem.objects.all()
    products = []

    if orders is not None:
        for order in orders:
            product = Product.objects.get(name=order)
            products.append(product)
        return render(request, 'cart/cart.html', {'products': products})


def delete_item(request, **kwargs):
    item = Product.objects.get(id=kwargs.get('item_id', ''))

    if item:
        item.delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('cart:view_cart'))


def checkout(request):
    form = PostForm(request.POST)
    if form.is_valid():
        OrderItem.objects.all().delete()
        form.save()
        #messages.success(request, "Save Success.")
        return render(request, 'payment/info.html', {})
    return render(request, 'checkout/checkout.html', {})


def payment(request):
    return render(request, 'payment/info.html', {})
