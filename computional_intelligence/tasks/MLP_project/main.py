import numpy as np
import scipy.io
from sklearn.model_selection import train_test_split
from neural_network import *


path = "D:\\work\\university\\Huni_projects\\computional_intelligence\\tasks\\MLP_project\\Data.mat"
mat = scipy.io.loadmat(path)
input_, target_ = mat["Input"], mat["Target"]

# fix data shape
fixed_shape_input = [[input_[0][i], input_[1][i]] for i in range(input_.shape[1])]
X = np.array(fixed_shape_input)
y = np.array(target_[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4321)

# X_train = np.array([[[-2.08796522, -4.4014648 ]],
#                     [[-0.63371396,  2.09373378]],
#                     [[ 2.69171633, -3.35786877]],
#                     [[-3.19845804,  4.52217065]],])

# y_train =np.array([ [[1]], [[-1]], [[-1]], [[-1]] ])

n = y_train.size
y_ = []
X_ = []
for i in range(n):
    y_tmp = np.array([[y_train[i]]])
    x_tmp = np.array([X_train[i]])
    y_.append(y_tmp)
    X_.append(x_tmp)
    
X_train = X_
y_train = y_
    


# network
net = Network()
net.add(FCLayer(2, 2))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(2, 1))
net.add(ActivationLayer(tanh, tanh_prime))

# train
net.use(mse, mse_prime)
net.fit(X_train, y_train, epochs=20, learning_rate=0.01)

# test
# out = net.predict(X_train)
# print(out)
