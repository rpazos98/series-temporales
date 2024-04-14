import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("Datasets/tp_final/df_max_usage.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index(df["DATE"])

df[df == 0] = 1e-100

plt.figure(figsize=(15, 6))
plt.plot(df['DATE'], df['MAX_USAGE'])
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlabel('Fecha')
plt.ylabel('Consumo Diario Máximo (kWh)')
plt.title('Consumo Máximo Diario de Electricidad')
plt.tight_layout()

if len(df) > 50:
    plt.xticks(rotation=45)

plt.show()

series = pd.Series(
    df['MAX_USAGE'].values, index=df['DATE'], name="Consumo Máximo Diario de Electricidad"
)

period = 30*12
decomposition = seasonal_decompose(series, model='additive', period=period)  # Specify additive model
decomposition.plot()
plt.show()

trend = decomposition.trend.dropna()

import statsmodels.api as sm

X = sm.add_constant(np.arange(len(trend)))
model = sm.OLS(trend, X).fit()
# cuadrados minimos

plt.plot(trend.index, trend.values, label="Tendencia")
plt.plot(trend.index, model.fittedvalues, label="Modelo ajustado")
plt.xlabel('Fecha')
plt.ylabel('Consumo Diario Máximo (kWh)')
plt.title('Tendencia Observada y Modelo Ajustado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

stationary_series = df['MAX_USAGE']

window = 400
rolling_mean = stationary_series.rolling(window=window).mean()
stationary_series = stationary_series - rolling_mean

stationary_series = stationary_series.diff()

stationary_series_df = pd.DataFrame(columns=["DATE", "MAX_USAGE"])

stationary_series_df['DATE'] = df["DATE"]

stationary_series_df["MAX_USAGE"] = stationary_series

stationary_series_df = stationary_series_df.dropna()

plt.plot(stationary_series_df["DATE"], stationary_series_df["MAX_USAGE"])
plt.title('Serie con transformaciones - Promedio movil + diferenciacion')
plt.xlabel('Fecha')
plt.ylabel('Consumo Diario Máximo (kWh) - Promedio movil + diferenciacion')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

from statsmodels.tsa.stattools import acf

acf_result = acf(stationary_series_df["MAX_USAGE"], nlags=len(stationary_series_df["MAX_USAGE"])-1)

plt.plot(acf_result)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Retraso')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de la Serie transformada de Consumo de Energía')
plt.show()

X = sm.add_constant(np.arange(len(stationary_series_df["MAX_USAGE"])))
model = sm.OLS(stationary_series_df["MAX_USAGE"], X).fit()

plt.plot(stationary_series_df["MAX_USAGE"].index, stationary_series_df["MAX_USAGE"].values, label="Tendencia")
plt.plot(stationary_series_df["MAX_USAGE"].index, model.fittedvalues, label="Modelo ajustado")
plt.xlabel('Fecha')
plt.ylabel('Serie con transformaciones - Promedio movil + diferenciacion')
plt.title('Serie con transformaciones - Promedio movil + diferenciacion y Modelo Ajustado')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
