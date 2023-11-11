import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from toolbox.knn import KNN


def test_knn():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1234)

    clf = KNN(k=3)
    clf.fit(X_train, y_train)
    predictions = clf.priedicte(X_test)

    acc = np.sum(predictions == y_test) / len(y_test )
    print(acc)
