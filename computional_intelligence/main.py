# from tasks import live_knn

# live_knn()


from toolbox.linear_regression import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt
from sklearn import datasets
import numpy as np

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

fig = plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], y, color= "b", marker= "o", s= 30)
plt.show()

reg = LinearRegression(lr=0.01)
reg.fit(X_train, y_train)
predictions = reg.predict(X_test)

def mse(y_test, predictions):
    return np.mean((y_test - predictions)**2)

mes = mse(y_test, predictions)
print(mes)


y_pred_line = reg.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train, y_train, color= cmap(0.9), s= 10)
m1 = plt.scatter(X_train, y_train, color= cmap(0.9), s= 10) 
plt.plot(X, y_pred_line, color= "black")
plt.show()