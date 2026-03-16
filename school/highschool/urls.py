from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('academics/', views.index, name = 'academics'),

    ]