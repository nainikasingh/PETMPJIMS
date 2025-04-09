from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forecast_expense, name="forecast"),  # ✅ Match the actual function name
]
