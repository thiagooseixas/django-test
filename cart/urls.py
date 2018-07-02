from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/(?P<item_id>[-\w]+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^cart/list$', views.view_cart, name='view_cart'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', views.delete_item, name='delete_item'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkout/status/$', views.payment, name='payment')
]
