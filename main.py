import math

from matplotlib import pyplot as plt
from mealpy.swarm_based.ALO import OriginalALO


def fitness_function(arg):
    result = math.sin((arg[0] + arg[1])) + math.pow((arg[0] - arg[1]), 2) - 1.5 * arg[0] + 2.5 * arg[1] + 1

    return result


def draw_plot_worst(param):
    plt.figure()
    plt.xlabel("Epochs")
    plt.ylabel("worst values")
    plt.title("worst values in each epoch")
    plt.plot([i for i in range(len(param))], param)
    plt.savefig('worst.png')


if __name__ == '__main__':
    problem_dict1 = {
        "fit_func": fitness_function,
        "lb": [-1.5, -3],
        "ub": [4, 4],
        "minmax": "min",
    }

    epoch = 10
    pop_size = 50
    model = OriginalALO(epoch, pop_size)
    best_position, best_fitness = model.solve(problem_dict1)
    history = model.history
    positions = history.list_current_best
    worst = history.list_current_worst
    model.history.save_diversity_chart(filename="diversity")
    model.history.save_local_best_fitness_chart(filename="best")
    print(f"Solution: {best_position}, Fitness: {best_fitness}")
    #draw_plot_worst(worst)

