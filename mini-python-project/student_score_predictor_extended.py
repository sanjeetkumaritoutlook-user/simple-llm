import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Load the extended dataset
df = pd.read_csv('data_extended.csv')
print("Data preview:")
print(df.head())

# Step 2: Prepare features (X) and label (y)
X = df[['study_hours', 'sleep_hours', 'internet_usage']].values
y = df['score'].values

# Step 3: Split into training/testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

# Step 6: Predict for a new student
# Example: 6.5 study hours, 6 hours of sleep, 2 hours internet usage
new_data = np.array([[6.5, 6, 2]])
predicted_score = model.predict(new_data)
print(f"\nPredicted score for study=6.5h, sleep=6h, internet=2h: {predicted_score[0]:.2f}")

# Step 7: Plotting study_hours vs score (as 3D would need more setup)
plt.scatter(df['study_hours'], df['score'], color='green', label='Actual Scores')
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Study Hours vs Score (Multiple Feature Model)')
plt.grid(True)
plt.legend()
plt.show()
