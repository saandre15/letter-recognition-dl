import random

import tensorflow as tf
from tensorflow.python.keras.models import Model
from tensorflow.python.keras import layers
from tensorflow.python.keras import backend
from tensorflow.python.keras.optimizer_v2.adam import Adam
from tensorflow.python.keras.optimizer_v2.rmsprop import RMSprop
from tensorflow.python.keras.callbacks import TensorBoard

from dataset import IMG_HEIGHT, IMG_WIDTH, letters, BATCH_SIZE

backend.clear_session()

img_input = layers.Input(shape=(IMG_HEIGHT, IMG_WIDTH, 1))
x = layers.Conv2D(32, 3, activation="relu")(img_input)
x = layers.Conv2D(64, 3, activation="relu")(x)
x = layers.MaxPooling2D(2, 2)(x)
x = layers.Dropout(0.25)(x)
x = layers.Flatten()(x)
x = layers.Dense(128, activation="relu")(x)
x = layers.Dropout(0.5)(x)
output = layers.Dense(52, activation="softmax")(x)

model = Model(img_input, output)
model.compile(loss="categorical_cross",
  optimizer=Adam(),
  metrics=['accuracy'])

training_set=list(filter(lambda letter: random.random() < 0.6, letters))
validation_set=list(filter(lambda cur: random.random() < 0.05, map(lambda letter: (letter.input, letter.output), letters)))

model.fit(
  x=list(filter(lambda letter: letter.input, training_set)),
  y=list(filter(lambda letter: letter.outputAsInt(), training_set)),
  epochs=20,
  validation_data=validation_set,
  validation_steps=12
  verbose=2
)

model.save("basic-letter-recognition.h5")


