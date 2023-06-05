from django.urls import path
from . import views
app_name='cartapp'

urlpatterns=[
    path('add/<int:pid>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:pid>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:pid>/',views.full_remove,name='full_remove'),



]