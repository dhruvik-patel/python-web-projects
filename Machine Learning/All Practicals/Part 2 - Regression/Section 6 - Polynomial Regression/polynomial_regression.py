#1 importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2 set present working directory and importing the data set
dataset = pd.read_csv('Position_Salaries.csv')

#3 matrix of independent variable (feature matrix)
X = dataset.iloc[:,1:2].values

#4 array of dependent variable
y = dataset.iloc[:,2].values


"""#7 Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""


"""#8 Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""

# fitting linear regression to the dataset (for comparison)
from sklearn.linear_model import LinearRegression
linear_regression = LinearRegression()
linear_regression.fit(X,y)

# fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_regression = PolynomialFeatures(degree=4)
X_poly = poly_regression.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

# visualising the Linear Regression results (for comparison)
plt.scatter(X,y,color='red')
plt.plot(X,linear_regression.predict(X),color='blue')
plt.title('True or Not(Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the polynomial regression results
X_grid = np.arange(min(X),max(X),0.1)				# points are 1, 1.1, 1.2, 1.3,....., 9.7, 9.8, 9.9
X_grid = X_grid.reshape((len(X_grid),1))			# row = len(X_grid) column = 1
plt.scatter(X,y,color='red')
plt.plot(X_grid,lin_reg_2.predict(poly_regression.fit_transform(X_grid)),color='blue')
plt.title('True or Not(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# predicting with linear regression (for comparison)
linear_regression.predict([[6.5]])

# predicting with polynomial regression
lin_reg_2.predict(poly_regression.fit_transform([[6.5]]))