from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
print(model.predict([[5]]))  # Output: [10.]
