
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def print_img(figure, name, alt_text = ""):
    slug = name.lower().replace(" ", "_")
    path = "%s.png" % slug
    figure.savefig(path)
    print("""![%s](%s "%s")""" % (alt_text, path, name))
    

data = pd.read_csv("kc_house_data.csv")

"""
['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
'lat', 'long', 'sqft_living15', 'sqft_lot15']
"""

data_sample = data[:5000]


areas = data_sample["sqft_living"] # can also be _lot or _above
prices = data_sample["price"]
    
print("""
Actividad práctica:
-------------------

### Regresión de una variable:
Considere el escenario de predecir el valor de una casa dependiendo del área. Adquiera o genere un dataset que represente el problema. Tomando como base la regresión lineal, se tiene que el valor de una casa es una función del área
```
y = A0 + A1*x
```
Donde y es el valor predicho y x es el área en metros cuadrados, el modelo lineal tiene los parámetros A0 y A1, el problema de Machine learning es encontrar los valores de los parámetros A0 y A1 que adapten el modelo a los datos.
""")

# this is just [vars.., 1] dot [in_weights]
def calc_price(vars, in_weights):
    b = np.ones([vars.shape[0], 1])
    all_vars = np.append(vars, b, 1) # append 1 to have const multiplier
    return np.dot(all_vars, in_weights)


print("""
      
En Machine Learning el método mas comúnmente aplicado para estimar los parámetros de un modelo es el gradiente descendente, para ello se requiere diseñar una función de costo.

* Plantee la función de costo para el problema mencionado

La función de costo planteada para la regresión lineal es el error cuadrado medio (Mean Squared Errror) definida de esta manera:
```
def mse(a, b):
    return np.sum(np.square(b - a))/a.shape[0]
```
Consiste en promediar el valor de las (diferencias entre valor real y valor esperado) al cuadrado.  
""")

def mse(a, b):
    return np.sum(np.square(b - a))/a.shape[0]



print("""
* Aplique el gradiente descendente para encontrar los parámetros del modelo. Considere hacer normalización de los datos.

Inicialmente probaremos el resultado de aplicar el descenso de gradiente en los datos sin ajustar.

```
""")

inputs = data_sample[["sqft_living"]].values

# first: plot base data
fig = plt.figure()
plt.plot(areas, prices, ".")

weights = np.array([1000., 500.])
print("Starting weights:", weights, "# Set arbitrarily")
projection = calc_price(inputs, weights)
plt.plot(areas, projection)


mse_at_start = mse(prices, projection)
print("Starting MSE:", mse_at_start)

# evaluates a function at vars and offsets, and returns its derivatives per component
def grad(func, vars, offsets = None):
    num_vars = vars.shape[0]
    if offsets == None:
        offsets = np.ones(num_vars)
        
    results = func(vars)
    # print(f" MSE: {results:e}")
    deltas = np.empty(num_vars)
    for idx in range(num_vars):
        vars2 = np.copy(vars)
        vars2[idx] += offsets[idx]
        results2 = func(vars2)
        deltas[idx] = results - results2
    return results, deltas / offsets


step = [1e-8, 1e-8]
step = [4e-8, 1e-6] # this converges in even less steps
gradient_step = [1e-3, 1e-3]
errors = [mse_at_start]
iters = 20
for idx in range(iters):
    # projection = calc_price(inputs, weights)
    rme_from_weights = lambda w: mse(prices, calc_price(inputs, w))
    next_rme, gradient = grad(rme_from_weights, weights, gradient_step)
    
    errors.append(next_rme)
    weights += gradient * step
    plt.plot(areas, calc_price(inputs, weights))

mse_at_end = mse(prices, calc_price(inputs, weights))
print("Final weights:", weights)
print("Final MSE:", mse_at_end)


print("""
```
""")
print_img(fig, "linear_regression")

print("""
A continuación analizamos las diferencias al hacer el ejercicio usando los datos normalizados
""")

import sklearn.preprocessing as pre
fig2 = plt.figure("with scaler")
def test_with_scaler(scaler_class):
    scaler = scaler_class()
    scaled_data = scaler.fit_transform(data_sample[["sqft_living", "price"]])

    print(scaled_data)
    
    scaled_inputs = scaled_data[:, 0:1]#"sqft_living"]
    scaled_prices = scaled_data[:, 1:2]#"price"]
    
    weights = np.array([1, 0], dtype=np.float64) # near to unit values
    projection = calc_price(scaled_inputs, weights)

    error = mse(scaled_prices, projection)
    print("Scaled starting MSE:", error)
    iters = 10
    step = [1e-5, 1e-5] # this converges in even less steps
    gradient_step = [1e-5, 1e-5]

    for idx in range(iters):
        rme_from_weights = lambda w: mse(scaled_prices, calc_price(scaled_inputs, w))
        current_rme, gradient = grad(rme_from_weights, weights, gradient_step)
        print("it:", idx, "\trme:", current_rme)
        print("gradient:", gradient);
        
        weights += gradient * step
        plt.plot(scaled_inputs[:,0], calc_price(scaled_inputs, weights))
        

test_with_scaler(pre.StandardScaler)

print_img(fig2, "with_scaler")
# todo later. . . check if scaling only inputs or only outputs would make things work better... or apply nonuniform (square, log) would change
