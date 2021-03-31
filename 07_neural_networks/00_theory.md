

Redes neuronales y Deep Learning
================================

Andrés Botero, 1201310

Actividad teórica
-----------------

Las redes neuronales artificiales (RNA) son una técnica de machine learning que
está inspirada en la estructura y el funcionamiento del tejido
nervioso. Usualmente las RNA son modelos de aprendizaje supervisado, aunque
existen algunas arquitecturas de aprendizaje no supervisado. Realice una
revisión de literatura sobre el tema de las RNA y responda:

### De forma general describa cómo funciona una RNA

Una RNA consiste en una red de nodos (neuronas) que procesan y
transmiten datos entre ellas de forma ponderada, es decir, con
influencias o pesos variables entre unas y otras. Los enlaces entre
estos nodos no están establecidos inicialmente, sino que se ajustan a
sí mismos basados en el resultado sobre una función de costo.

### Indique algunas de las principales aplicaciones de las RNA

- Traducción de idiomas
- Reconocimiento de voz
- Análisis semántico
- Visión de máquina
  + identificacion de caracteres
  + identificacion de objetos
  + imágenes médicas
- predicción de acciones o divisas



### ¿Cuales son las arquitecturas o configuraciones más comúnmente aplicadas?

Existen varios tipos de redes neuronales
- Redes neuronales prealimentadas: Son el tipo mas simple, ya que los datos
  fluyen en una sola dirección. Incluyen tipos como:
  * Probabilística
  * Convolucional
- Redes neuronales recurrentes: Propagan los datos hacia adelante, pero también
  hacia atrás, lo que le da temporalidad a los datos, es decir, una evaluación
  anterior puede afectar a la siguiente.
- Redes neuronales dinámicas: La forma de la red puede cambiar. Pueden partir
  de una red de baja complejidad y entrenar nuevas conecciones automáticamente.


### De forma general, ¿Cómo es que las RNA son capaces de aprender?

Las RNA pasan los datos suministrados en varias capas de procesamiento hasta
llegar a un resultado. Inicialmente estas capas tienen unos niveles de
influencia arbitrario que proporcionan un resultado que puede no ser bueno. A
partir de ese resultado las capas van variando sus influencias iterativamente
buscando reducir el error del resultado final.


**En la última década el aprendizaje profundo (deep learning, DL), se ha
convertido en una de las técnicas de ML más ampliamente utilizadas grasias a
los buenos resultados en un sinnúmero de problemas. Tomando como base de las
referencias antes mostradas, analice y responda lo siguiente**

### ¿Qué significa deep learning?

Deep learning es un tipo de machine learning que usa redes neuronales con
múltiples capas para extraer características de alto nivel a partir de datos
suminstrados con el fin de obtener resultados con la efectividad que lo podría
lograr un humano.


### Para qué se usa el deep learning? aplicaciones

El deep learning se ha usado con éxito en multitud de aplicaciones. Uno de los
primeros usos del deep learning fue en el reconocimiento del habla, que ha sido
cimiento para los asistentes virtuales que vemos en la actualidad como Siri de
Apple o Cortana de Microsoft.

En adicion a esto, estos asistentes virtuales no solo reconocen las palabras
que dice el usuario, sino que hacen un reconocimiento semántico de las frases
para entender la intención del usuario aún si este dió un mensaje incompleto,
en desorden, o con palabras mal dichas. A esto lo llaman procesamiento natural
del lenguaje (NLP).

El DL también se ha usado en el campo del reconocimiento de imágenes y visión
por computador, ayudando tanto en procesos industriales como en sistemas de
seguridad y vigilancia. Los sistemas de visión por deep learning han logrado
superar las capacidades de visión de los humanos desde hace varios años.

### ¿Qué diferencia el deep learning de otras técnicas de machine learning?

Los algoritmos de deep learning proyectan lograr un nivel de efectividad
similar al de un humano al momento de procesar cierto tipo de informacion. Para
esto el deep learning debe ser capaz de identificar los datos relevantes a
partir de los datos de entrada sin necesidad de que estos datos hayan sido
preparados para ser procesados. Es por esto que los metodos de deep learning
requieren de un entrenamiento más intensivo para aprender a reconocer patrones
entre todas las capas de interpretación que surgen dentro del modelo.

### Qué diferencias existen entre las shallow NN y las deep NN? haga un cuadro comparativo

 Shallow Neural Networks             | Deep Neural Networks
  ---------------------------------- | ---------------------------------
 Tienen pocas capas de procesamiento | Tienen muchas capas de procesamiento
 Requieren de menos computación      | El nivel de computación es elevado
 Requieren preprocesar los datos     | Estan hechas para extraer características de los datos
 Se entrenan con cientos de muestras | Se entrenan con decenas o cientos de miles de muestras


### Qué plataformas o librerías existen para hacer deep learning? haga un cuadro comparativo de las herramientas que encontró

Libreria   | Autor     | Licencia   | Año   | Comentarios
---------- | --------- | ---------- | ----- | -------------
Keras      | 64px      | MIT        | 2015  | Funciona como wrapper de Tensorflow
Tensorflow | Google    | Apache     | 2015  | Usa GPU, tiene bindings para varios lenguajes
PyTorch    | Facebook  | BSD        | 2016  | Usa GPU
Core ML    | Apple     | Closed     | 2017  | Usada para ML embebido
Aesara     | PyMC      | BSD        | 2007  | Anteriormente Theano


Actividad práctica:
-------------------

Tomando como base los dos últimos enlaces en la sección de Material de
apoyo. Realice la implementación en python del ejemplo descrito en la
web. Reproduzca los resultados mostrados y desarrolle la sección Keras Tutorial
Extensions.

Una vez haya realizado lo mencionado, considere el ejemplo en matlab de
clasificación de los símbolos manuscritos. Realice la implementación de dicho
ejemplo y compare las dos plataformas de desarrollo, desde el punto de vista de
la facilidad de implementación y facilidad de manejo por parte del usuario.

* Implemente el ejemplo hecho en python y usando el mismo dataset pero en matlab
* Implemente el ejemplo hecho en matlab y usando el mismo dataset pero en python
* Compare los resultados de los modelos en una y otra herramienta de desarrollo
* Compare los tiempos de entrenamiento de los modelos en cada una de las herramientas
* Analice y concluya sobre lo que aprendió de este ejercicio.

Autoevaluación:
---------------


Bibliografia
------------

https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks