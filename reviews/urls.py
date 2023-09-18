from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.welcome_view, name='welcome_index'),
    path('books/', views.books_list, name='books_list'),
]