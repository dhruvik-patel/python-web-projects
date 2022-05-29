import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Position_Salaries.csv")

X = dataset.iloc[:,1:2].values
y  = dataset.iloc[:,2].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,y)

y_pred = regressor.predict([[6.5]])

plt.scatter(X , y , color='red')
plt.plot(X , regressor.predict(X) , color='blue')
plt.title('Truth or bluff(Decision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

X_grid = np.arange(min(X),max(X),0.01)				# points are 1, 1.1, 1.2, 1.3,....., 9.7, 9.8, 9.9
X_grid = X_grid.reshape((len(X_grid),1))			# row = len(X_grid) column = 1
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('True or Not(Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()