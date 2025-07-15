## mini project 
that uses all three libraries — NumPy, Pandas, and Scikit-learn — to predict students' scores based on their study hours.

## Goal:
You have a dataset of students with hours studied and corresponding scores.

You’ll build a machine learning model using scikit-learn to predict scores based on hours studied.

## step by step
pip install numpy pandas scikit-learn matplotlib

## Output:
Console will print:

Data preview

Mean Squared Error

Predicted score for a new input

A graph will open showing the regression line and data points.

NumPy  ->	Creating arrays (e.g., np.array([[6.5]]))

Pandas	->  Reading CSV, exploring data

Scikit-learn	-> Splitting data, training model, making predictions

Matplotlib ->	Plotting the regression result

## extended version 
with more features like study_hours, sleep_hours, internet_usage to predict performance

Output

You’ll see:

Console preview of the dataset

Mean Squared Error

Predicted score for a custom input like:

study_hours=6.5, sleep_hours=6, internet_usage=2 → Predicted score: ~72

A plot showing correlation between study_hours and actual score


## Next Steps (Optional):
Plot in 3D using mpl_toolkits.mplot3d

Add GUI using Tkinter or Streamlit

Save/load model using joblib

Try decision tree or random forest (non-linear models)

## Would you like: 

3D visualization?  -> pip install matplotlib

Export predictions to a CSV?

Real-time input from user and prediction?

## 3D visualization  🎯 using mpl_toolkits.mplot3d.
What You'll See:

A 3D scatter plot with green dots for real data

A red dot for the predicted score (e.g. 6.5h study, 6h sleep)

X, Y, Z axes labeled properly

We'll plot:

X-axis: study_hours

Y-axis: sleep_hours

Z-axis: score

## Want to go further?
We can add:

A 3D surface plot (mesh grid) to visualize the regression plane

A slider GUI to input values and see real-time predictions

Export predictions to CSV or Excel

