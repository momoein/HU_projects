import scipy.io
import numpy as np
from neural_network import MLP
from sklearn.model_selection import train_test_split

# load data
path = "D:\\work\\university\\Huni_projects\\computional_intelligence\\tasks\\ANNproject\\Data.mat"
mat = scipy.io.loadmat(path)
input_, target_ = mat["Input"], mat["Target"]

# fix data shape
fixed_shape_input = [[input_[0][i], input_[1][i]] for i in range(input_.shape[1])]
X = np.array(fixed_shape_input)
y = np.array(target_[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4321)

# net = MLP([2, 3, 1])
# out = net.feedforward(X_train[0])
# print(out)

# a = [1]
# b = [2,3]
# print(a+b)