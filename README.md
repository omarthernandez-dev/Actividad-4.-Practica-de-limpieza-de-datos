# Actividad 4 - Limpieza de datos
26B_ANALISIS Y VISUALIZACION DE LA INFORMACION

## Objetivo
Aplicar técnicas de limpieza y transformación de datos con Python en una base de datos diseñada para contener problemas de calidad.

## Procedimiento
- Se revisaron valores faltantes, duplicados y tipos de datos.
- Se reemplazaron valores inválidos como "ERROR" y "UNKNOWN" por `NaN`.
- Se convirtieron columnas numéricas y de fecha a su tipo correcto.
- Se imputaron valores faltantes con mediana (numéricos) y moda (categóricos).
- Se eliminaron registros deventas negativas.
- Se exportó la base limpia como `Cafe_Sales_Clean.csv`.

# Problemas y decisiones

| Problema encontrado        | Registros afectados                               | Acción realizada                           | Justificación                                   |
|----------------------------|---------------------------------------------------|--------------------------------------------|-------------------------------------------------|
| Valores faltantes          | Item=333, Payment Method=2579, Location=3265      | Imputación con mediana/moda                | Mantener representatividad sin sesgos extremos  |
| Duplicados                 | 0 registros                                       | No se aplicó acción, no había duplicados   | No se detectaron duplicados                     |
| Errores de formato         | Valores 'ERROR' y 'UNKNOWN'                       | Reemplazo por NaN y corrección             | Homogeneizar formatos para análisis correcto    |
| Valores atípicos           | 259                                               | Eliminación de negativos, revisión manual  | Solo se descartaron valores imposibles          |
| Tipos de datos incorrectos | Quantity, Price Per Unit, Total Spent             | Conversión con to_numeric y to_datetime    | Necesario para cálculos y análisis temporal     |
