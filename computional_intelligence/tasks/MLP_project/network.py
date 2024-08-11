import numpy as np
import scipy.io
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Activation function and its derivative
def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1 - np.tanh(x) ** 2

# Loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size

# Fully connected layer
class FCLayer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    def backward_propagation(self, output_error, learning_rate):
        input_error = np.dot(output_error, self.weights.T)
        weights_error = np.dot(self.input.T, output_error)

        self.weights -= learning_rate * weights_error
        self.bias -= learning_rate * output_error
        return input_error

# Activation layer
class ActivationLayer:
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

    def backward_propagation(self, output_error, learning_rate):
        return self.activation_prime(self.input) * output_error

# Neural network
class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        self.layers.append(layer)

    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    def predict(self, input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)

        return result

    def fit(self, x_train, y_train, epochs, learning_rate):
        samples = len(x_train)
        errors = []

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                err += self.loss(y_train[j], output)

                error = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)

            err /= samples
            errors.append(err)
            print('epoch %d/%d   error=%f' % (i + 1, epochs, err))

        plt.plot(range(1, epochs + 1), errors)
        plt.xlabel('Epochs')
        plt.ylabel('Error')
        plt.title('Training Progress')
        plt.show()

    def accuracy(self, X_test, y_test):
        predictions = self.predict(X_test)
        accuracy = calculate_accuracy(predictions, y_test)
        print('Accuracy on test set:', accuracy)

# Function to calculate accuracy
def calculate_accuracy(predictions, targets):
    predictions = np.squeeze(predictions)
    predictions = np.round(predictions)
    correct = np.sum(predictions == targets)
    total = len(targets)
    print("total test:", total, "correct:", correct)
    accuracy = correct / total 
    return accuracy

