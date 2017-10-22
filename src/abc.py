from food_sources import FoodSource
import pprint as pp


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
        self.fn_lb = fn_lb
        self.fn_ub = fn_ub

        self.employed_bees = round(npopulation * employed_bees_percentage)
        self.onlooker_bees = npopulation - self.employed_bees

    def optimize(self):
        self.initialize()
        pp.pprin(self.food_sources)

    def initialize(self):
        self.food_sources = [self.create_foodsource() for i in range(self.employed_bees)]

    def employed_bees_stage(self):
        pass

    def onlooker_bees_stage(self):
        pass

    def scout_bees_stage(self):
        pass

    def generate_solution(self, current_solution):
        pass

    def random_solution_excluding(self, excluded_index):
        pass

    def best_solution(self, new_solution, parent_solution):
        pass

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
        fitness self.fitness(solution)

        return FoodSource(solution, fitness)

    def candidate_solution(self, lb, ub):
        r = rand.random()
        solution = lb + (ub - lb) * r

        return solution
