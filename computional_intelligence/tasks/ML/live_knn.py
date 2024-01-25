import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from toolbox.knn import KNN


cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF']) # or ['r', 'b', 'g']

iris = datasets.load_iris()
X = iris.data[:,2:] # --> ['petal length (cm)', 'petal width (cm)']
y = iris.target
fname1 = iris.feature_names[2]
fname2 = iris.feature_names[3]


fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(X[:,0], X[:,1], c=y, cmap=cmap, edgecolors='k', s=20)
ax.set(xlabel=fname1, ylabel=fname2)
ax.legend(scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes")

knn = KNN(k=3)
knn.fit(X, y)

def onclick(event):
    predict = knn.priedicte([[event.xdata, event.ydata]])[0]
    new_X = np.vstack([X, [event.xdata, event.ydata]])
    new_y = np.append(y, predict)
    print('predict=%d, xdata=%f, ydata=%f' % (predict, event.xdata, event.ydata))
    plt.scatter(new_X[:,0], new_X[:,1], c=new_y, cmap=cmap, edgecolors='k', s=20)
    fig.canvas.draw()


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()