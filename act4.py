import pandas as pd
import numpy as np

df = pd.read_csv("dirty_cafe_sales.csv")
print("Dimensiones iniciales:", df.shape)
print(df.info())
print(df.head())
#identificación de problemas
print("\nValores faltantes por columna:\n", df.isnull().sum())
print("\nDuplicados:", df.duplicated().sum())
print("\nTipos de datos:\n", df.dtypes)
#duplicados
df = df.drop_duplicates().reset_index(drop=True)
#Corrección de tipos de datos
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
#reemplazar ERROR y UNKNOWN por NaN
df = df.replace(r'(?i)^error$', np.nan, regex=True)
df = df.replace(r'(?i)^unknown$', np.nan, regex=True)
#convertir columnas numéricas a float
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
#eliminar filas con demasiados NaN     más del 50% de columnas
threshold = df.shape[1] / 2
df = df.dropna(thresh=threshold)
#imputación de numéricos con mediana
num_cols = df.select_dtypes(include=['float64','int64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())
#imputación de categóricos con moda
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
#valores atípicos en 'Total Spent'
Q1 = df['Total Spent'].quantile(0.25)
Q3 = df['Total Spent'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
outliers = df[(df['Total Spent'] < lower_bound) | (df['Total Spent'] > upper_bound)]
print("\nOutliers detectados en 'Total Spent':", outliers.shape[0])
#eliminar solo valores negativos
df = df[df['Total Spent'] >= 0]


df.to_csv("Cafe_Sales_Clean.csv", index=False)
print("\nDimensiones finales:", df.shape)

