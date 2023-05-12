import pandas as pd
#a)
data = pd.read_csv("data_C02_emission.csv")
print(data.info())

data.dropna(axis=0)
data.drop_duplicates()
data = data.reset_index(drop=True)
print(len(data))

for col in data:
    if type(col) == object:
        data[col] = data[col].astype("Category")

#b)
data_new = pd.DataFrame(
    data, columns=["Make", "Model", "Fuel Consumption City (L/100km)"]
).sort_values("Fuel Consumption City (L/100km)", ascending=False)
print("Najveća potrošnja: ")
print(data_new.head(3))
print("Najmanja potrošnja: ")
print(data_new.tail(3))

#c)
enginebetween2535 = data[
    (data["Engine Size (L)"] >= 2.5) & (data["Engine Size (L)"] <= 3.5)
]
print("Broj vozila s velicinom motora izmedju 2.5L i 3.5L")
print(len(enginebetween2535))
print("CO2: ", enginebetween2535.loc[:, "CO2 Emissions (g/km)"].mean())

#d)
audi_data = data[(data["Make"] == "Audi")]
print("Broj vozila proizvodjaca Audi: ")
print(len(audi_data))
audi4cylinders = audi_data[(audi_data["Cylinders"] == 4)]
print("CO2: ", audi4cylinders.loc[:, "CO2 Emissions (g/km)"].mean())

#e)
cylinders_data = data[data["Cylinders"] % 2 == 0]
print(len(cylinders_data))
print("CO2: ", cylinders_data.loc[:, "CO2 Emissions (g/km)"].mean())

#f)
diesel_data = data[data["Fuel Type"] == "D"]
gasoline_data = data[(data["Fuel Type"] == "X") | (data["Fuel Type"] == "Z")]
print("D", diesel_data.loc[:, "Fuel Consumption City (L/100km)"].mean())
print("B", gasoline_data.loc[:, "Fuel Consumption City (L/100km)"].mean())
print("D", diesel_data.loc[:, "Fuel Consumption City (L/100km)"].median())
print("B", gasoline_data.loc[:, "Fuel Consumption City (L/100km)"].median())

#g)
diesel4cylinders_data = diesel_data[diesel_data["Cylinders"] == 4].sort_values(
    "Fuel Consumption City (L/100km)", ascending=False
)
print(diesel4cylinders_data.head(1))

#h)
manual_data = data[data["Transmission"].str.startswith("M")]
print(len(manual_data))

#i)
print(data.corr(numeric_only=True))
