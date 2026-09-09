# Pipeline Básico de Procesamiento de Datos - Hollywood Movies

## Descripción
Este proyecto consiste en un pipeline automatizado desarrollado en Python utilizando Pandas y NumPy. El script procesa el dataset `Hollywood Movies` cargando el archivo original, seleccionando las variables requeridas, limpiando los datos faltantes con estrategias según la naturaleza de cada columna, generando métricas financieras y de calidad, realizando agrupaciones analíticas y exportando el dataset procesado listo para su uso.

---

## Preguntas de Razonamiento

* **Etapa 1:** *¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a limpiar directamente desde la primera columna que veas?*
  Diagnosticar el dataset completo al inicio permite obtener una visión panorámica de la calidad y estructura general de los datos. Esto ayuda a definir la mejor estrategia de limpieza (imputación vs. eliminación) para todo el conjunto en lugar de tomar decisiones aisladas columna por columna que podrían resultar incompatibles o destruir datos valiosos.

* **Etapa 2:** *¿Qué pasaría si rellenaras Budget con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna Ganancia que vas a crear en la próxima etapa?*
  Si se rellena `Budget` con 0, al calcular la ganancia (`WorldGross - Budget`), la fórmula asumirá que la película no costó nada producirla. Esto inflaría artificialmente la columna `Ganancia`, haciendo que las películas sin presupuesto reportado aparezcan como altamente rentables cuando en realidad no se conoce su costo.

* **Etapa 3:** *Ganancia se calcula restando (WorldGross - Budget). ¿Qué representaría, en cambio, una columna que dividiera WorldGross entre Budget? ¿En qué caso preferirías esa versión en vez de la resta?*
  Dividir `WorldGross` entre `Budget` representaría el Retorno de Inversión (ROI) o multiplicador de taquilla. Preferiría esa versión al evaluar la eficiencia financiera de proyectos con presupuestos muy dispares; por ejemplo, para comparar el rendimiento de una película independiente de bajo presupuesto con el de un blockbuster multimillonario.

* **Etapa 4:** *¿Qué habría pasado si hubieras intentado ordenar por Ganancia antes de limpiar los nulos de WorldGross y Budget en la Etapa 2? ¿Por qué el orden en que se hacen las etapas importa aquí?*
  Si no se hubieran limpiado los nulos previamente, la columna `Ganancia` habría heredado valores `NaN` en esas filas. Al ordenar por `Ganancia`, Pandas colocaría los registros nulos al final o interferiría en el ordenamiento, imposibilitando identificar de manera precisa las películas realmente más rentables.

* **Etapa 5:** *De los géneros con más películas en el dataset (Comedia, Acción, Drama), ¿cuál tiene el promedio de calificación de crítica más alto? ¿Te sorprende, o era lo que esperabas?*
  Drama es el género que suele registrar las mejores calificaciones promedio por parte de la crítica especializada entre los géneros más comunes. No resulta sorprendente, ya que la crítica tiende a valorar con mejor puntuación el desarrollo narrativo e interpretativo de producciones dramáticas frente a comedias o películas de acción comercial.

* **Etapa 6:** *¿Por qué guardar el resultado en un archivo nuevo (hollywood_limpio.csv), en vez de sobrescribir el archivo original hollywood.csv que descargaste?*
  Mantener inmutable el archivo original asegura la integridad de la fuente de datos raw. Esto permite auditar los datos originales en cualquier momento, corregir el código sin perder el punto de partida o reejecutar el pipeline bajo nuevos criterios sin tener que descargar nuevamente la información.

---

## Escenarios de Transferencia

* **Escenario 1:** *Si el dataset tuviera una columna de fechas completas (día, mes y año) en vez de solo el año, ¿qué tendrías que verificar antes de poder ordenar el dataset cronológicamente por esa columna?*
  Tendría que verificar que la columna esté convertida al tipo de dato `datetime64` de Pandas (usando `pd.to_datetime()`). Si la columna permaneciera como tipo texto (`object`), el ordenamiento se haría de forma alfabética/lexicográfica y no en un orden cronológico real.

* **Escenario 2:** *Si quisieras aplicar este mismo pipeline a un dataset completamente distinto (por ejemplo, canciones con su artista, género y número de reproducciones), ¿qué partes de tu código cambiarían, y cuáles seguirían exactamente igual?*
  Cambiarían los nombres de las columnas seleccionadas, los nombres de los archivos de entrada/salida y las fórmulas/condiciones específicas de las nuevas columnas. Seguirían exactamente igual la secuencia lógica del pipeline, la sintaxis de filtrado por columnas, los métodos de limpieza (`fillna`, `dropna`), la conversión de tipos, el ordenamiento y el método `.to_csv(..., index=False)`.

* **Escenario 3:** *Si una columna nueva tuviera 95% de sus valores nulos (mucho peor que Genre, que tenía cerca del 29%), ¿seguirías rellenándola de la misma forma? ¿Qué harías distinto, y por qué?*
  No la rellenaría de la misma forma. Imputar el 95% de una columna crearía datos sintéticos y sesgaría gravemente cualquier análisis. En su lugar, optaría por eliminar esa columna por completo o convertirla en una variable binaria (indicando si el dato está disponible o no).
