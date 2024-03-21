import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

show = True

# Leer el DataFrame desde el archivo CSV
df = pd.read_csv("Datasets/tp_final/df_max_usage.csv")
df['DATE'] = pd.to_datetime(df['DATE'])

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

# Realizar la descomposición de series temporales
decomposition = seasonal_decompose(df['MAX_USAGE'], model='additive', period=1)

# Graficar las cuatro componentes de la descomposición
plt.subplot(411)
plt.plot(df['DATE'], decomposition.trend, label='Tendencia')
plt.legend()

plt.subplot(412)
plt.plot(df['DATE'], decomposition.seasonal, label='Estacionalidad')
plt.legend()

plt.subplot(413)
plt.plot(df['DATE'], decomposition.resid, label='Residuos')
plt.legend()

plt.subplot(414)
plt.plot(df['DATE'], decomposition.observed, label='Observado')
plt.legend()

plt.show()
