
from django.contrib import admin
from django.urls import path
from .views import biu, saudacao, id_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biu/', biu ),
    path('id_produto/<str:id>/', id_produto),
    path('saudacao/<str:name>/', saudacao)
]
