import tensorflow.keras as keras
import tensorflow.keras.backend as K
import numpy as np
import matplotlib.pyplot as plt
import time

# Disables TensorFlow warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# MLP Hyper Parameters
batch_size = 128
epochs = 10

hidden_layers = 4
hidden_neurons = 1000

dropout_value = 0.2

# Processing Data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)


# Creating MLP
model = keras.Sequential()

model.add(keras.layers.Dense(hidden_neurons, activation=keras.activations.relu, input_dim=784))
model.add(keras.layers.Dropout(dropout_value))

for h_layers in range(hidden_layers - 1):
    model.add(keras.layers.Dense(hidden_neurons, activation=keras.activations.relu))
    model.add(keras.layers.Dropout(dropout_value))

model.add(keras.layers.Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])


# Training MLP
model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_data=(x_test, y_test))


# Testing MLP
for test_i in range(100):

    w = 10
    h = 10
    fig = plt.figure(figsize=(8, 8))
    columns = hidden_layers + 2
    rows = 1

    # Showing Input Data
    img = np.reshape(x_test[test_i], newshape=(28, 28))
    fig.add_subplot(rows, columns, 1)
    plt.imshow(img, cmap='gray')

    # Showing Hidden Layers
    for i in range(2, columns + 1):

        layer_i = (i - 2) * 2
        get_h_layer_output = K.function([model.layers[0].input], [model.layers[layer_i].output])

        test_array = np.array((x_test[test_i],))
        layer_output = get_h_layer_output([test_array, 0])[0]

        layer_img = np.reshape(layer_output, newshape=(layer_output.shape[1], layer_output.shape[0]))

        fig.add_subplot(rows, columns, i)
        plt.imshow(layer_img, cmap='gray')

    plt.show()







