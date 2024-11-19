### INSTRUCCIONES PARA LA REALIZACIÓN DEL TRABAJO FINAL

### CURSO 2024-2025

#### *LEA LAS SIGUIENTES INSTRUCIONES CON DETENIMIENTO*
---
* El trabajo consiste en realizar un informe de coyuntura trimestral sobre una de las comunidades autónomas españolas. La comunidad autónoma sobre la que versará el informe es asignada de manera aleatoria por el profesor.
* El trabajo se realizará en grupos de dos estudiantes, a elegir libremente.
* El informe se supone que va dirigido al equipo de asesores del Consejero de Economía de la Comunidad Autónoma; por tanto, debéis suponer que no va dirigido al profesor. Dadle, pues, un carácter y formato profesional.
* El informe tendrá una extensión máxima de 8 páginas A4, a una carilla, y deberá generarse "automáticamente" a través de un notebook de Jupyter, usando preferentemente la librería ```matplotlib```. 
* El informe debe ir acompañado de un anexo donde se explique la metodología seguida para la construcción del indicador sintético de consumo (apartado 3.1) y para las predicciones del apartado 6. El anexo es otro documento. No debe mezclarse con el informe.
* La fecha máxima para la entrega del trabajo será el viernes 20 de diciembre de 2024 a las 23.00 horas.
  
---
#### CONTENIDO DEL INFORME:
**1. Resumen:** 
  1. Exponer de manera resumida y representar gráficamente las principales variables que definen la evolución de la economía de la región.
  2. Explicar y justificar el momento del ciclo en el que se encuentra la economía regional y las previsiones sobre su evolución en el corto plazo.

**2. Actividad productiva:** 
  1. PIB.
  2. Índice de Producción Industrial.
  3. Índice de confianza empresarial.
  4. Otros indicadores que estén disponibles y estiméis oportuno.

**3. Demanda:** 
  1. Índicador sintético de consumo en la comunidad autónoma, construido por vosotros.
  2. Indicadores parciales más representativos (relevantes) del indicador sintético.
  3. Evolución del sector exterior (exportaciones, importaciones y balanza comercial).

**4. Mercado de trabajo:**
  1. Tasas de actividad, empleo y paro (EPA).
  2. Evolución de la afiliación a la Seguridad Social.
  3. Evolución del paro registrado.
  4. Otros indicadores que estén disponibles y estiméis oportuno.
     
**5. Precios y costes:**
  1. Inflación (IPC). Total y subyacente (es decir, sin energía ni alimentos no elaborados).
  2. Costes laborales. Salariales y no salariales.

**6. Previsiones:**
  1. Previsión propia de la tasa de crecimiento del PIB para el *cuarto trimestre de 2024* usando el modelo SARIMAX.  
  2. Previsión propia de la tasa de paro para el *cuarto trimestre de 2024* usando el modelo SARIMAX.  
  * En ambos casos, como variable exógena podéis usar una variable concreta o un indicador compuesto de varias variables. Observad que podéis usar los datos de afiliaciones, contratos y paro registrado, consumo eléctrico, IPI, etc., de los meses de octubre y noviembre para realizar las predicciones.
  * Además, en base a la predicción del punto 6.1, comentad cuál se espera que sea el crecimiento del PIB anual en 2024 (como suma de los cuatro trimestres).
    
**7. Cuadro de indicadores:**
  * Tabla de indicadores donde se muestren los valores de los principales indicadores durante los últimos periodos.
  
---
---
* Los indicadores arriba citados deben mostrarse en gráficos y, de manera complementaria (en algunos casos que se considere oportuno) en tablas.
* **Mostrar siempre en los gráficos (y tablas, en su caso) los valores para España con fines comparativos.**
* Debéis elegir críticamente en cada caso cómo han de ir expresadas o medidas las variables mostradas en el informe. Por ejemplo, ¿tiene sentido mostrar la tasa de variación del ICC? ¿Tiene sentido mostrar el IPC en niveles? ¿Deben usarse datos desestacionalizados o brutos?
* Además del uso de gráficos (y, en su caso, tablas), se deberá incluir un breve texto explicativo en cada apartado. En el texto tenéis que describir muy brevemente (en una frase) la evolución reciente de cada variable, tal y como se hace en los informes de coyuntura referenciados en clase.
* En relación con los periodos a mostrar en el informe, debéis ser consistentes a lo largo del informe y mostrar siempre los mismos. Tomar otros informes como ejemplo para decidir qué rango temporal mostrar.
* El informe se entregará a través del Aula Virtual, incluyendo los siguientes archivos:
  1. El informe en formato PDF. Este es el principal documento del informe.
  2. El anexo que contiene los detalles metodológicos de los apartados 3.1 y 6.
  3. El notebook de Jupyter que genera el informe.
  4. El archivo Excel con todos los datos usados en el informe y de los que se nutre el notebook del punto anterior. El fichero Excel deberá contener también una hoja adicional con una leyenda explicativa.
     
* [**Aquí**](https://otoperalias.github.io/Coyuntura/) tenéis ejemplos de los mejores informes de los cursos pasados. Prestad especial atención al informe del último curso.
  
---
#### **EVALUACIÓN**:
* **El trabajo supone cuatro de los seis puntos de la evaluación continua**. 
* Peso de cada sección del informe:

| Apartado  | Extensión aprox. | Peso en la evaluación |
| ------------- | ------------- |  ------------- |
| 1. Resumen  | 1 pág.  | 10% |
| 2. Actividad productiva | 1 pág.  | 10% |
| 3. Demanda  | 1 pág.  | 20% |
| 4. Mercado de trabajo  | 2 págs.  | 20% |
| 5. Precios y costes  | 1 pág.  | 10% |
| 6. Previsiones  | 1 pág.  | 20% |
| 7. Cuadro de indicadores  | 1 pág.  | 10% |


* Cada sección se evaluará tanto por la rigurosidad y pertinencia del contenido como por la forma (es decir, el formato y el estilo). 
* La nota global del informe es igual a la suma ponderada de la puntuación obtenida en cada apartado. Dicha nota sufrirá deducciones en los siguientes casos:  
  1. El estilo y formato no se mantienen constantes a lo largo del informe. Por ejemplo, los gráficos del primer apartado son de una manera y los gráficos de otro apartado siguen un formato y estilo diferente. 
  2. La estructura es deficiente porque, por ejemplo, no se sigue el orden establecido arriba.  
  3. El notebook de Jupyter no genera correctamente el informe. Por ejemplo, no se cargan los datos (por error de lectura o porque faltan en el archivo Excel) o los gráficos no se generan.
