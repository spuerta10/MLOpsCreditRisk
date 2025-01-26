# Lineamientos del proyecto final
[Lineamientos Proyecto Final MLOps.pdf](https://github.com/spuerta10/CFCRPL-creditRiskProject/blob/main/docs/Lineamientos%20Proyecto%20Final%20MLOps.pdf)
# Definición del problema y objetivos
### Actividades
- [x] Claridad en la descripción del problema a resolver. ✅ 2024-10-12
- [x] Establecimiento de objetivos claros y alcanzables. ✅ 2024-10-13
- [x] Documentación detallada de la infraestructura necesaria para llevar a cabo el entrenamiento, despliegue y monitoreo del modelo o aplicación de ML. ✅ 2024-10-12
- [x] Creación de diagramas que representen el flujo de datos en la infraestructura propuesta. ✅ 2024-10-12
- [x] Justificación de la elección de despliegue basada en el objetivo final. ✅ 2024-10-13
---
## Un poco de contexto...
El banco PrestaDificil S.A.S identifico que recibía una gran cantidad de llamadas telefónicas de clientes preguntando si son aptos o no para un préstamo por un monto y razón arbitrarias. Para poder atender a estas llamadas se requerían de asesores en la línea telefónica lo cual implicaba un costo fijo alto. 
Ante esta problemática, el banco, decidió crear un portal web en donde sus clientes pueden ingresar los datos respectivos a su solicitud de préstamo y un modelo de ML responde si el crédito es pre aprobado, o por el contrario, denegado. 
Con el paso del tiempo los analistas de datos del banco han notado que la precisión del modelo ha caído, implicando que ha denegado a potenciales clientes solicitudes de préstamo. 
## El problema
El problema radica en que PrestaDificil S.A.S no posee un proceso en donde se pueda monitorear y mantener la confiabilidad y rendimiento de su modelo de riesgo crediticio en el tiempo. 
## Arquitectura propuesta
![[CFCRPL creditRisk project.drawio]]
La arquitectura propuesta para abordar el problema anteriormente descrito es la mostrada en la siguiente figura. 
**FIGURA 1**
Diagrama de despliegue de creditRisk.
![CFCRPL creditRisk project architecture.png](https://raw.githubusercontent.com/spuerta10/CFCRPL-creditRiskProject/refs/heads/main/docs/img/CFCRPL%20creditRisk%20project%20architecture.png)
Esta arquitectura pretende abarcar y dar solución a los siguientes apartados:
- Gestión de experimentos y modelos.
- Orquestación y pipelines de ML.
- Integración continua incluyendo pruebas.
- Despliegue del modelo.
- Monitoreo de modelos.
## Objetivos
1. **Monitoreo continuo y mantenimiento del rendimiento del modelo de riesgo crediticio**: Se debe de establecer un proceso de monitoreo continuo para garantizar que el modelo de riesgo crediticio se mantenga confiable y preciso a lo largo del tiempo, reduciendo la probabilidad de denegar solicitudes válidas. Esto cumple el objetivo de garantizar la efectividad del modelo en condiciones cambiantes.
2. **Automatización de la actualización y reentrenamiento del modelo**: Se debe incluir un sistema automatizado que evalúe de manera periódica el desempeño del modelo y decida si es necesario reentrenarlo con nuevos datos. Este objetivo ayuda a mantener la precisión del modelo, adaptándose a cambios en el comportamiento de los solicitantes de crédito.
3. **Reducción de costos operativos y mejora de la experiencia del cliente**: Al implementar el proceso de monitoreo y reentrenamiento automático del modelo, se reduce la necesidad de intervención manual, lo que permite al banco optimizar sus costos operativos (como la contratación de asesores) y mejorar la experiencia del cliente al ofrecer respuestas más precisas y rápidas sobre la viabilidad de sus solicitudes de préstamo.
# Gestión de experimentos y modelos
## Actividades
- [x] Implementación de un sistema eficaz para el tracking de experimentos. ✅ 2024-10-12
- [x] Registro adecuado de parámetros, métricas y artefactos de los experimentos. ✅ 2024-10-13
- [x] Versionado efectivo de modelos. ✅ 2024-10-12
- [ ] Implementación de un proceso claro para la selección y promoción de modelos.
- [x] Documentación clara de los experimentos y sus resultados. ✅ 2024-10-12
---
Para la gestión de experimentos y modelos se incorporara el uso de MLFlow, esta plataforma habilitara:
- El tracking de experimentos.
- Registrar los parámetros, métricas y artefactos resultantes de dichos experimentos.
- Versionar los modelos.
- Seleccionar y promover los modelos.
- Documentar los experimentos y sus resultados.
Así pues, los científicos de datos tendrán una plataforma en la cual experimentar diferentes enfoques, pudiendo comparar el rendimiento del modelo de riesgo crediticio que se encuentra en producción contra un modelo de prueba, dado el caso de que el modelo de prueba supere el rendimiento del modelo productivo podrán promover el modelo de prueba a 'challenger'. 
Una vez promovido, el modelo 'challenger' se enfrentara a los productivos, datos de solicitudes de clientes de los últimos diez dias o menos, en caso tal de que el 'challenger' supere al modelo productivo, el científico de datos podrá promover el modelo 'challenger' a productivo y degradar el modelo productivo a 'challenger'.
## Registro de parámetros, métricas y artefactos
En esta sección se especificarán los **parámetros**, **métricas** y **artefactos** que se almacenan en MLFlow para el proyecto. Los **parámetros** son valores que describen características importantes de los datos o del modelo, como el tamaño y las columnas de los datasets en sus diferentes etapas: crudos, preprocesados y procesados. Las **métricas** permiten evaluar el rendimiento del modelo, proporcionando información detallada sobre su precisión, capacidad para identificar correctamente los positivos reales (recall), y el equilibrio entre precisión y recall (F1-score). Por último, los **artefactos** incluyen archivos esenciales para el seguimiento, como el modelo entrenado, los reportes de clasificación generados y los datasets utilizados, tanto en su forma cruda como transformada, lo que facilita la replicación y evaluación del proceso de modelado.
### Parámetros
La siguiente tabla contiene el nombre y la descripción de los parámetros que serán almacenados en MLFlow.
**TABLA 1**
Nombre y descripción de los parámetros almacenados en MLFlow.

| Nombre del parámetro        | Descripción del parámetro                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| rawdataset_shape            | Tamaño del dataset crudo antes de cualquier preprocesamiento. Tupla que indica (filas, columnas).                                    |
| rawdataset_columns          | Lista de nombres de las columnas presentes en el dataset crudo antes del preprocesamiento.                                           |
| preprocesseddataset_shape   | Tamaño del dataset después de la conversión de tipos, eliminación de valores nulos, duplicados y outliers. Indica (filas, columnas). |
| preprocesseddataset_columns | Lista de nombres de las columnas presentes en el dataset después de los pasos de preprocesamiento mencionados.                       |
| processeddataset_shape      | Tamaño del dataset después de realizar ingeniería de características. Indica (filas, columnas).                                      |
| processeddataset_columns    | Lista de nombres de las columnas presentes en el dataset después de realizar ingeniería de características.                          |
**FIGURA 2**
Parámetros almacenados en MLFlow.
![Parametros almacenados en MLFlow proyecto final Bootcamp MLOps.png](https://raw.githubusercontent.com/spuerta10/CFCRPL-creditRiskProject/refs/heads/main/docs/img/Parametros%20almacenados%20en%20MLFlow%20proyecto%20final%20Bootcamp%20MLOps.png)
### Métricas
Principalmente, se almacenará la precisión (accuracy) mostrada por el modelo. Además, se guardará un reporte de clasificación que contiene métricas clave para evaluar el rendimiento del modelo en términos de clasificación. Este reporte incluye los siguientes valores:
- **Precision**: Representa la proporción de predicciones positivas correctas respecto al total de predicciones positivas realizadas. Es decir, cuántos de los casos predichos como positivos realmente lo eran.
- **Recall**: Mide la capacidad del modelo para identificar todos los casos positivos reales. Es decir, de todos los casos que realmente son positivos, qué porcentaje fue correctamente identificado.
- **F1-Score**: Es la media armónica entre precisión y recall, proporcionando una medida equilibrada que refleja tanto la capacidad del modelo para hacer predicciones correctas (precisión) como para identificar correctamente los positivos reales (recall).
- **Support**: Indica el número de ocurrencias de cada clase en el conjunto de datos.

**FIGURA 3**
Precisión mostrada por el modelo almacenada en MLFlow.
![Precision mostrada por el modelo almacenada en MLFlow proyecto final Bootcamp MLOps.png](https://raw.githubusercontent.com/spuerta10/CFCRPL-creditRiskProject/refs/heads/main/docs/img/Precision%20mostrada%20por%20el%20modelo%20almacenada%20en%20MLFlow%20proyecto%20final%20Bootcamp%20MLOps.png)
**FIGURA 4**
Reporte de clasificación almacenado en MLFlow.
![Reporte de clasificación almacenado en MLFlow proyecto final Bootcamp MLOps.png](https://raw.githubusercontent.com/spuerta10/CFCRPL-creditRiskProject/refs/heads/main/docs/img/Reporte%20de%20clasificaci%C3%B3n%20almacenado%20en%20MLFlow%20proyecto%20final%20Bootcamp%20MLOps.png)
### Artefactos
En MLFlow se almacenan varios artefactos clave. El **xgb_model** es el modelo entrenado con XGBoost, listo para hacer predicciones sobre el riesgo crediticio. El **classification_report.txt** contiene el reporte de clasificación con métricas como precisión, recall y F1-score para evaluar el rendimiento del modelo. El **credit_risk_dataset.csv** es el conjunto de datos crudos utilizado para el entrenamiento del modelo, mientras que el **processed_credit_risk_dataset.csv** contiene los datos preprocesados y transformados listos para el análisis.
# Orquestación y pipelines de ML
## Actividades
- [x] Diseño e implementación de pipelines de ML reproducibles y escalables. ✅ 2024-10-12
- [ ] Automatización efectiva de los flujos de trabajo de preprocesamiento, entrenamiento y evaluación.
	- [x] Automatización efectiva del flujo de trabajo de preprocesamiento. ✅ 2024-10-12
	- [x] Automatización efectiva del flujo de trabajo de entrenamiento. ✅ 2024-10-12
	- [ ] Automatización efectiva del flujo de trabajo de evaluación. 
- [x] Manejo adecuado de dependencias entre tareas en los pipelines. ✅ 2024-10-12
- [x] Implementación de mecanismos para la paralelización y distribución de tareas. ✅ 2024-10-12
- [ ] Integración efectiva de los pipelines con sistemas de gestión de recursos.
---
La arquitectura propuesta introduce un Pipeline de reentrenamiento del modelo productivo de riesgo crediticio, dado el caso de que se presente deriva en los datos (data drift). 
El Pipeline mencionado funciona de la siguiente forma:
1. Se comparan las solicitudes de crédito recibidas en la semana contra las solicitudes recibidas en los últimos tres (3) meses con el fin de poder identificar deriva en los datos.
2. En caso de que el Pipeline detecte deriva en los datos se procede a reentrenar y reevaluar el modelo productivo actual, en caso contrario (no se detecto deriva en los datos) el pipeline finaliza su ejecución. 
3. Se compara el rendimiento del modelo productivo reentrenado contra el modelo productivo sin reentrenar, dado el caso de que el modelo reentrenado demuestre mejor rendimiento que su contraparte, se actualiza la versión del modelo productivo. 
## Sobre el despliegue del pipeline
Se propone desplegar el Pipeline de reentrenamiento del modelo productivo de riesgo crediticio en la herramienta 'Cloud Composer' administrada por Google Cloud Platform, tal como se indica en la arquitectura del sistema (figura 1), en la zona 'CFCRPL-creditRiskDAG'.
## Sobre el DAG
El proceso el cual lleva a cabo el DAG de Cloud Composer se compone principalmente de tres (3) etapas:
### 1. Verificar si el numero de peticiones en la semana es suficiente.
En esta etapa el DAG consulta el numero de peticiones de crédito registradas en la semana en BigQuery (*p*). Posteriormente se establece un umbral (*u*), dicho umbral es el numero de peticiones en la semana necesarias para verificar correctamente si existe o no deriva en los datos, en caso tal de que las peticiones semanales sean menores a *u* (*p* < *u*), el DAG finaliza su ejecución. 
👉 El código correspondiente a esta etapa se encuentra [aquí](https://github.com/spuerta10/CFCRPL-creditRiskDAG/blob/dev/src/threshold.py).
### 2. Verificar si existe deriva en los datos.
Si las peticiones semanales satisfacen ser mayores o iguales a *u* (>= *u*), el DAG procede a verificar si existe deriva (*d*) en los datos recolectados de la semana, comparándolos con el histórico de las solicitudes recibidas en los últimos tres (3) meses.
👉 El código correspondiente a esta etapa se encuentra [aquí](https://github.com/spuerta10/CFCRPL-creditRiskDAG/blob/dev/src/drift.py).
### 3. Reentrenamiento y revalidación del modelo. 
Finalmente y en caso tal de que se halle la existencia de deriva en los datos (*d* == true), se procederá a ejecutar una funciona anónima encargada de reentrenar, reevaluar, y dado el caso, de actualizar la versión del modelo productivo.
👉 El código correspondiente a esta etapa se encuentra [aquí](https://github.com/spuerta10/CFCRPL-creditRiskDAG/blob/dev/src/retrain.py).

En la interfaz de composer (composer UI), el proceso y etapas anteriormente descritas se ven de la siguiente forma.
**FIGURA 5**
retrainMLModelPipeline steps.
![retrainMLModelPipeline.png](https://raw.githubusercontent.com/spuerta10/CFCRPL-creditRiskProject/refs/heads/main/docs/img/retrainMLModelPipeline.png)
# Integración continua incluyendo pruebas
## Actividades
- [x] Implementación de un pipeline de CI/CD robusto para proyectos de ML. ✅ 2024-10-12
- [ ] Uso de IaC para el despliegue de la infraestructura de entrenamiento o inferencia.
- [ ] Ejecución de pruebas automatizadas.
- [ ] Automatización efectiva del proceso de entrenamiento, evaluación y despliegue de modelos.
	- [x] Automatización efectiva del proceso de entrenamiento. ✅ 2024-10-12
	- [ ] Automatización efectiva del proceso de evaluación. 
	- [x] Automatización efectiva del proceso de despliegue. ✅ 2024-10-12
---
...
# Despliegue del modelo
## Actividades
- [x] Despliegue del modelo en el modo más pertinente (batch, online, streaming). ✅ 2024-10-12
- [x] Ejemplo de consulta de predicciones. ✅ 2024-10-12
- [x] Documentación clara de la API del modelo. ✅ 2024-10-12
---
El modelo ha sido habilitado a través de una API web y está desplegado en modo de predicciones en línea. Este enfoque fue elegido porque el modelo debe realizar predicciones bajo demanda. Es decir, cada vez que un usuario solicite la aprobación o denegación de crédito por parte de PrestaDificil S.A.S., el modelo determinará si el solicitante es apto para el préstamo.

Para consultar el modelo, se puede utilizar una aplicación como Postman. La API web requiere un cuerpo en formato JSON con la siguiente información:
```json
{
 "person_age":22,
 "person_income":59,
 "person_home_ownership":"RENT",
 "person_emp_length":123,
 "loan_intent":"PERSONAL",
 "loan_grade":"D",
 "loan_amnt":35,
 "loan_int_rate":16.2,
 "loan_percent_income":0.59,
 "cb_person_default_on_file":"Y",
 "cb_person_cred_hist_length":3
}
```

El endpoint disponible para realizar consultas es `http://URI/predict` o `https://URI/predict`. A modo de ejemplo, se utilizará la dirección local `http://127.0.0.1:8080/predict` para mostrar cómo realizar una petición al endpoint.

La siguiente figura contiene un ejemplo de consulta de predicción. 
**FIGURA 6**
Ejemplo de consulta de predicciones.
![[Ejemplo de consulta predicciones proyecto final Bootcamp MLOps.png]]

Las siguientes tablas contienen una descripción del endpoint y del cuerpo en formato JSON necesario para realizar la solicitud.
**TABLA 2**
Descripción del endpoint

| Método requerido | Endpoint | Descripción                                                                                                              |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| POST             | /predict | Analiza, pre procesa y solicita una predicción de un MLModel en función de los datos de las solicitudes de los clientes. |

**TABLA 3**
Descripción del cuerpo en formato JSON.

| Nombre de la llave         | Descripción de la llave                                            | Tipo de dato permitido | Valores permitidos            |
| -------------------------- | ------------------------------------------------------------------ | ---------------------- | ----------------------------- |
| person_age                 | Edad de la persona en años                                         | Int                    |                               |
| person_income              | Ingreso anual de la persona en miles                               | Float                  |                               |
| person_home_ownership      | Estado de propiedad de la vivienda                                 | String                 | RENT, OWN, MORTGAGE.          |
| person_emp_length          | Duración del empleo en meses                                       | Float                  |                               |
| loan_intent                | Propósito o intención del préstamo                                 | String                 | PERSONAL, EDUCATION, MEDICAL. |
| loan_grade                 | Calificación del préstamo asignada por el prestamista              | String                 | A, B, C, D.                   |
| loan_amnt                  | Monto del préstamo en miles                                        | Float                  |                               |
| loan_int_rate              | Tasa de interés del préstamo en porcentaje                         | Float                  |                               |
| loan_percent_income        | Monto del préstamo como porcentaje del ingreso anual de la persona | Float                  |                               |
| cb_person_default_on_file  | Indica si la persona tiene un historial de incumplimiento          | String                 | Y para Sí, N para No.         |
| cb_person_cred_hist_length | Duración del historial crediticio de la persona en años            | Int                    |                               |
|                            |                                                                    |                        |                               |

👉 El código correspondiente a esta etapa se encuentra [aquí.](https://github.com/spuerta10/CFCRPL-onlinePredictService)

# Monitoreo de modelos
## Actividades
- [ ] Implementación de un sistema robusto de logging para modelos en producción.
- [ ] Configuración de alertas para detectar degradación del rendimiento del modelo.
- [ ] Implementación de mecanismos para la detección de data drift y concept drift.
	- [x] Implementación de mecanismos para la detección de data drift. ✅ 2024-10-12
	- [ ] Implementación de mecanismos para la detección de concept drift.
- [ ] Diseño e implementación de dashboards para visualizar métricas clave del modelo.
---
Para detectar la deriva (drift) en los datos, se utilizó el módulo **Evidently**, que facilita la monitorización del rendimiento de los modelos de ML. Se emplearon dos componentes clave:

1. **`Report`**: Genera un informe detallado sobre el rendimiento del modelo y los cambios en la distribución de los datos, ayudando a identificar posibles problemas de drift.
2. **`DataDriftPreset`**: Compara las distribuciones de los datos de entrada actuales con los datos de referencia, detectando diferencias significativas que podrían afectar la precisión del modelo.

Ambos componentes permiten detectar de manera eficiente el drift en los datos y ayudan a mantener la fiabilidad del modelo.

👉 El código correspondiente para detectar de manera eficiente el drift en los datos se encuentra [aquí](https://github.com/spuerta10/CFCRPL-creditRiskDAG/blob/dev/src/drift.py).