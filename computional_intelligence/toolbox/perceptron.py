import numpy as np
import math


class P:
    def __init__(self, input_size, lr=1, epoch=10):
        self.W = np.zeros(input_size+1) # add one for bias
        self.epoch = epoch
        self.lr = lr
        
    def activation(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        z = self.W.T.dot(x)
        a = self.activation(z)
        return a
    
    def fit(self, X, d):
        for _ in range(self.epoch):
            for i in range(d.shape[0]):
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)



class Perceptron:
    def __init__(self, lr=0.01):
        """Parameters
        lr: learning rate 
        Xsize: input size 
        """
        self.W = None # np.zeros(1 + Xsize)
        self.lr: float = lr  # eta

    def output(self, z, func=None):
        """default activation function is tanh(z)"""
        if func is None:
            func = self.tanh(z)
        return func

    def sum(self, X):
        return np.dot(self.W[1:], X) + self.W[0]
    
    def error(self):
        pass

    # def cost(self, y, o):


    def tanh(self, z):
        return np.tanh(z)
    
    def sigmiod(self, z):
        return 1 / (1 + np.exp(-z))
    
    def sign(self, z):
        return np.sign(z)
    
    def linear(self, z):
        return z
    
    def relu(self, z):
        return z if z > 0 else 0





X = np.array([2, 3, 4])
W = np.array([1, 2, 3, 4])
W = np.array([1, 1, 3])

per = Perceptron()
per.W = W
# sum = per.sum(X)
# print(sum)

# print(np.zeros(1 + X.shape[0]))
s = [(X[i] - W[i])**2 for i in range(X.shape[0])]
print(np.sum(s) / 2)

