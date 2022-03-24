from django.contrib import admin
from django.urls import path
from django.urls import path, include

from cookbook import views

urlpatterns = [
    path('<dish>/', views.home_page,name='home')]