from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('add-product', views.AddProductInSystem.as_view(), name='add-product'),
]
