# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Product


def list_products(request):
    #products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    products = Product.objects.all()
    return render(request, 'list/list.html', {'products': products})
