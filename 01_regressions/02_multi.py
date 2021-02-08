
import numpy as np
import pandas
import matplotlib.pyplot as plt
import sklearn.preprocessing as pre

def print_img(figure, name, alt_text = ""):
    slug = name.lower().replace(" ", "_")
    path = "%s.png" % slug
    figure.savefig(path)
    print("""![%s](%s "%s")""" % (alt_text, path, name))

    
np.set_printoptions(precision=5)
fig = plt.figure()

data = pandas.read_csv("kc_house_data.csv")
"""
['id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
'lat', 'long', 'sqft_living15', 'sqft_lot15']
"""
data_sample = data[:1000]

variables = data_sample[[
    "sqft_living", # can also be _lot or _above
    "floors",
    "bedrooms",
    "sqft_living",
]].values



scaler = pre.StandardScaler()
inputs = scaler.fit_transform(variables)

pre_prices = data_sample[["price"]].values
scaler2 = pre.StandardScaler()
prices = scaler2.fit_transform(pre_prices)

def calc_price(vars, in_weights):
    b = np.ones([vars.shape[0], 1])
    all_vars = np.append(vars, b, 1) # append 1 to have const multiplier
    return np.dot(all_vars, in_weights)



def mse(a, b):
    return np.sum(np.square(b - a))/a.shape[0]


def mse_from_projected_weights(in_weights):
    projection = calc_price(inputs, in_weights)
    return mse(prices, projection)


def grad(func, vars, offsets):
    num_vars = vars.shape[0]
    results = func(vars)
    #print("MSE:\t", np.format_float_scientific(results, 5))
    
    deltas = np.empty(num_vars)
    for idx in range(num_vars):
        vars2 = np.copy(vars)
        vars2[idx] += offsets[idx]
        results2 = func(vars2)
        deltas[idx] = results2 - results
    return deltas / offsets


weights = np.array([1, 1, 1, 1, 1], dtype=np.float64)
step = np.ones(5) * 0.0001
iters = 80

# print("W:\t", weights)
grad_result = grad(mse_from_projected_weights, weights, step)

errors = np.empty(iters)

for idx in range(iters):
    weights -= grad_result * step
    error = mse_from_projected_weights(weights)
    # print(idx, "W:\t", error, '\t', weights)
    errors[idx] = error
    grad_result = grad(mse_from_projected_weights, weights, step)


plt.plot(errors)

print("""

### Regresión multivariable:
Considere ahora que existe más de una característica para predecir el valor de la casa, ej. área, numero de habitaciones, años de construcción, etc. Así el modelo se convierte en:
```
y = A0 + A1 X1 + A2 X2 + ... + AnX
```

* ¿Cómo se plantearía la nueva función de costo teniendo en cuenta el nuevo conjunto de datos? realice la implementación
* Aplique el gradiente descendente para ajustar el modelo a los datos. Considere hacer normalicación de los datos.

""")

print_img(fig, "error de regresión multivariable")


