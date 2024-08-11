from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from deap import base, creator, tools
import numpy as np
 

X, y = load_iris(return_X_y=True)

scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4321)

input_size = X.shape[1]
output_size = len(np.unique(y))
hidden_layer_size = (2, )


def mlp_classifier(best):
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer_size, 
                        activation="logistic", solver="sgd", 
                        max_iter=500, learning_rate_init=0.1
                        )
    mlp.coefs_ = [np.array(best[0]), np.array(best[1])]
    mlp.intercepts_ = [np.array(best[2]), np.array(best[3])]
    return mlp



def evaluate(best):
    mlp = mlp_classifier(best)
    mlp.fit(X_train, y_train)
    accuracy = mlp.score(X_test, y_test)
    return (accuracy, )



creator.create("Fitness", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.Fitness)

toolbox = base.Toolbox()
toolbox.register("weights", np.random.uniform, -1, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.weights, n=1 * (input_size * hidden_layer_size[0] + output_size))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxBlend, alpha=0.9)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("evalute", evaluate)



if __name__ == "__main__":
    for i in range(1):
        pop_size = 75
        generations = 100

        population = toolbox.population(n=pop_size)
        best_individual = tools.selBest(population, k=1)[0]
        best_accuracy = evaluate(best_individual)

        # print("Best individual:", best_individual)
        print("Best Accuracy:", best_accuracy)