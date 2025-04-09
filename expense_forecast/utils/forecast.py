# expenses/utils/forecast.py

from expenses.models import Expense
from datetime import timedelta
from django.utils import timezone
from collections import defaultdict

def generate_forecast(user):
    today = timezone.now().date()
    past_30_days = today - timedelta(days=30)

    recent_expenses = Expense.objects.filter(owner=user, date__gte=past_30_days)

    total_spent = sum(exp.amount for exp in recent_expenses)
    avg_daily_spend = total_spent / 30 if total_spent else 0
    forecast = avg_daily_spend * 30

    category_totals = defaultdict(float)
    for exp in recent_expenses:
        category_totals[exp.category] += exp.amount

    return {
        'total_spent': total_spent,
        'avg_daily_spend': avg_daily_spend,
        'forecast': forecast,
        'category_totals': dict(category_totals),
        'today': today
    }
