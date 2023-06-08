import math

from mealpy.swarm_based.ALO import OriginalALO


def fitness_function(arg):
    result = math.sin((arg[0] + arg[1])) + math.pow((arg[0] - arg[1]), 2) - 1.5 * arg[0] + 2.5 * arg[1] + 1

    return result


if __name__ == '__main__':
    problem_dict1 = {
        "fit_func": fitness_function,
        "lb": [-1.5, -3],
        "ub": [4, 4],
        "minmax": "min",
    }

    epoch = 1000
    pop_size = 50
    model = OriginalALO(epoch, pop_size)
    best_position, best_fitness = model.solve(problem_dict1)
    print(f"Solution: {best_position}, Fitness: {best_fitness}")
    print("g")

"""
    The original version of: Ant Lion Optimizer (ALO)

    Links:
        1. https://www.mathworks.com/matlabcentral/fileexchange/49920-ant-lion-optimizer-alo
        2. https://dx.doi.org/10.1016/j.advengsoft.2015.01.010

    Examples
    ~~~~~~~~
    >>> import numpy as np
    >>> from mealpy.swarm_based.ALO import OriginalALO
    >>>
    >>> def fitness_function(solution):
    >>>     return np.sum(solution**2)
    >>>
    >>> problem_dict1 = {
    >>>     "fit_func": fitness_function,
    >>>     "lb": [-10, -15, -4, -2, -8],
    >>>     "ub": [10, 15, 12, 8, 20],
    >>>     "minmax": "min",
    >>> }
    >>>
    >>> epoch = 1000
    >>> pop_size = 50
    >>> model = OriginalALO(epoch, pop_size)
    >>> best_position, best_fitness = model.solve(problem_dict1)
    >>> print(f"Solution: {best_position}, Fitness: {best_fitness}")

    References
    ~~~~~~~~~~
    [1] Mirjalili, S., 2015. The ant lion optimizer. Advances in engineering software, 83, pp.80-98.
    """
