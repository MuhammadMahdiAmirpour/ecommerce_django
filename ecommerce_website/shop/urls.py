from django.contrib import admin
from django.urls import path
from .views import index
from .views import detail

urlpatterns = [
        path('index/', index, name='index'),
        path('detail/<int:id>', detail, name='detail'),
]
