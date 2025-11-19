## Tema 3. Tarea 3
## *Predicción de series temporales*

**Datos a usar**:

Ocupados (EPA, total nacional): 1er trim de 2002 hasta el último dato disponible. 

Afiliados (a fin de mes, total sistema, total nacional): Enero de 2002 hasta último disponible (octubre de 2025). Disponible [aquí](https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8/EST10/EST305/EST306).

**Tarea**:

Construir un modelo SARIMAX para predecir los ocupados, donde la variable exógena (X) sean los afiliados.  

En concreto, debéis hacer las tres predicciones siguientes:
1. Usando datos de ocupados hasta 4º trim de 2024, aportad la predicción del número de ocupados (en miles) para el 1er, 2º y 3er trimestre de 2025 usando el modelo SARIMA. Calculad el coeficiente ```mape``` de vuestra predicción para esos tres trimestres en comparación con la serie real.
2. Usando datos de ocupados hasta 4º trim de 2024, aportad la predicción del número de ocupados (en miles) para el 1er, 2º y 3er trimestre de 2025, usando el model SARIMAX y los afiliados como variable exógena. Calculad el coeficiente ```mape``` de vuestra predicción para esos tres trimestres en comparación con la serie real. ¿Mejora la capacidad del modelo para predecir?
3. Proporcionad un avance del número de ocupados para el cuarto trimestre de 2025 con ayuda de los últimos datos de afiliados.

**Imp**: *Tened en cuenta que la variable de afiliados es mensual y tenéis que trimestralizarla. Normalmente, uno tomaría la media de los tres meses de cada trimetre; sin embargo, como para el 4º trimestre de 2025 solo tenéis el mes de octubre, entonces, para que todos los periodos (trimestres) sean comparables, la trimestralización debe consistir en seleccionar el primer mes de cada trimestre: enero para el primer trimestre, abril para el segundo, julio para el tercero y octubre para el cuarto. Por supuesto, esto se aplica a todos los años, no solo a 2025.*

Cuando se usan regresores exógenos, es **fundamental** asegurarnos de que los periodos en cada tabla son los correctos.

Aplicado a nuestro ejemplo:

|Variable endógena (y): ocupados | variable exógena (x): afiliados |
|----------------------|----------------------|
| **Punto 2 (división entre train y test dataset):** |   |
| Training dataset: 2002Q1 - 2024Q4     | X_in: 2002Q1 - 2024Q4    |
| Test dataset: 2025Q1 - 2025Q3         | X_out: 2025Q1 - 2025Q3    |
| **Punto 3: Predicción hacia el futuro:** |   |
| Datos completos: 2002Q1 - 2025Q3 | X_in: 2002Q1 - 2025Q3 |
| Predicción 4º trim de 2025 |  X_out: 2025Q4 |

*Nótese que solo podemos predecir hacia el futuro 1 periodo porque nuestra variable exógena (afiliados) solo está disponible para un trimestre adicional, no más.*
