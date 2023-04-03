import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('data_C02_emission.csv')

data = data.drop(["Make", "Model"], axis=1)

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders']

output_variables = ['CO2 Emissions (g/km)']
X = data[input_variables].to_numpy()
y = data[output_variables].to_numpy() 

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state =1)
fig1 = plt.figure("Scatter ulaznih vrijednosti")
plt.scatter(X_train[:,0], y_train, c="green")
plt.scatter(X_test[:,0], y_test, c="blue")


sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

fig2, axes2 = plt.subplots(2)

axes2[0].hist(X_train[:,0])
axes2[1].hist(X_train_n[:,0])


linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

y_test_p = linearModel.predict(X_test_n)

fig3 = plt.figure("Scatter izlaznih vrijednosti")
plt.scatter(y_test, y_test_p)

print(linearModel.coef_)
MAE = mean_absolute_error ( y_test , y_test_p )
print(MAE)


plt.show()
