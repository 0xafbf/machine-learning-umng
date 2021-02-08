
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def print_img(figure, name, alt_text = ""):
    slug = name.lower().replace(" ", "_")
    path = "%s.png" % slug
    figure.savefig(path)
    print("""![%s](%s "%s")""" % (alt_text, path, name))
    

    
print("""
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
* Aplique el gradiente descendente para encontrar los parámetros del modelo. Considere hacer normalización de los datos.
* ¿Cuál es el metodo idóneo con el que se normalizan los datos?

""")


    
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

# some sane defaults
weights = np.array([1000., 500.])


def calc_price(vars, in_weights):
    b = np.ones([vars.shape[0], 1])
    all_vars = np.append(vars, b, 1) # append 1 to have const multiplier
    return np.dot(all_vars, in_weights)

inputs = np.array(areas).reshape([-1, 1])

projected_price = calc_price(inputs, weights)

fig = plt.figure()

plt.plot(areas, prices, ".")
plt.plot(areas, projected_price)

def mse(a, b):
    return np.sum(np.square(b - a))/a.shape[0]

print("mse", mse(prices, projected_price))

def mse_from_projected_weights(in_weights, plot=False):
    projection = calc_price(inputs, in_weights)
    if plot:
        plt.plot(areas, projection)
    return mse(prices, projection)


def grad(func, vars, offsets = None):
    num_vars = vars.shape[0]
    if offsets == None:
        offsets = np.ones(num_vars)
        
    results = func(vars, True) # true to plot
    # print(f" MSE: {results:e}")
    deltas = np.empty(num_vars)
    for idx in range(num_vars):
        vars2 = np.copy(vars)
        vars2[idx] += offsets[idx]
        results2 = func(vars2)
        deltas[idx] = results - results2
    return deltas

# print("  w:", weights)
grad_result = grad(mse_from_projected_weights, weights)
# print("grad:", grad_result)

step = [1e-8, 1e-8]
step = [4e-8, 1e-6] # this converges in even less steps
coarse_iters = 50
for idx in range(coarse_iters):
    weights += grad_result * step
    # print(idx, " w:\t", weights)
    grad_result = grad(mse_from_projected_weights, weights)
    # print("grad:", grad_result)

print("mse after", mse_from_projected_weights(weights))

print_img(fig, "linear_regression")


