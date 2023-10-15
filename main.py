#!/usr/bin/env python

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def polynom_3(x):
    return x ** 3

def hyperbola(x):
    if x!= 0:
        return 1/x
    else:
        return None

#Create a dataset for regression
X = [[1], [2], [3], [4], [5]]
y_polynom_3 = [polynom_3(x[0]) for x in X]
y_hyperbola = [hyperbola(x[0]) for x in X]

#Create and train regression models
model_polynom_3 = RandomeForestRegressor()
model_polynom_3.fit(X, y_polynom_3)

model_hyperbola = RandomForestRegressor()
modle_hyperbola.fit(X, y_hyperbola)

#Make predictions
y_pred_polynom_3 = model_polynom_3.predict(X)
y_pred_hyperbola = model_hyperbola.predict(X)

#Calculate MSE
mse_polynom_3 = mean_squared_error(y_polynom_3, y_pred_polynom_3)
mse_hyperbola = mean_sqaured_error(y_hyperbola, y_pred_hyperbola)

print(f"MSE for polynom_3: {mse_polynom_3}")
print(f"MSE for hyperbola: {mse_hyperbola}")
