import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Load the data
df = pd.read_csv('data.csv')
print("Data preview:")
print(df.head())

# Step 2: Prepare features and labels
X = df[['hours']].values  # 2D array
y = df['score'].values    # 1D array

# Step 3: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict
y_pred = model.predict(X_test)

# Step 6: Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

# Step 7: Predict for new input
new_hours = np.array([[6.5]])
predicted_score = model.predict(new_hours)
print(f"\nPredicted score for 6.5 study hours: {predicted_score[0]:.2f}")

# Step 8: Plot
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours vs Score Prediction')
plt.legend()
plt.grid(True)
plt.show()
