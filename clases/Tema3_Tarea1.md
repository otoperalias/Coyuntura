## Tema 3. Tarea 1
## *Informe sobre afiliaciones a la Seguridad Social*

* Datos a usar: [Serie de afiliados a la Seguridad Social](https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST8/EST10/EST290/EST291) => **Serie de afiliación Media por regímenes 2001 - 2024**).   
Debéis usar la columna de "Total sistema", es decir, los afiliados totales.  

* Con los métodos de descomposición clásico aditivio, STL y el X13ARIMA-SEATS, averiguar cuándo las afiliaciones a la Seguridad Social tocaron fondo durante la crisis inmobiliaria-financiera que empezó en 2008, es decir, en qué mes las afiliaciones alcanzaron su valor más bajo. ¿Coincide con el mes en el que la serie bruta, sin desestacionalizar, alcanzó su valor mínimo?

* Calcular también, con cada método, cuáles son **de media** los meses del año con mayor y menor número de afiliaciones, y cuál es la diferencia entre ambos meses.  
Naturalmente, aquí me estoy refiriendo al carácter estacional de la serie y debéis analizar el componente estacional de la misma.

* Por último, probar a usar la opción ```robust=True```  en el [método STL](www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.STL.html#statsmodels.tsa.seasonal.STL).  
¿Cambia en algo el análisis anterior? Si es así, ¿por qué?  
Echar un vistazo a [este ejemplo de descomposición STL](https://www.statsmodels.org/stable/examples/notebooks/generated/stl_decomposition.html)  
Como podéis observar en el enlace anterior, con datos mensuales, debéis especificar la opción seasonal=13 con el método STL.

Una vez hecho lo anterior, debéis completar la actividad *Tema3_Tarea1* disponible en el Aula Virtual, con fecha límite **viernes 8 de noviembre a las 23:55**.

