class FoodSource(object):
    trials = 0

    """docstring for FoodSource"""
    def __init__(self, initial_solution, initial_fitness):
        super(FoodSource, self).__init__()

        self.solution = initial_solution
        self.fitness = initial_fitness

    def __repr__(self):
        return f'<FoodSource s:{self.solution} f:{self.fitness} />'
