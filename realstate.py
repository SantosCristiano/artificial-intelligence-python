#https://datatofish.com/multiple-linear-regression-python/
#https://www.aprendemachinelearning.com/regresion-lineal-en-espanol-con-python/

import pandas as pd
import pandas as Dataframe
from sklearn import linear_model
import statsmodels.api as sm

#leemos el csv
datos = pd.read_csv("barrios.csv")
#dataframe:
dataframe = pd.DataFrame(datos)
print(datos)
X = (dataframe[["metros","barrio"]])
Y = (dataframe['precio'])

print(X)
print(Y)

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# prediction with sklearn
metros = 200
barrio = 1
tipo = 1
print ('Precio aproximado de: \n', regr.predict([[metros ,barrio]]))

# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)