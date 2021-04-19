from django.shortcuts import render

from django.urls import path

from . import views

# Create your views here.
urlpatterns = [
    path('update-add/', views.AddToCart.as_view(), name='update-cart-add'),
    path('update-remove/', views.RemoveFromCart.as_view(), name='update-cart-remove'),
    path('cart-details/', views.ShowCartDetail.as_view(), name='cart-detail'),
]
