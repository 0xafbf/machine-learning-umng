
Actividad práctica:
-------------------

### Regresión de una variable:
Considere el escenario de predecir el valor de una casa dependiendo del área. Adquiera o genere un dataset que represente el problema. Tomando como base la regresión lineal, se tiene que el valor de una casa es una función del área
```
y = A0 + A1*x
```
Donde y es el valor predicho y x es el área en metros cuadrados, el modelo lineal tiene los parámetros A0 y A1, el problema de Machine learning es encontrar los valores de los parámetros A0 y A1 que adapten el modelo a los datos.


      
En Machine Learning el método mas comúnmente aplicado para estimar los parámetros de un modelo es el gradiente descendente, para ello se requiere diseñar una función de costo.

* Plantee la función de costo para el problema mencionado

La función de costo planteada para la regresión lineal es el error cuadrado medio (Mean Squared Errror) definida de esta manera:
```
def mse(a, b):
    return np.sum(np.square(b - a))/a.shape[0]
```
Consiste en promediar el valor de las (diferencias entre valor real y valor esperado) al cuadrado.  


* Aplique el gradiente descendente para encontrar los parámetros del modelo. Considere hacer normalización de los datos.

Inicialmente probaremos el resultado de aplicar el descenso de gradiente en los datos sin ajustar.

```

Starting weights: [1000.  500.] # Set arbitrarily
Starting MSE: 2819766538489.7344
Final weights: [266.77621149 492.15685172]
Final MSE: 77222387560.08604

```

![](linear_regression.png "linear_regression")

A continuación analizamos las diferencias al hacer el ejercicio usando los datos normalizados

