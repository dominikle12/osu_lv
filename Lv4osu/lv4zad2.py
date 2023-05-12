import pandas as pd
import sklearn.linear_model as lm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score, max_error
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

ohe = OneHotEncoder()
X_encoded = ohe.fit_transform(data[['Fuel Type']]).toarray()

y = data['CO2 Emissions (g/km)']
X = data[['Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)',
          'Fuel Consumption Comb (L/100km)', 'Engine Size (L)', 'Fuel Consumption Comb (mpg)', 'Cylinders']]

(X_train, X_test, y_train, y_test) = train_test_split(
    X, y, test_size=0.2, random_state=1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)

y_test_prediction = linearModel.predict(X_test)

MAE = mean_absolute_error(y_test, y_test_prediction)
MAPE = mean_absolute_percentage_error(y_test, y_test_prediction)
MSE = mean_squared_error(y_test, y_test_prediction)
R2 = r2_score(y_test, y_test_prediction)

MAX_ERROR = max_error(y_test, y_test_prediction)

data["difference"] = abs(data['CO2 Emissions (g/km)'] - MAX_ERROR)
car = data[data["difference"] == data["difference"].max()]

print("Najveće odstupanje iznosi:", round(data["difference"].max(), 2), "g/km")
print("Najveće odstupanje je za automobil:")
print(car)
