import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

show = False

# Leer el DataFrame desde el archivo CSV
df = pd.read_csv("Datasets/tp_final/df_max_usage.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index(df["DATE"])

if show:
    plt.figure(figsize=(15, 6))  # Configurar el tamaño de la figura
    plt.plot(df['DATE'], df['MAX_USAGE'])  # Graficar los datos de consumo máximo diario
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Agregar cuadrícula
    plt.xlabel('Fecha')  # Etiqueta para el eje x
    plt.ylabel('Consumo Diario Máximo (kWh)')  # Etiqueta para el eje y
    plt.title('Consumo Máximo Diario de Electricidad')  # Título
    plt.tight_layout()  # Ajustar diseño para evitar superposición

    if len(df) > 50:
        plt.xticks(rotation=45)  # Rotar etiquetas del eje x si hay muchos datos

    plt.show()

series = pd.Series(
    df['MAX_USAGE'].values, index=df['DATE'], name="Consumo Máximo Diario de Electricidad"
)

# res = STL(series, seasonal=3).fit()
# res.plot()
# plt.show()

period = 30
decomposition = seasonal_decompose(series, model='additive', period=period)  # Specify additive model
decomposition.plot()
plt.show()

# Extraer la tendencia de la descomposición
trend = decomposition.trend.dropna()

import statsmodels.api as sm

# Ajustar un modelo de regresión lineal
X = sm.add_constant(np.arange(len(trend)))
model = sm.OLS(trend, X).fit()

# Visualizar la tendencia y el modelo ajustado
plt.plot(trend.index, trend.values, label="Tendencia")
plt.plot(trend.index, model.fittedvalues, label="Modelo ajustado")
plt.xlabel('Fecha')
plt.ylabel('Consumo Diario Máximo (kWh)')
plt.title('Tendencia Observada y Modelo Ajustado')
plt.legend()
plt.grid(True)
plt.show()

