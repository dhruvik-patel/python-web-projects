"""
Created on Sun Mar  1 21:09:21 2020

@author: Dhruvik
"""
#1 importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2 set present working directory and importing the data set
dataset = pd.read_csv('Data.csv')

#3 matrix of independent variable (feature matrix)
X = dataset.iloc[:,:-1].values

#4 array of dependent variable
y = dataset.iloc[:,3].values

#5 taking care of missing data
from sklearn.impute import SimpleImputer
simpleimp = SimpleImputer(missing_values=np.nan, strategy='mean', verbose=0)
simpleimp = simpleimp.fit(X[:,1:3])
X[:,1:3] = simpleimp.transform(X[:,1:3])


#6 encoding categorical data
# independent variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
#dependent variables
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

"""from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)"""

#7 Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#8 Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1,1))