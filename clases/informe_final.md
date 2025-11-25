### INSTRUCCIONES PARA LA REALIZACIÓN DEL TRABAJO FINAL

### CURSO 2025-2026

#### *LEA LAS SIGUIENTES INSTRUCIONES CON DETENIMIENTO*
---
* El trabajo consiste en realizar un informe de coyuntura trimestral sobre una de las comunidades autónomas españolas. La comunidad autónoma sobre la que versará el informe es asignada de manera aleatoria por el profesor.
* El trabajo se realizará en grupos de dos estudiantes, a elegir libremente.
* El informe se supone que va dirigido al equipo de asesores del Consejero de Economía de la Comunidad Autónoma; por tanto, debéis suponer que no va dirigido al profesor. Dadle, pues, un **carácter y formato profesional**.
* El informe tendrá una extensión de 6 páginas A4, a una carilla, y deberá generarse "automáticamente" a través de un notebook de Jupyter, usando preferentemente la librería ```matplotlib```. 
* La fecha máxima para la entrega del trabajo será el miércoles 24 de diciembre de 2025 a las 14:00 horas.
  
---
#### CONTENIDO DEL INFORME:
**1. Resumen:** *(1 página)* 
  1. Exponer de manera resumida y representar gráficamente las principales variables que definen la evolución de la economía de la región.
  2. Explicar y justificar el momento del ciclo en el que se encuentra la economía regional y las previsiones sobre su evolución en el corto plazo.
  * Esta sección es muy importante y debe ser lo suficientemente atractiva para generar interés en el lector respecto al resto del informe.

**2. Actividad productiva:**  *(1 página)*
  1. PIB.
  2. Índice de Producción Industrial.
  3. Índice de confianza empresarial.
  4. Otros indicadores que estén disponibles y estiméis oportuno.

**3. Demanda:** *(1 página)*  
  * Opción a) (*plus de nota*):
    1. Índicador sintético de consumo en la comunidad autónoma, construido por vosotros.
    2. Indicadores parciales más representativos (relevantes) del indicador sintético.
    3. Evolución del sector exterior (exportaciones, importaciones y balanza comercial).
  * Opción b):
    1. Indicadores de demanda interna disponibles para vuestra comunidad autónoma.
    2. Evolución del sector exterior (exportaciones, importaciones y balanza comercial).

**4. Mercado de trabajo:** *(1 página)*
  1. Tasas de actividad, empleo y paro (EPA).
  2. Evolución de la afiliación a la Seguridad Social.
  3. Evolución del paro registrado.
  4. Otros indicadores que estén disponibles y estiméis oportuno.
     
**5. Precios y costes:** *(media página)*
  1. Inflación (IPC). Total y subyacente (es decir, sin energía ni alimentos no elaborados).
  2. Costes laborales. Salariales y no salariales.

**6. Previsiones:** *(media página)*
  1. Previsión propia de la tasa de crecimiento del PIB para el *cuarto trimestre de 2025* usando el modelo SARIMAX.  
  2. Previsión propia de la tasa de paro para el *cuarto trimestre de 2025* usando el modelo SARIMAX.  
  * En ambos casos, como variable exógena podéis usar una variable concreta o un indicador compuesto de varias variables. Observad que podéis usar los datos de afiliaciones, contratos y paro registrado, consumo eléctrico, IPI, etc., de los meses de octubre y noviembre para realizar las predicciones. En la nota al pie del gráfico, explicar brevemente la metodología (la técnica usada y qué variable exógena).
  * Además, en base a la predicción del punto 6.1, comentad cuál se espera que sea el crecimiento del PIB anual en 2025 (como suma de los cuatro trimestres).
    
**7. Cuadro de indicadores:** *(1 página)*
  * Tabla de indicadores donde se muestren los valores de los principales indicadores durante los últimos periodos.
  * La tabla debe incluir *al menos* todas las variables e indicadores mostrados en el informe.
  
---
---
* Los indicadores arriba citados deben mostrarse en gráficos y de manera complementaria en el Cuadro de Indicadores.
* El informe debe tener fecha de diciembre de 2025 y debe estar actualizado con los últimos datos disponibles a la fecha de entrega. Esto implica que, por ejemplo, los datos de afiliados a la Seguridad Social deben incluir los del mes de noviembre.
* **Mostrar siempre en los gráficos (y tablas, en su caso) los valores para España con fines comparativos** (excepto en la sección 6). 
* Debéis elegir críticamente en cada caso cómo han de ir expresadas o medidas las variables mostradas en el informe. Por ejemplo, ¿tiene sentido mostrar la tasa de variación del ICC? ¿Tiene sentido mostrar el IPC en niveles? ¿Deben usarse datos desestacionalizados o brutos?
* Además del uso de gráficos, se deberá incluir un breve texto explicativo en cada apartado. En el texto tenéis que describir muy brevemente (en una frase) la evolución reciente de cada variable, tal y como se hace en los informes de coyuntura referenciados en clase.
* En relación con los periodos a mostrar en el informe, debéis ser consistentes a lo largo del informe y mostrar siempre los mismos. Tomar otros informes como ejemplo para decidir qué rango temporal mostrar.
* El informe se entregará a través del Aula Virtual, incluyendo los siguientes archivos:
  1. El informe en formato PDF. Este es el principal documento del informe.
  2. El notebook de Jupyter que genera el informe.
  3. El archivo Excel con todos los datos usados en el informe y de los que se nutre el notebook del punto anterior. El fichero Excel deberá contener también una hoja adicional con una leyenda explicativa.
     
* [**Aquí**](https://otoperalias.github.io/Coyuntura/) tenéis ejemplos de los mejores informes de los cursos pasados. Prestad especial atención al informe del último curso.
  
---
#### **EVALUACIÓN**:
* **El trabajo supone tres de los seis puntos de la evaluación continua**. 
* Peso de cada sección del informe:

| Apartado  | Extensión aprox. | Peso en la evaluación |
| ------------- | ------------- |  ------------- |
| 1. Resumen  | 1 pág.  | 15% |
| 2. Actividad productiva | 1 pág.  | 15% |
| 3. Demanda  | 1 pág.  | 15% |
| 4. Mercado de trabajo  | 2 págs.  | 15% |
| 5. Precios y costes  | 1 pág.  | 10% |
| 6. Previsiones  | 1 pág.  | 15% |
| 7. Cuadro de indicadores  | 1 pág.  | 15% |


* Cada sección se evaluará tanto por la rigurosidad y pertinencia del contenido como por la forma (es decir, el formato y el estilo). 
* La nota global del informe es igual a la suma ponderada de la puntuación obtenida en cada apartado. Dicha nota sufrirá deducciones en los siguientes casos:  
  1. El estilo y formato no se mantienen constantes a lo largo del informe. Por ejemplo, los gráficos del primer apartado son de una manera y los gráficos de otro apartado siguen un formato y estilo diferente. 
  2. La estructura es deficiente porque, por ejemplo, no se sigue el orden establecido arriba.  
  3. El notebook de Jupyter no genera correctamente el informe. Por ejemplo, no se cargan los datos (por error de lectura o porque faltan en el archivo Excel) o los gráficos no se generan.
