import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def priedicte(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        # compute the distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # get the closests k
        k_indices = np.argsort(distances)[:self.k] 
        k_nearest_labls = [self.y_train[i] for i in k_indices]
        
        # majority voye
        most_common =  Counter(k_nearest_labls).most_common()
        return most_common[0][0]

 

def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum(x1-x2)**2) 
    return distance
