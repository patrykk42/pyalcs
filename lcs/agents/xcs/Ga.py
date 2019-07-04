from .Constants import Constants
from .Random import Random

class GA:

    # --- PRIVATE ---

    @staticmethod
    def __select_offspring(self, action_set):

        if 0 < Constants.tau <= 1.0:
            return Random.tournament_selection(action_set, Constants.tau)
        else:
            return Random.roulette_wheel_selection(action_set)


    def __crossover(self):
        return "TODO"

    def __mutate(self):
        return "TODO"

    # --- PUBLIC ---

    def run(self):
        return "TODO"
