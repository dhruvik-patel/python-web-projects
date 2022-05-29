#1 importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2 set present working directory and importing the data set
dataset = pd.read_csv('F:\Dhruvik\Machine Learning\All Practicals\Part 2 - Regression\Section 5 - Multiple Linear Regression\\50_Startups.csv')

#3 matrix of independent variable
X = dataset.iloc[:,:-1].values

#4 array of dependent variable
y = dataset.iloc[:,4].values

#6 encoding categorical data
# independent variables : Create Object And then run fit&transform method on that object
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])						# convert to numerics
onehotencoder = OneHotEncoder(categorical_features=[3])				# column number of categorical data(state)
X = onehotencoder.fit_transform(X).toarray()				# specify that numerics are independent(not < or >)

# Avoiding dummy variable trap -> remove any one column from dummy variables HERE California is removed (col 0)
X = X[:,1:]

#7 Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#8 Feature Scaling
'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)'''

# Fitting(Defining pattern for prediction) multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)			# compare this y_pred with y_test

# building optimal model using Bacward Elimination :: OLS = Ordinary Least Squares
import statsmodels.api as sm
X = np.append(arr=np.ones((50,1)).astype(int), values = X,axis=1)	# appending first column of ones before X
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,1,2,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,1,4]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()