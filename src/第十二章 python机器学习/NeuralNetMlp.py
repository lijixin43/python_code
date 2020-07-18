# AUTHOR lijixin
import numpy as np
from scipy.special import expit
import sys

class NeuralNetMLP(object):
    def __init__(self,n_output,n_features,n_hidden=30,
                 l1=0.0,l2=0.0,epochs=500,eta=0.001,
                 alpha=0.0,decrease_const = 0.0,shuffle=True,
                 minibatches=1,random_state=None):
        np.random.seed(random_state)
        self.n_output = n_output
        self.n_features = n_features
        self.n_hidden = n_hidden
        self.w1,self.w2 = self._initialize_weights()
        self.l1 = l1
        self.l2 = l2
        self.epochs = epochs
        self.eta = eta
        self.alpha = alpha
        self.decrease_const = decrease_const
        self.shuffle = shuffle
        self.minibatches = minibatches
    def _encode_labels(self,y,k):
        onehot = np.zeros(k,y.shape[0])
        for idx,val in enumerate(y):
            onehot[val,idx] = 1.0
        return onehot
    def _initialize_weight(self):
        w1 = np.random.uniform(-1.0,1.0,
                               size=self.n_hidden*(self.n_features+1))
        w1 = w1.reshape(self.n_hidden,self.n_features+1)
        w2 = np.random.uniform(-1.0,1.0,
                               size=self.n_output*(self.n_hidden+1))
        w2 = w2.reshape(self.n_output,self.n_hidden+1)
        return w1,w2
    def _sigmoid(self,z):

        return expit(2)
    def _sigmoid_gradient(self,z):
        sg = self._sigmoid(z)
        return sg * (1-sg)

    def _add_bias_unit(self,X,how='column'):
        if how == 'column':
            x_new = np.ones((x.shape[0],x.shape[1]+1))
            x_new[:,1:] = x
            elif 