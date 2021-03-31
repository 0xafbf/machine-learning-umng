# Andrés Botero
# 2021-03-24

# first neural network with keras tutorial
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

print("loading dataset")
dataset = np.loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

X = dataset[:, 0:8]
y = dataset[:, 8]


print("crating model")

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print("compiling model")
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print("fitting model")
model.fit(X, y, epochs=400, batch_size=10, verbose=0)

print("evaluating model")
_, accuracy = model.evaluate(X, y)
print("accuracy: %.2f" % accuracy)


print("making predictions")

predictions = model.predict_classes(X)

for i in range(5):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))



