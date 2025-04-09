# expense_forecast/forecast.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
from .models import ExpenseHistory

def forecast_expense(user):
    qs = ExpenseHistory.objects.filter(user=user).order_by('date')
    if not qs.exists():
        return None

    data = pd.DataFrame(list(qs.values('date', 'amount')))
    data['date'] = pd.to_datetime(data['date'])
    data['timestamp'] = data['date'].map(datetime.toordinal)

    X = data[['timestamp']]
    y = data['amount']

    model = LinearRegression()
    model.fit(X, y)

    # Predict next month's expense
    next_date = data['date'].max() + pd.DateOffset(months=1)
    next_timestamp = [[next_date.toordinal()]]

    predicted_expense = model.predict(next_timestamp)[0]

    return round(predicted_expense, 2), next_date.strftime("%B %Y")
