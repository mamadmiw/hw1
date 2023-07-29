import tensorflow as tf
from tensorflow.keras import layers as ksl
class model:
  def __init__(self):
    self.inputShape=[784]
    self.net=None
  def buildModel(self):
    self.net=tf.keras.Sequential([ksl.Dense(256,activation='tanh',input_shape=self.inputShape),
                               ksl.Dense(128,activation='tanh'),#pish farz mishe [784]
                               ksl.Dense(64,activation='tanh'),
                               ksl.Dense(10,activation='softmax')

                               ])#tf.keras.layers.Dense
  def compileModel(self):
    tf.keras.utils.plot_model(self.net,show_shapes=True)
    self.net.summary()
    los=tf.keras.losses.CategoricalCrossentropy()
    optim=tf.keras.optimizers.SGD(learning_rate=0.01)
    self.net.compile(loss=los)