import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Sample synthetic data for demonstration
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
sales = np.random.poisson(lam=200, size=100) + np.sin(np.linspace(0, 3.14, 100)) * 20
data = pd.DataFrame({"Date": dates, "Sales": sales})
data.set_index("Date", inplace=True)

# Train-Test Split
train_size = int(len(data) * 0.8)
train_data = data.iloc[:train_size]
test_data = data.iloc[train_size:]

# Fit ARIMA Model
model = ARIMA(train_data, order=(2, 1, 2))
fitted_model = model.fit()

# Forecast
forecast = fitted_model.forecast(steps=len(test_data))

# Evaluate
mse = mean_squared_error(test_data, forecast)
mae = mean_absolute_error(test_data, forecast)

# Save output to a file
output = pd.DataFrame({"Actual": test_data["Sales"], "Forecast": forecast})
output.to_csv("forecast_output.csv")

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
