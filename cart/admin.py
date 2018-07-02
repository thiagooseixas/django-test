# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import OrderItem, Transaction, Payment

admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(Payment)
