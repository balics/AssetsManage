from django.urls import path
from assets_app import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    
]