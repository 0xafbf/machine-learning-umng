
Actividad teórica
-----------------

Realizar clustering (agrupamiento) es otra de las actividades comunes en una
aplicación de Machine Learning para resolver problemas. Agrupar los datos puede
entre otras cosas, facilitar tareas de clasificación, permite entender la
estructura de los datos e identificar tendencias o patrones que de otra forma
no resultaria fácil. Existen múltiples estrategias para realizar clustering,
algunas de las más populares son:

* K-means/k-medians
* DBSCAN
* Gaussian mixture models (EM-GMMs)
* BIRCH

Revise el material de lectura, el de apoyo y consulte información adicional y
responda los siguientes puntos:

* En el contexto de machine learning, ¿Qué significa clustering?

Clustering es el agrupamiento de muestras _no etiquetadas_ que tienen
similaridad entre ellas. Esta similaridad se establece con una _medida de
similaridad_. A medida que las muestras incrementan en dimensionalidad, su
medida de similaridad se convierte en un algoritmo más complejo

---

* ¿Qué aplicaciones tiene el clustering? Mencione aplicaciones reales

**Marketing:** Descubrir grupos de clientes potenciales.

**Suelos:** Identificar areas de usos de la tierra similares.

**Servicios de streaming:** Tienen una base de datos de clientes, y los pueden
agrupar por intereses.

En Google usan Clustering para __generalización__, __compresión de datos__ y
__preservación de la privacidad__ de las siguientes maneras:

__Generalización:__ Los videos de youtube menos populares se ubican en un
cluster de videos más populares para alimentar el motor de recomendaciones.

__Compresión de datos:__ Los videos de youtube contienen muchos datos como
visualizaciones, ubicación, fecha, demográficas, etc. que se pueden sintetizar
en un cluster que relacione todos esos datos. Por ejemplo: cluster de videos de
gatos que hacen que las personas en latinoamérica hagan muchos comentarios.

__Preservación de la privacidad:__ De esta manera "anonimizan" un poco los
datos del usuario, de manera que las recomendaciones no son tan específicas.
Por ejemplo: te recomienda un video de gatos porque has visto videos de gatos,
en lugar de recomendarte videos de gatos blancos con manchas grises.

---

* ¿Qué tipos de estrategias existen para realizar clustering?
* Para los tipos mencionados, explique su fundamento.
* Indique y explique las ventajas y desventajas de cada uno de los tipos de
  técnicas de clustering.

---

### Clustering basado en centroides

Es un tipo de clustering que organiza los datos en clusters no
jerárquicos. En general consisten en establecer clusters alrededor de un punto
basado en la distancia de cada muestra respecto al centro del cluster. El
algoritmo de centroides más usado es K-means. Estos algoritmos son eficientes
en procesamiento, pero son sensibles a las condiciones iniciales y a los
valores atípicos.

---

### Clustering basado en densidad

Consiste en conectar áreas de alta densidad de muestras y de esta manera hacer
crecer el cluster. Esto permite que los clusters tengan formas arbitrarias
desde que las áreas tengan una densidad de muestras consistentes.

#### Desventajas

Estos algoritmos tienen problemas con datos con densidad irregular o
dimensiones altas. Por diseño, estos algoritmos no le asignan ningún cluster a
los valores atípicos.

#### Ejemplo: 

---

### Clustering basado en distribución

Este método asume que los datos están compuestos de distribuciones como la gaussiana. Consisten en encontrar los centros de estas distribuciones y de esta manera asignar un cluster a cada muestra basado en qué probabilidad tiene esta muestra de pertenecer a cada uno de los clusters.

#### Desventajas

Este clustering asume que se conoce la distribución de los datos. Cuando no se sabe la manera en la que se distribuyen los datos se debe usar otro algoritmo.

---

### Clustering jerárquico

El clustering jerárquico crea un árbol de clusters, por esto es muy adecuado para datos jerárquicos como 

---


* Explique detalladamente al menos un método por cada tipo de técnica de
  clustering.

* Muestre y explique ejemplos de uso de los algoritmos estudiados.


Actividad práctica
------------------

Busque en la red ejemplos desarrollados donde se apliquen los métodos
mencionados en este capítulo, descargue los datos y ejecute el código de cada
ejemplo. Realice experimentos siguiendo los siguientes pasos:

* Revise y describa el problema a resolver en cada uno de los ejemplos
  estudiados

* Entienda el funcionamiento (paso a paso) de los ejemplos, identificando
  específicamente la o las técnicas de clustering utilizadas.

* Determine los parámetros específicos de los métodos de clustering utilizados

* Explore (realice la variación) cómo los diferentes parámetros afectan el
  desempeño de los métodos trabajados.

* Considere cambiar la estrategia de clustering aplicada originalmente, indique
  cuál método nuevo se utilizó y argumente la razón de escogerlo.

* Compare los resultados del experimento original y el modificado, explique las
  diferencias y formule una hipótesis sobre las causas de las diferencias en
  los resultados



