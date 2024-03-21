from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
dateparse2 = lambda x: datetime.strptime(x, '%d%m%Y')


df1 = pd.read_csv("Datasets/RIGO.2012.2021.csv", parse_dates=['fechaHora'], date_parser=dateparse)

df1_clean = df1.drop(df1.columns[0], axis=1)

print(df1_clean.head())


plt.plot(df1_clean['fechaHora'], df1_clean['ultimoPrecio'])  # Assuming 'y' is the column you want to plot
plt.xlabel('Año')
plt.ylabel('Precio de la acción')
plt.title('Precio de RIGO')
plt.show()


df1 = pd.read_csv("Datasets/YPFD.2000.2021.csv", parse_dates=['fechaHora'], date_parser=dateparse)

df1_clean = df1.drop(df1.columns[0], axis=1)

print(df1_clean.head())


plt.plot(df1_clean['fechaHora'], df1_clean['ultimoPrecio'])  # Assuming 'y' is the column you want to plot
plt.xlabel('Año')
plt.ylabel('Precio de la acción')
plt.title('Precio de YPFD')
plt.show()

df1 = pd.read_csv("Datasets/TECO2.2000.2021.csv", parse_dates=['fechaHora'], date_parser=dateparse)

df1_clean = df1.drop(df1.columns[0], axis=1)

print(df1_clean.head())


plt.plot(df1_clean['fechaHora'], df1_clean['ultimoPrecio'])  # Assuming 'y' is the column you want to plot
plt.xlabel('Año')
plt.ylabel('Precio de la acción')
plt.title('Precio de TECO')
plt.show()