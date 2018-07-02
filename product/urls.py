from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_products, name='list_products')
]