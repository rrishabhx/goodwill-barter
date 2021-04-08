from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView
)
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', ProductListView.as_view(), name="products-home"),
    path('products/product/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/product/new/', ProductCreateView.as_view(), name="product-create"),
    path('services/', views.serviceshome, name="services-home"),
]
