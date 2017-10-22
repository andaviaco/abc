from food_source import FoodSource
import numpy as np
import pprint as pp
import random as rand


class ABC(object):
    """docstring for ABC"""

    food_sources = []

    def __init__(
        self,
        npopulation,
        nruns,
        fn_eval,
        *,
        trials_limit=50,
        employed_bees_percentage=0.5,
        fn_lb=[-5, -5],
        fn_ub=[5, 5],
    ):
        super(ABC, self).__init__()
        self.npopulation = npopulation
        self.nruns = nruns
        self.fn_eval = fn_eval
        self.trials_limit = trials_limit
        self.fn_lb = np.array(fn_lb)
        self.fn_ub = np.array(fn_ub)

        self.employed_bees = round(npopulation * employed_bees_percentage)
        self.onlooker_bees = npopulation - self.employed_bees

    def optimize(self):
        self.initialize()
        pp.pprint(self.food_sources)

        for nrun in range(1, self.nruns+1):
            self.employed_bees_stage()

        pp.pprint(self.food_sources)

    def initialize(self):
        self.food_sources = [self.create_foodsource() for i in range(self.employed_bees)]

    def employed_bees_stage(self):
        for i in range(self.employed_bees):
            food_source = self.food_sources[i]
            new_solution = self.generate_solution(i)
            best_solution = self.best_solution(food_source.solution, new_solution)

            if np.array_equal(best_solution, food_source.solution):
                food_source.trials += 1
            else:
                food_source.solution = best_solution
                food_source.trials = 0

    def onlooker_bees_stage(self):
        pass

    def scout_bees_stage(self):
        pass

    def generate_solution(self, current_solution_index):
        solution = self.food_sources[current_solution_index].solution
        k_source_index = self.random_solution_excluding([current_solution_index])
        k_solution = self.food_sources[k_source_index].solution
        d = rand.randint(0, len(self.fn_lb) - 1)
        r = rand.uniform(-1, 1)

        new_solution = np.copy(solution)
        new_solution[d] = solution[d] + r * (solution[d] - k_solution[d])

        return new_solution

    def random_solution_excluding(self, excluded_index):
        available_indexes = set(range(self.employed_bees))
        exclude_set = set(excluded_index)
        diff = available_indexes - exclude_set
        selected = rand.choice(list(diff))

        return selected

    def best_solution(self, current_solution, new_solution):
        if self.fitness(new_solution) > self.fitness(current_solution):
            return new_solution
        else:
            return current_solution

    def probability(self, solution_fitness):
        pass

    def fitness(self, solution):
        result = self.fn_eval(solution)

        if result >= 0:
            fitness = 1 / (1 + result)
        else:
            fitness = abs(result)

        return fitness

    def selection(self, solutions, weights):
        pass

    def create_foodsource(self):
        solution = self.candidate_solution(self.fn_lb, self.fn_ub)
        fitness = self.fitness(solution)

        return FoodSource(solution, fitness)

    def candidate_solution(self, lb, ub):
        r = rand.random()
        solution = lb + (ub - lb) * r

        return solution
