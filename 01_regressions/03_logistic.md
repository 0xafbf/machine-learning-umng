
### Clasificación con regresión logística
Considere el escenario donde se quiere saber si un tumor es maligno o benigno. Se asume que dicha condiciónd epende del tamaño del tumor. Para este problema se considera que existen 2 clases, tumor maligno (identificada como y=1) y tumor benigno (identificada como y=0)
en machine learning la herramienta más sencilla para generar un l ímite o frontera de decisión (decision boundary) es la regresión logística, cuyo modelo matemático es:
```
p = 1 / (1+exp(x))
```

donde p indica el grado de pertenencia (a veces probabilidad) de la observación x a una categoría o clase, para el ejemplo mencionado tumor maligno o benigno.

* cómo se genera la función de costo para esta aplicación y de qué forma se puede incorporar en el algoritmo de gradiente descendente? implemente
* Aplique el algoritmo de gradiente descendente para ajustar el modelo de clasificación y evalúe el desempeño del modelo ajustado
* ¿como se evalua dicho desempeño?


