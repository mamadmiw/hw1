import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
from tensorflow.keras import layers as ksl
class utils:
  def __init__(self):
    #print("hi")
    #pass
    self.xTrain=None
    self.yTrain=None
    self.xTest=None
    self.yTest=None

  def loadData(self):
    mnist=tf.keras.datasets.mnist
    (self.xTrain,self.yTrain),(self.xTest,self.yTest)=mnist.load_data()
    #return xTrain....
  def plotSomeDate(self):
    idx=np.random.choice(60000,9)
    #imgs=self.xTrain[idx]
    imgs=self.xTrain[idx,:,:]
    _,axis=plt.subplots(3,3,figsize=[12,12])
    #return awli mohem nis
    axis=axis.flatten();
    for i,ax in enumerate(axis):

      ax.imshow(imgs[i])
    plt.show()

