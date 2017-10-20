
class ABC(object):
    """docstring for Colony"""

    food_sources = []
    
    def __init__(self,
        npopulation,
        nruns,
        fn_eval,
        *,
        trials_limit=50,
        employed_bees_percentage=0.5,
        fn_lb=[-5, -5],
        fn_ub=[5, 5],
    ):
        super(Colony, self).__init__()
        self.npopulation = npopulation
        self.nruns = nruns
        self.fn_eval = fn_eval
        self.trials_limit = trials_limit
        self.fn_lb = fn_lb
        self.fn_ub = fn_ub

        self.employed_bees = 0
        self.onlooker_bees = 0

    def optimize(self):
        pass

    def initialize(self):
        pass

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
        pass

    def selection(self, solutions, weights):
        pass

    def candidate_solution(self, lb, ub):
        pass
