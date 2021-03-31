
Actividad teórica
-----------------

Las tareas de clasificacion son actividades que comunmente se presentan en diversas áreas, y es una de las aplicaciones más comunes del aprendizaje de máquina, especialmente el aprendizaje supervisado. En este apartado se analizarán algunas de las técnicas mas comunes:

* K-NN
* Decision trees
* Random forest
* Boosting (Adaboost)
* SVM

Consulte y describa en detalle cómo funciona cada una de estas técnicas. Realice una tabla comparativa entre ellas. Incluya en la tabla las ventajas, desventajas y aplicaciones comunes.

k-NN (k-Nearest Neighbor)
:	k-NN es la abreviación en ingles de `k vecinos mas cercanos`. Es un método
de clasificación de datos. Se calcula a partir de tomar una cantidad `k` de
vecinos de una muestra que se consideren los mas cercanos bajo alguna funcion
de distancia. El resultado esperado de esta técnica es la clasificación de esta
muestra, que se obtiene a partir de encontrar la clase mas común entre estos `k`
vecinos. Cuando se usa `k` = 1, se le asigna directamente la clase del vecino
mas cercano.

Decision trees
:	Decision trees viene de "Árboles de decisión". Este método consiste en
clasificar una muestra basado en la aplicación de criterios especificados en
una estructura en forma de árbol. Se parte desde el primer criterio, y según el
resultado de ese criterio, se aplican otros criterios consecutivamente en base
a las ramifiaciones del árbol. Las hojas del árbol son donde se determina la
clasificación de cada muestra.

Random forest
:	Random forest es un método de clasificación "ensemble" (conjunto) que
consiste en la construcción y aplicacion de múltiples _decision trees_ y la
evaluación de la __moda__ de los resultados para obtener una clasificación. La
aplicación de múltiples arboles corrige los problemas de los _decision trees_
de sobreajustarse a los datos de entrenamiento. Aún así, el rendimiento de los
random forest se puede ver afectado por sesgos o discontinuidades en los datos.

Boosting
:	Boosting es un meta-algoritmo de aprendizaje automático que reduce los
errores de clasificasión basado en el principio que se puede crear un
clasificador robusto a partir de un conjunto de clasificadores débiles. Un
clasificador débil es un clasificador que correlaciona de manera débil una
muestra con su clasificación verdadera. El clasificador robusto de boosting
parte de usar los resultados de varios clasificadores débiles e integrar sus
resultados asignandoles pesos para obtener la clasificación final.

	El método de boosting mas popular es Adaboost (Adaptive Boosting) que
consiste en 



### Comparación entre técnicas de clasificación:

| Técnica        | Ventajas       | Desventajas         | Aplicaciones          |
| -------------- | -------------- | ------------------- | --------------------- |
| k-NN           | 
| Decision trees |
| Random forest  |
| Boosting       |
| SVM            |


Revise el material de lectura, el de apoyo y consulte información adicional y responda los siguientes puntos:

* ¿Qué significa clasificar patrones?, dé algunos ejemplos de aplicaciones reales
* ¿Qué significa una cliasificación binaria?, ¿Qué es una clasificación multi-label?

Realice una investigación en la web buscando problemas prácticos de clasificación y resuelva los siguientes ejercicios.

* Identifique y describa de forma clara y concisa el problema
* Identifique y describa la secuencia de pasos desarrollados para resolver el problema
* Diga cuál o cuales pasos involucran estrategias de clasificación
* Tomando lo aprendido ¿considera que la o las técnicas empleadas son adecuadas?, ¿Podría formularuna mejor opción?, Justifique sus respuestas

Actividad práctica
------------------

Realice una búsqueda en la red de un problema de clasificación del cual pueda descargar el dataset y pueda recrear la implementación y resultados. Con lo aprendido hasta ahora en el curso y lo cencerniente a este tema, resuelva

* Identifique el problema y los pasos de tratamiento de datos y ML empleados para su solución
* Identifique la(s) estrategia(s) de clasificación utilizada(s)
* Realice una propuesta para cambiar o modificar la etapa de clasificación. Explique en detalle dicha modificación.
* Tomando como base las comparaciones entre técnicas de clasificación realizadas en la parte teórica, argumente las razones y posibles cambios en el desempeño del método.
* Realice las pruebas correspondientes, experimentos, uso de estrategias de cross-validation y evalúe los resultados antes y después de sus modificaciones
* Haga un análisis de los resultados y haga un contraste entre lo que consideró para la modificación del método y los resultados obtenidos

