---
abstract: |
  This is the abstract. It consists of two paragraphs.
author:
- Andrés Botero
- Carlos Guerrero
babel-lang: english
bibliography: bibliography.bib
csl: bibliography.csl
date: 2021-02-07
keywords:
- one
- two
- three
lang: en
numbersections: yes
title: Conceptos básicos
---

## Actividad teórica:

### ¿Qué es Machine Learning?

Es el estudio de algoritmos de computador que se mejoran automáticamente
por medio de la experiencia. Usan un un modelo basado en *datos de
entrenamiento* para hacer predicciones o decisiones sin ser programado
específicamente para eso.

### ¿Cuál es el objetivo principal del Machine Learning?

El machine learning busca que sea el mismo computador el que cree el
algoritmo necesario para resolver un problema, ya que puede ser un
problema tan complejo, que crear un algoritmo para resolver el problema
puede ser demasiado desafiante para que un humano pueda desarrollarlo.

### ¿Qué diferencia y/o relación existe entre Machine Learning e Inteligencia Artificial?

Inteligencia artificial puede considerarse cualquier algoritmo que lleve
a un computador a tomar decisiones "inteligentes" basadas en datos de
entrada. Puede abarcar campos desde la gestion de procesos industriales
hasta los videojuegos, pero generalmente representa comportamientos de
inteligencia humana plasmados en algoritmos. Machine learning es un tipo
de IA donde se busca que sea la misma máquina la que llega a este
"conocimiento" mediante un proceso de aprendizaje de la máquina o
"entrenamiento".

### Explique: ¿Cómo diferenciar una aplicación de machine learning de una aplicación de inteligencia artificial?

La diferencia particular del machine learning es que el algoritmo final
es generado por la misma máquina basado en observaciones. Basado en esto
se puede identificar una aplicación de machine learning si requiere de
datos iniciales para ser entrenada. Además de esto la aplicación de
machine learning se puede hacer mejor cada vez a medida que es usada y
entrenada, mientras que otro tipo de inteligencia artificial va a
generar los mismos resultados ante los mismos estímulos.

### Mencione al menos 3 aplicaciones generales de machine learning

Seguridad, en la deteccion de rostro por medio de grabaciones de camaras
de seguridad Busqueda en linea, el sistemas de busqueda que manejan los
navegadores Procesamiento de lenguage natural, como lo es Alexa y Siri
que reconocen la voz y el idioma

### Mencione y explique 3 aplicaciones de Machine Learning en ingenieria

Prediccion de fallos en una maquinaria, esto ayuda a prevenir fallos
graves y costosos, ademas de poder programar la reparacion de la
maquinaria sin dañar la productividad. Auto ajustes en una aplicacion,
la aplicacion se ajusta a los gustos del usuario y le da opciones basado
en los gustos, constumbres y/o necesidades. Analisis de imagenes de alta
calidad, con este tipo de imagenes se le enseña que tipo de imagenes se
esta buscando.

### Explique que relacion existe entre machine learning e ingenieria mecatronica?

Ya que

### Mencione y explique 3 aplicaciones de machine learning en el escenario especifico de la ingeniería para la que se está formando

Prediccion de fallos en una maquinaria, ya que con esto se puede
programar detencion de la maquinaria y cambiar los implementos
necesarios previniendo fallos graves y costosos. Analisis de imagenes,
por medio de grabaciones en la deteccion del rostro o por medio de una
camara para emparejar las imagenes y hacer un espaciado 3D del entorno.

### Para las aplicaciones mencionadas anteriormente, diga ¿Qué estrategias diferentes a Machine Learning pueden ser usadas para resolver el problema?

Para predicir un fallo solo es con las con las estadisticas de las
piezas que contienen en el manual programando una mantenimiento para
revisar el estado de la pieza En el analisis de imagenes para la
deteccion de rostros tocaria pausar el video y seleccionar la parte de
la imagen donde se encuentre el rostro.

### Investigue ¿Qué es la regresión lineal? y ¿Cuál es su relación y aplicación con Machine learning?

Es un modelo matemático para aproximar la relacion entre una variable
dependiente y varias variables independientes.

La manera de lograr esto es partir de una funcion lineal (o cualquier
función), y mediante un proceso iterativo se busca que esta función se
vaya adaptando a un resultado, buscando reducir al máximo la diferencia
entre la función y los datos con los que se compara. Es decir, se busca
minimizar la diferencia entre los datos reales y la función lineal (o
cualquier otra)

Para lograr esto es conveniente tener una manera de medir esta
*diferencia*. Esto se hace con una **función de costo** que nos indique
numéricamente qué tan cerca de los datos reales está nuestra predicción.
Una función de costo popular es la función del *error cuadrático medio*
mostrada a continuación:

    ECM = 1/n * sum( (prediccion_i - dato_i)^2 )

Para buscar la aproximación óptima (la que tenga el error mínimo) es
necesario ajustar las influencias de las variables independientes sobre
la predicción. Este proceso se hace de manera iterativa usando el
concepto de descenso de gradiente.

El descenso de gradiente, de manera resumida, consiste en tomar dos
predicciones A y B (con dos valores de influencia cercanos) y evaluar
cuál de las predicciones es más acertada (usando nuestra función de
costo). Luego de esto podemos ajustar las influencias del modelo en la
dirección que tiende a reducirse el error de la predicción. De esta
manera cada nuevo paso va reduciendo el error.

### Investigue ¿Qué es la regresión logística? y ¿Cuál es su relación y aplicación con machine learning?

## Actividad práctica:

### Regresión de una variable:

Considere el escenario de predecir el valor de una casa dependiendo del
área. Adquiera o genere un dataset que represente el problema. Tomando
como base la regresión lineal, se tiene que el valor de una casa es una
función del área

    y = A0 + A1*x

Donde y es el valor predicho y x es el área en metros cuadrados, el
modelo lineal tiene los parámetros A0 y A1, el problema de Machine
learning es encontrar los valores de los parámetros A0 y A1 que adapten
el modelo a los datos.

En Machine Learning el método mas comúnmente aplicado para estimar los
parámetros de un modelo es el gradiente descendente, para ello se
requiere diseñar una función de costo. \* Plantee la función de costo
para el problema mencionado \* Aplique el gradiente descendente para
encontrar los parámetros del modelo. Considere hacer normalización de
los datos. \* ¿Cuál es el metodo idóneo con el que se normalizan los
datos?

mse 2819766538489.7344 mse after 77223648707.19275
![](linear_regression.png "linear_regression")

### Regresión multivariable:

Considere ahora que existe más de una característica para predecir el
valor de la casa, ej. área, numero de habitaciones, años de
construcción, etc. Así el modelo se convierte en:

    y = A0 + A1 X1 + A2 X2 + ... + AnX

-   ¿Cómo se plantearía la nueva función de costo teniendo en cuenta el
    nuevo conjunto de datos? realice la implementación
-   Aplique el gradiente descendente para ajustar el modelo a los datos.
    Considere hacer normalicación de los datos.

![](error_de_regresion_multivariable.png "error de regresion multivariable")

### Clasificación con regresión logística

Considere el escenario donde se quiere saber si un tumor es maligno o
benigno. Se asume que dicha condiciónd epende del tamaño del tumor. Para
este problema se considera que existen 2 clases, tumor maligno
(identificada como y=1) y tumor benigno (identificada como y=0) en
machine learning la herramienta más sencilla para generar un l ímite o
frontera de decisión (decision boundary) es la regresión logística, cuyo
modelo matemático es:

    p = 1 / (1+exp(x))

donde p indica el grado de pertenencia (a veces probabilidad) de la
observación x a una categoría o clase, para el ejemplo mencionado tumor
maligno o benigno.

-   cómo se genera la función de costo para esta aplicación y de qué
    forma se puede incorporar en el algoritmo de gradiente descendente?
    implemente
-   Aplique el algoritmo de gradiente descendente para ajustar el modelo
    de clasificación y evalúe el desempeño del modelo ajustado
-   ¿como se evalua dicho desempeño?

## Conclusion

### Autoevaluación:

En este apartado debe realizar una autoevaluación del proceso
desarrollado y de las habilidades adquiridas con las actividades
propuestas. Para ello responda las siguientes preguntas otorgando el
valor porcentual (0 - 100 %) a cada una de ellas.

1.  ¿Desarrolló la totalidad de las actividades propuestas?

2.  ¿La metodología le permitió construir saberes significativos que le
    aporten al desarrollo del tema planteado?

3.  ¿Qué tanto fue su grado de dedicación durante el desarrollo de las
    actividades planteadas?

4.  ¿Qué tanto fue su grado de interés en el tema propuesto?

5.  Otorgue un valor porcentual a cada uno de los indicadores de las
    metas propuestas según su cumplimiento

### Retroalimentación:

En esta sección se espera que a partir de lo vivido durante el
desarrollo de las actividades propuestas, Ud pueda dar algunas
recomendaciones o sugerencias sobre el tema y el desarrollo de las
mismas. Tenga en cuenta que sus aportes enriquecen el ejercicio docente,
gracias.
