import tensorflow as tf
tf.reset_default_graph()
from keras.layers import Dense, Activation
import keras


keras.applications.inception_v3.InceptionV3(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)