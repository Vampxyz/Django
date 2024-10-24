from django.contrib import admin
from django.urls import path
from .views import greetings, products, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<str:name>/', greetings),
    path('products/', products),
    path('product/<str:id>/', product),
]
