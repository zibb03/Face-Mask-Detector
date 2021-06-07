import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([1, 2, 3])
y_data = np.array([2, 4, 6])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

model.compile(loss=tf.keras.losses.mean_squared_error,
              optimizer=tf.keras.optimizers.RMSprop(lr=0.1)
              )

history = model.fit(x_data, y_data, epochs=2000)

print(model.predict([4]))

plt.figure(0)
plt.plot(history.history['loss'])
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()
