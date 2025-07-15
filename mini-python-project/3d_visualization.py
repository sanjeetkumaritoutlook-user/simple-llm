import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Load data
df = pd.read_csv('data_extended.csv')
print("Data preview:")
print(df.head())

# Step 2: Prepare data
X = df[['study_hours', 'sleep_hours', 'internet_usage']].values
y = df['score'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict for custom input
custom_input = np.array([[6.5, 6, 2]])
predicted_score = model.predict(custom_input)
print(f"\nPredicted score for study=6.5h, sleep=6h, internet=2h: {predicted_score[0]:.2f}")

# Step 5: Plot in 3D (study_hours, sleep_hours vs score)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Get data
x_vals = df['study_hours']
y_vals = df['sleep_hours']
z_vals = df['score']

# Plot actual data points
ax.scatter(x_vals, y_vals, z_vals, c='green', label='Actual Data')

# Plot predicted point
ax.scatter(6.5, 6, predicted_score[0], color='red', s=100, label='Predicted Point')

# Labels and view
ax.set_xlabel('Study Hours')
ax.set_ylabel('Sleep Hours')
ax.set_zlabel('Score')
ax.set_title('3D Score Prediction Visualization')
ax.view_init(elev=20, azim=135)  # Adjust the angle for better view
ax.legend()
plt.tight_layout()
plt.show()
