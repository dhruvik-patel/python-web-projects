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

#7 Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

#8 Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1,1))		# convert into matrix
y = y[:,0]									# convert into array

# fitting the SVR Model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

# predicting a new result
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))

# Visualising the SVR Results
plt.scatter(X,y,color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('True or Not(Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
