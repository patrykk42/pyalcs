from random import uniform, randrange, choice, choices


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Random(metaclass=Singleton):

    @staticmethod
    def next_double(lower=0, upper=1):
        return uniform(lower, upper)

    @staticmethod
    def next_int(lower, upper):
        return randrange(lower, upper)

    @staticmethod
    def choose_from(container):
        return choice(container) # return index instead?

    @staticmethod
    def roulette_wheel_selection(container):
        return choices(container, weights=container) # return index instead?

    @staticmethod
    def greedy_selection(container):
        max_val = max(container)
        
        max_elements = []
        for el in container:
            if el == max_val:
                max_elements.append(el)
            
        return choice(max_elements)

    @staticmethod
    def epsilon_greedy_selection(container, epsilon):
        if Random.next_double() < epsilon:
            return choice(container)
        else:
            return Random.greedy_selection(container)

    @staticmethod
    def tournament_selection(container, tau):
        best = choice(container)

        for el in container:
            if Random.next_double() < tau and best < el:
                best = el

        return best

    @staticmethod
    def tournament_selection_micro_classifier(container, tau):

        best = choice(container)
        best_val = best[0] / best[1]

        for el in container:
            if best_val < el[0] / el[1]:
                for i in range(0, el[1]): # repeat numerosity times
                    if Random.next_double() < tau:
                        best = el
                        best_val = best[0] / best[1]
                        break

        return best
