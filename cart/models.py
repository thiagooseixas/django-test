# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from product.models import Product


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def create_item_order(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product.name


class Payment(models.Model):
    #order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    number_card = models.CharField(max_length=12)
    expiration = models.CharField(max_length=5)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.order
