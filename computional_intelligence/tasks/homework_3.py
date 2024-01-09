from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from deap import base, creator, tools
import numpy as np
 

X, y = load_iris(return_X_y=True)

scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4321)

input_size = X.shape[1]
output_size = len(np.unique(y))
hidden_layer_size = (2, )


def create_classifier(ind):
    clf = MLPClassifier(hidden_layer_sizes=hidden_layer_size, 
                        activation="logistic", solver="sgd", 
                        max_iter=500, learning_rate_init=0.1
                        )
    clf.coefs_ = [np.array(ind[0]), np.array(ind[1])]
    clf.intercepts_ = [np.array(ind[2]), np.array(ind[3])]
    return clf



def evaluate(ind):
    clf = create_classifier(ind)
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return (accuracy, )



creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("weights", np.random.uniform, -1, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.weights, n=4 * (input_size * hidden_layer_size[0] + output_size))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxBlend, alpha=0.9)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evalute", evaluate)



if __name__ == "__main__":
    for i in range(1):
        population_size = 50
        generations = 100

        population = toolbox.population(n=population_size)
        best_individual = tools.selBest(population, k=1)[0]
        best_accuracy = evaluate(best_individual)

        # print("Best individual:", best_individual)
        print("Best Accuracy:", best_accuracy)