from django.contrib import admin
from django.urls import path
from .views import greetings, personal_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/hello', greetings),
    path('/datas', personal_data)
]
