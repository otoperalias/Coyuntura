## Informe 2
## *Medidas de contención COVID-19 vs. crecimiento económico*

En el actual contexto de la pandemia de coronavirus, se ha discutido sobre la idoneidad de imponer medidas de restricción de la actividad por el daño que hace a la economía. Así, hay quienes argumentan que existe un “trade-off” entre contención de la pandemia y economía: un excesivo énfasis en controlar la pandemia podría llevar a una excesiva reducción de la actividad económica y, por tanto, a una grave crisis económica. A este respecto, resulta interesante analizar si los países que han conseguido contener más la pandemia han sufrido una mayor caída del PIB.

Para responder a esta cuestión, vamos a usar datos de COVID-19 de Our World in Data y datos de PIB de la OCDE.

Debéis centraros en los países **europeos** de la OCDE. Los países miembros de la OCDE lo podéis encontrar en la tabla de datos del PIB que se menciona abajo. Por tanto, vuestra muestra debe contener 26 países (Turquía no lo consideramos europeo para este ejercicio).

Por una parte, debéis calcular la tasa de muertes acumuladas por COVID-19 (por millón de habitantes) desde enero de 2020 a diciembre de 2021. Por otra, con relación al PIB, debéis calcular la tasa de variación anual media del PIB en 2020 y en 2021 (es decir, calcular las tasas de variación anuales para cada año y luego calcular la media).

Una vez calculadas ambas variables, debéis dibujar un gráfico de dispersión (scatter plot) donde visualizar su relación. A su vez, calcular la correlación entre ambas variables (usando la función de pandas .corr)([^1]).

[^1]: [función **pandas** ```.cor```](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html)
[^2]: [función **pandas** ```.merge```](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)

Observad que para unir la tabla de datos de COVID-19 con la tabla de datos de PIB, tenéis que usar la función .merge([^2]) y unir las tablas por la columna del nombre de los países. Para ello, tenéis que aseguraros que los países tienen el mismo nombre en las dos tablas.

Una vez realizado el análisis para el periodo enero 2020 - diciembre 2021, debéis realizarlo de manera independiente para cada año (enero 2020-diciembre 2020 y enero 2021-diciembre 2021).

---

Este informe no debéis entregarlo. En su lugar, haré una serie de preguntas a través de la plataforma para comprobar si habéis hecho la tarea. Por ejemplo, preguntas tales como: ¿los países con una tasa de muertes mayor han sufrido menos caída del PIB? ¿Cuál ha sido la caída del PIB para España en 2020? Etc.

Aunque el informe no se entregue, por favor esforzaros al máximo para crear gráficos de alta calidad y generar el informe en formato HTML.

---

**Descarga de datos de la OCDE:**

Enlace: https://stats.oecd.org/

![OECD data](images/DatosOECD.jpg)

---
**Ayuda datos COVID:**
Para aquellos con problemas para importar los datos de Our World in Data, [**aquí**](https://github.com/otoperalias/Coyuntura/blob/main/clases/datos/owid-covid-data_eu.csv) se encuentra disponible una copia de la base de datos (en formato .csv) que incluye solamente las columnas y países relevantes (y por tanto es más fácil y rápido de cargar). Y [**aquí**](https://raw.githubusercontent.com/otoperalias/Coyuntura/main/clases/datos/owid-covid-data_eu.csv) está el enlace para directamente leer los datos.





