import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

data = pd.read_csv('data_C02_emission.csv')

#a)
data = data.drop(['Make', 'Model'], axis=1)
input = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'Fuel Consumption Hwy (L/100km)']
output = ['CO2 Emissions (g/km)']

X = data[input].to_numpy()
y = data[output].to_numpy()

X_train , X_test , y_train , y_test = train_test_split (X , y , test_size = 0.2 , random_state =1 )


#b)
plt.figure()
plt.scatter(X_train[:,4], y_train, c='green', s=1)
plt.scatter(X_test[:,4], y_test, c='red', s=1)
plt.xlabel('Fuel Consumption Comb (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')


#c)
sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

for i in range(0, 6):
    fig, axs = plt.subplots(2)
    axs[0].hist(X_train[:, i], bins=30, color='green')
    axs[0].set_title('Normal')
    axs[1].hist(X_train_n[:, i], bins=30, color='red')
    axs[1].set_title('Standardized')
    plt.show()


#d)
linearModel = lm.LinearRegression()
linearModel.fit( X_train_n , y_train )
print(linearModel.get_params())


#e)
y_test_p = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_p, c='green', s=1)
plt.show()


#f)

mse = mean_squared_error(y_test, y_test_p)
rmse = math.sqrt(mse)
mae = mean_absolute_error(y_test, y_test_p)
mape = mean_absolute_percentage_error(y_test, y_test_p)
r2 = r2_score(y_test, y_test_p)

print("MSE:",mse)
print("RMSE: ",rmse)
print("MAPE: ",mape)
print("R2: ",r2)
    

plt.figure()
plt.scatter(x=X_test_n[:, 0], y=y_test, c="green", s=1)
plt.scatter(x=X_test_n[:, 0], y=y_test_p, c="red", s=1)
plt.show()
