from django.urls import path

from . import views

urlspatterns = [
    path ('', views.frontpage, name='frontpage'),
    
]