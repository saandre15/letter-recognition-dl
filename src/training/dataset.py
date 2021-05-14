import pathlib
import os

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import Letter

IMG_WIDTH=8
IMG_HEIGHT=16
BATCH_SIZE=52152 - 1

letters = [None] * BATCH_SIZE
counter = 0

with open("sample/letter.data") as file:
  for line_num, line in enumerate(file):
    vals = line.split(" ")
    _output = vals[1]
    _input = [[None] * IMG_WIDTH] * IMG_HEIGHT

    for i in range(0, IMG_HEIGHT)
      for j in range(0, IMG_WIDTH)
        _input[i][j] = vals[(i * IMG_HEIGHT) + j + 6]
    
    letter = Letter(_input, _output)
    letters[counter] = letter;
    counter++


    
    
     
    