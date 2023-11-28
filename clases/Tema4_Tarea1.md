## Tema 4. Tarea 1. Construcción del Indicador Sintético de Consumo

La tarea propuesta consiste en replicar la construcción del **Indicador Sintético de Consumo**, perteneciente a los *Indicadores sintéticos de la economía española* (Ministerio de Asuntos Económicos).  
Para realizar esta tarea tenéis que seguir la metodología empleada por el Ministerio, disponible [aquí](https://serviciosede.mineco.gob.es/indeco/DescargaArchivo.aspx?estadisticas=True&tipo=1), sobre la cual hemos trabajado en el notebook anterior ([Ejercicio práctico: replicar el indicador sintético de inversión en equipo ISE](https://github.com/otoperalias/Coyuntura/blob/main/clases/Tema4_ISE.ipynb)).  
<br/><br/>
El Indicador Sintético de Consumo se crea a partir de nueve indicadores parciales. Estos nueve indicadores, junto con el código de los mismos en la [base de datos del ministerio](https://serviciosede.mineco.gob.es/indeco/bdsice/Busquedas/busquedas_new.aspx), son los siguientes:

#### Indicador Sintético de Consumo 
|Indicador parcial | Codigo base datos ministerio|
|------------------|-----------------------------|
|1. Remuneración real de asalariados de ventas en grandes empresas| 25b400 (Fuente original: [Estadística de Ventas, Empleo y Salarios en las Grandes Empresas](https://sede.agenciatributaria.gob.es/Sede/datosabiertos/catalogo/hacienda/Informe_Ventas_Empleo_y_Salarios_en_las_Grandes_Empresas.shtml)) |
|2. Índice de comercio al por menor sin estaciones de servicio en términos reales| 272700G |
| 3. Matriculación de automóviles turismos | 271200|
|4. Indicador de confianza del consumidor | 339000 |
|5. Ventas interiores reales de bienes y servicios de consumo en grandes empresas | 25b050  |
|6. Índice de producción industrial de bienes de consumo| 229500 |
|7. Importaciones de bienes de consumo en volumen | 506R60 |
|8. Exportaciones de bienes de consumo en volumen |502R60 |
|9. Financiación a familias e ISFLSH residentes en términos reales Banco de España | 807102  |

<br/><br/>
Debéis descargar los datos, procesarlos y construir el indicador para el máximo periodo temporal posible. Posteriormente calculad, para las tasas de variación interanual, lo siguiente:
1. Cómo de bien mide la macromagnitud del consumo (cód: 941000T) (para lo cual debéis trimestralizar el indicador sintético construido).
2. Cómo de cerca está vuestro indicador sintético de consumo del que calcula el Ministerio.

<br/><br/>

Una vez realizado lo que se pide en la tarea, debéis responder a este breve cuestionario: [Formulario Tarea 1 del Tema 4](https://docs.google.com/forms/d/e/1FAIpQLSdrFrQC3nee4ULba_SgWh5BXhqjEHRPWJ8kYVm9SJeRqSkaiQ/viewform?usp=sf_link).
