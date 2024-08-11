import numpy as np
import scipy.io
from sklearn.model_selection import train_test_split
from network import *


# Load data
path = "D:\\work\\university\\Huni_projects\\computional_intelligence\\tasks\\MLP_project\\Data.mat"
mat = scipy.io.loadmat(path)
input_, target_ = mat["Input"], mat["Target"]

# Prepare data
"""
sample X input : np.array([
                           [[-2.08796522, -4.4014648 ]],
                           [[-0.63371396,  2.09373378]],
                           [[ 2.69171633, -3.35786877]],
                           [[-3.19845804,  4.52217065]],
                           ])
sample y input : np.array([ [[1]], [[-1]], [[-1]], [[-1]] ])
"""

fixed_shape_input = [[input_[0][i], input_[1][i]] for i in range(input_.shape[1])]
X = np.array(fixed_shape_input)
y = np.array(target_[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4321)

n = y_train.size
y_tmp = []
X_tmp = []
for i in range(n):
    y = np.array([[y_train[i]]])
    x = np.array([X_train[i]])
    y_tmp.append(y)
    X_tmp.append(x)

X_train = X_tmp
y_train = y_tmp



# Create and train network
net = Network()
net.add(FCLayer(2, 5))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(5, 1))
net.add(ActivationLayer(tanh, tanh_prime))

net.use(mse, mse_prime)
net.fit(X_train, y_train, epochs=25, learning_rate=0.001)
net.accuracy(X_test=X_test, y_test=y_test)
