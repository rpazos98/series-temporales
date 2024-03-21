from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

show = False
export = True

df = pd.read_csv("Datasets/tp_final/D202.csv")
df_clean = df[['DATE', 'END TIME', 'USAGE']]

# Concatena las columnas 'DATE' y 'END TIME' en una nueva columna llamada 'DATETIME'
# df_clean['DATETIME'] = df_clean['DATE'] + ' ' + df_clean['END TIME']
# df_clean['DATETIME'] = pd.to_datetime(df_clean['DATETIME'])

daily_max_usage = df_clean.groupby('DATE')['USAGE'].max()

df_max_usage = pd.DataFrame({
    'DATE': daily_max_usage.index,
    'MAX_USAGE': daily_max_usage.values
})

df_max_usage['DATE'] = pd.to_datetime(df_max_usage['DATE'])

df_max_usage = df_max_usage.sort_values(by='DATE')

df_max_usage = df_max_usage.reset_index(drop=True)

print(df_max_usage.head())
print(df_max_usage['DATE'].min())
print(df_max_usage['DATE'].max())
print(len(df_max_usage))

df_max_usage.to_csv("Datasets/tp_final/df_max_usage.csv", index=False)

if show:
    plt.figure(figsize=(15, 6))  # Set a larger figure size for clarity
    plt.plot(df_max_usage['DATE'], df_max_usage['MAX_USAGE'])  # Use markers and line style
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines with better style
    plt.xlabel('Date')  # Use a more descriptive label
    plt.ylabel('Maximum Daily Consumption (kWh)')  # Use a more descriptive label
    plt.title('Daily Maximum Electricity Consumption')  # More informative title
    plt.tight_layout()  # Adjust spacing to avoid overlapping elements

    if len(df_max_usage) > 50:
        plt.xticks(rotation=45)

    plt.show()

