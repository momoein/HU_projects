import scipy.io
import numpy as np


path = "D:\\work\\university\\Huni_projects\\computional_intelligence\\tasks\\ANNproject\\Data.mat"
mat = scipy.io.loadmat(path)
input_, target_ = mat["Input"], mat["Target"]

fixed_shape_input = [[input_[0][i], input_[1][i]] for i in range(input_.shape[1])]
X = np.array(fixed_shape_input)
y = target_



class Perceptron:
    def __init__(self, input_size) -> None:
        self.input_size = input_size
        self.W = np.random.randn(input_size + 1)
        
    def get_net(self, inp): 
        net = np.dot(inp, self.W[1:]) + self.W[0]
        return net

    def activation(self, net): 
        """activation function"""
        return np.tanh(net)

    def activation_prim(self, net):
        return 1 - (np.tanh(net)**2)

    def feed(self, inp):
        net = self.get_net(inp)
        return self.activation(net)


class MLPClassifier_:
    def __init__(self, layer_size, hidden_size=1) -> None:
        self.hidden_size = hidden_size
        self.layer_size = layer_size
        self.hidden_layers = None
        self.output_layer = None

    def initial(self, X):
        hidden_layers = []
        for i in range(self.hidden_size):
            layer = [Perceptron(X.shape[1]) for j in range(self.layer_size)]
            hidden_layers.append(layer)
        #
        self.hidden_layers = np.array(hidden_layers)
        self.output_layer = Perceptron(self.layer_size)
    ...

    def __fit(self, x):
        inp = x
        for layer in self.hidden_layers:
            next_inp = []
            for neuron in layer:
                next_inp.append(neuron.feed(inp))
            inp = np.array(next_inp)

        out = self.output_layer.feed(inp)
        return out
    ...    

    def fit(self, X, y):
        if self.hidden_layers is None:
            self.initial(X)
        self.X_train = X
        self.y_train = y
        #
        y_pre = self.predict(X)
        error = self.loss_function(func=self.mse, y=y, y_pre=y_pre)
        print(error)

    ...

    def predict(self, X): 
        y_pre = np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            y_pre[i] = self.__fit(X[i])
        return y_pre
    ...

    def mse(self, y, y_pre):
        """return Mean Squared Error 1/m(sum((y - y_pre)**2)) """
        sub = np.subtract(y, y_pre)
        quadratic = np.power(sub, 2)
        sum = np.sum(quadratic)
        div = np.divide(sum, 2)
        return div
    ...

    def loss_function(self, func, y, y_pre):
        return func(y, y_pre)
    





mlp = MLPClassifier_(layer_size=2, hidden_size=1)
mlp.fit(X, y)
