from pylab import *
import numpy as np 
from numpy import *
import mnist
images, labels = mnist.load_mnist('training', digits=np.arange([10]))
print np.shape(images)
print np.shape(labels)
#imshow(images[0], cmap=cm.gray)
#show()