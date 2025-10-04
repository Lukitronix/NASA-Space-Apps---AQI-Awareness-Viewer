# This file was made with the help of artificial intelligence.
import pandas as pd
import glob
from datetime import timedelta
import warnings
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

all_files = glob.glob("./daily_aqi_by_cbsa_*.csv")
print("Archivos encontrados:", all_files)

df_list = []
for filename in all_files:
    df = pd.read_csv(filename)
    df.columns = [c.strip().replace('"','').upper() for c in df.columns]

    if 'DATE' in df.columns and 'AQI' in df.columns:
        df_list.append(df[['DATE', 'AQI']])
    else:
        print(f"Archivo {filename} no tiene las columnas necesarias, se ignora.")

if not df_list:
    raise ValueError("No se encontraron CSV válidos para procesar.")

data = pd.concat(df_list)
data['DATE'] = pd.to_datetime(data['DATE'])
data = data.sort_values('DATE').set_index('DATE')
print("Datos cargados correctamente, primeras filas:")
print(data.head())

data_daily = data.groupby(data.index).mean()

data_hourly = data_daily.resample('h').interpolate(method='linear')
print("Datos resampleados a horario, primeras filas:")
print(data_hourly.head())

data_hourly = data_hourly.dropna()
df_features = data_hourly.copy()
for lag in range(1, 25):
    df_features[f'lag_{lag}'] = df_features['AQI'].shift(lag)

df_features['day_of_week'] = df_features.index.dayofweek
df_features['hour_of_day'] = df_features.index.hour

df_features = df_features.dropna()
print("Features creados, primeras filas:")
print(df_features.head())

X = df_features.drop(columns=['AQI'])
y = df_features['AQI']

warnings.filterwarnings("ignore", category=RuntimeWarning)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
print("Modelo RandomForest entrenado correctamente.")

joblib.dump(model, 'aqi_model.joblib')
print("Modelo guardado en 'aqi_model.joblib'.")

forecast_steps = 48
last_known = df_features.iloc[-1]

predictions = []
current_features = last_known.drop('AQI').copy()

for step in range(forecast_steps):
    X_pred = current_features.values.reshape(1, -1)
    pred_aqi = model.predict(X_pred)[0]
    predictions.append(pred_aqi)

    for lag in range(24, 1, -1):
        current_features[f'lag_{lag}'] = current_features[f'lag_{lag-1}']
    current_features['lag_1'] = pred_aqi

    forecast_time = df_features.index[-1] + timedelta(hours=step+1)
    current_features['day_of_week'] = forecast_time.dayofweek
    current_features['hour_of_day'] = forecast_time.hour

forecast_index = pd.date_range(
    start=df_features.index[-1] + timedelta(hours=1),
    periods=forecast_steps,
    freq='h'
)

forecast_df = pd.DataFrame({'DATE': forecast_index, 'PREDICTED_AQI': predictions})

forecast_df.to_csv('aqi_forecast_48h.csv', index=False)
print("Predicción de 48h guardada en 'aqi_forecast_48h.csv'.")
print(forecast_df)