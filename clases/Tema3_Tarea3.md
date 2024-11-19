## Tema 3. Tarea 3
## *Predicción de series temporales*

**Datos a usar**:

Ocupados (EPA): 1er trim de 2002 hasta el 3er trim de 2024

Afiliados: Enero de 2002 hasta último disponible (octubre de 2024)

**Tarea**:

Construir un modelo SARIMAX para predecir los ocupados, donde la variable exógena (X) sean los afiliados.  

En concreto, debéis hacer las tres predicciones siguientes:
1. Usando datos de ocupados hasta 4º trim de 2023, aportad la predicción del número de ocupados (en miles) para el 1er, 2º y 3er trimestre de 2024 usando el modelo SARIMA. Calculad el coeficiente ```mape``` de vuestra predicción para esos tres trimestres en comparación con la serie real.
2. Usando datos de ocupados hasta 4º trim de 2023, aportad la predicción del número de ocupados (en miles) para el 1er, 2º y 3er trimestre de 2024, usando el model SARIMAX y los afiliados como variable exógena. Calculad el coeficiente ```mape``` de vuestra predicción para esos tres trimestres en comparación con la serie real. ¿Mejora la capacidad del modelo para predecir?
3. Proporcionad un avance del número de ocupados para el cuarto trimestre de 2024 con ayuda de los últimos datos de afiliados. Notad que disponéis de los datos de afiliados para el mes de octubre, que es el primer mes del último trimestre. Hay varias maneras de crear una variable X válida para el modelo SARIMAX:
    * a) Crear una variable X que contenga los afiliados del primer mes de cada trimestre (ya que para el 4º trimestre solo tenemos el primer mes).
    * b) Predecir los afiliados de los meses de noviembre y diciembre con el modelo SARIMA y entonces usar la predicción del 4º trimestre de afiliados en el modelo SARIMAX.
    * Notad que independientemente de la opción usada, la variable X debe estar en frecuencia trimestral. La función ```resample()``` es muy práctica para ello. 

Una vez hecho lo anterior, completen la actividad del aula virtual antes del viernes 22 de noviembre.
