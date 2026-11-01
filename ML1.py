# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Load dataset
df = pd.read_csv("uber.csv")

print(df.head())

# 1. Pre-processing
df = df.drop(columns=["Unnamed: 0", "key"], errors="ignore")

df = df.dropna()

# Convert pickup_datetime into datetime
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], utc=True)

# Extract hour, day and month
df["hour"] = df["pickup_datetime"].dt.hour
df["day"] = df["pickup_datetime"].dt.day
df["month"] = df["pickup_datetime"].dt.month

df = df.drop(columns=["pickup_datetime"])

# Remove invalid values
df = df[
    (df["fare_amount"] > 0) &
    (df["fare_amount"] < 200) &
    (df["passenger_count"] > 0) &
    (df["passenger_count"] <= 6) &
    (df["pickup_longitude"].between(-75, -72)) &
    (df["dropoff_longitude"].between(-75, -72)) &
    (df["pickup_latitude"].between(40, 42)) &
    (df["dropoff_latitude"].between(40, 42))
]

print("After preprocessing:", df.shape)

# 2. Identify outliers using IQR
Q1 = df["fare_amount"].quantile(0.25)
Q3 = df["fare_amount"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["fare_amount"] < lower) |
    (df["fare_amount"] > upper)
]

print("Number of outliers:", len(outliers))

# Remove outliers
df = df[
    (df["fare_amount"] >= lower) &
    (df["fare_amount"] <= upper)
]

# 3. Check correlation
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 4. Implement regression models

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred1 = lr.predict(X_test)

# Random Forest Regression
rf = RandomForestRegressor(n_estimators=50, random_state=42)
rf.fit(X_train, y_train)

y_pred2 = rf.predict(X_test)

# 5. Evaluate models

print("\nLinear Regression Results")
print("R2 Score:", r2_score(y_test, y_pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred1)))
print("MAE:", mean_absolute_error(y_test, y_pred1))

print("\nRandom Forest Results")
print("R2 Score:", r2_score(y_test, y_pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred2)))
print("MAE:", mean_absolute_error(y_test, y_pred2))