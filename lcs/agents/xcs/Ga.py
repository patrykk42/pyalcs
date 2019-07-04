from .Constants import Constants
from .Random import Random

class GA:

    # --- PRIVATE ---

    def __selectOffspring(self, action_set):
        targets = []

        for cl in action_set:
            targets.append(cl)

        fitnesses = []
        if 0 < Constants.tau <= 1.0:
            for cl in action_set:
                fitnesses.append((cl.fitness, cl.numerosity))
            selected = Random.tournament_selection(fitnesses, Constants.tau)
        else:
            for cl in action_set:
                fitnesses.append(cl.fitness)
            selected = Random.roulette_wheel_selection(fitnesses)

        return

    def __crossover(self):
        return "TODO"

    def __mutate(self):
        return "TODO"

    # --- PUBLIC ---

    def run(self):
        return "TODO"
