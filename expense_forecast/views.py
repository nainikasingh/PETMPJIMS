from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils.forecast import generate_forecast  # 👈 import the modular function

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def forecast_expense(request):
    forecast_data = generate_forecast(request.user)
    return render(request, 'expense_forecast/index.html', forecast_data)
