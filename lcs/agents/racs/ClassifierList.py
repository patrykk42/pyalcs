from __future__ import annotations

import random
from itertools import chain
from typing import Optional, List

import lcs.agents.racs.components.alp as alp_racs
import lcs.strategies.anticipatory_learning_process as alp
import lcs.strategies.genetic_algorithms as ga
import lcs.strategies.reinforcement_learning as rl
from lcs import TypedList, Perception
from lcs.agents.racs import Configuration
from lcs.agents.racs.components.genetic_algorithm import mutate, crossover
from . import Classifier


class ClassifierList(TypedList):

    def __init__(self, *args) -> None:
        super().__init__((Classifier,), *args)

    def form_match_set(self, situation: Perception) -> ClassifierList:
        matching = [cl for cl in self if cl.condition.does_match(situation)]
        return ClassifierList(*matching)

    def form_action_set(self, action: int) -> ClassifierList:
        matching = [cl for cl in self if cl.action == action]
        return ClassifierList(*matching)

    def expand(self) -> List[Classifier]:
        """
        Returns an array containing all micro-classifiers

        Returns
        -------
        List[Classifier]
            list of all expanded classifiers
        """
        list2d = [[cl] * cl.num for cl in self]
        return list(chain.from_iterable(list2d))

    def get_maximum_fitness(self) -> float:
        """
        Returns the maximum fitness value amongst those classifiers
        that anticipated a change in environment.

        Returns
        -------
        float
            fitness value
        """
        anticipated_change_cls = [cl for cl in self
                                  if cl.does_anticipate_change()]

        if len(anticipated_change_cls) > 0:
            best_cl = max(anticipated_change_cls, key=lambda cl: cl.fitness)
            return best_cl.fitness

        return 0.0

    @staticmethod
    def apply_alp(population: ClassifierList,
                  match_set: ClassifierList,
                  action_set: ClassifierList,
                  p0: Perception,
                  action: int,
                  p1: Perception,
                  time: int,
                  theta_exp: int,
                  cfg: Configuration) -> None:

        new_list = ClassifierList()
        new_cl: Optional[Classifier] = None
        was_expected_case = False
        delete_counter = 0

        for cl in action_set:
            cl.increase_experience()
            cl.set_alp_timestamp(time)

            if cl.does_anticipate_correctly(p0, p1):
                new_cl = alp_racs.expected_case(cl, p0, time)
                was_expected_case = True
            else:
                new_cl = alp_racs.unexpected_case(cl, p0, p1, time)
                if cl.is_inadequate():
                    delete_counter += 1

                    lists = [x for x in [population, match_set, action_set]
                             if x]
                    for lst in lists:
                        lst.safe_remove(cl)

            if new_cl is not None:
                new_cl.tga = time
                alp.add_classifier(new_cl, action_set, new_list, theta_exp)

        # No classifier anticipated correctly - generate new one
        if not was_expected_case:
            new_cl = alp_racs.cover(p0, action, p1, time, cfg)
            alp.add_classifier(new_cl, action_set, new_list, theta_exp)

        # Merge classifiers from new_list into self and population
        action_set.extend(new_list)
        population.extend(new_list)

        if match_set is not None:
            new_matching = [cl for cl in new_list if
                            cl.condition.does_match(p1)]
            match_set.extend(new_matching)

    @staticmethod
    def apply_reinforcement_learning(action_set: ClassifierList,
                                     reward: int,
                                     p: float,
                                     beta: float,
                                     gamma: float) -> None:
        for cl in action_set:
            rl.update_classifier(cl, reward, p, beta, gamma)

    @staticmethod
    def apply_ga(time: int,
                 population: ClassifierList,
                 match_set: ClassifierList,
                 action_set: ClassifierList,
                 p: Perception,
                 theta_ga: int,
                 mu: float,
                 chi: float,
                 theta_as: int,
                 do_subsumption: bool,
                 theta_exp: int) -> None:

        if ga.should_apply(action_set, time, theta_ga):
            ga.set_timestamps(action_set, time)

            # Select parents
            parent1, parent2 = ga.roulette_wheel_selection(
                action_set, lambda cl: pow(cl.q, 3) * cl.num)

            child1 = Classifier.copy_from(parent1, time)
            child2 = Classifier.copy_from(parent2, time)

            # Execute mutation
            mutate(child1, mu)
            mutate(child2, mu)

            # Execute cross-over
            if random.random() < chi:
                if child1.effect == child2.effect:
                    crossover(child1, child2)

                    # Update quality and reward
                    child1.q = child2.q = float(sum([child1.q, child2.q]) / 2)
                    child2.r = child2.r = float(sum([child1.r, child2.r]) / 2)

            child1.q /= 2
            child2.q /= 2

            # We are interested only in classifiers with specialized condition
            unique_children = {cl for cl in [child1, child2]
                               if cl.condition.specificity > 0}

            ga.delete_classifiers(
                population, match_set, action_set,
                len(unique_children), theta_as)

            # check for subsumers / similar classifiers
            for child in unique_children:
                ga.add_classifier(child, p,
                                  population, match_set, action_set,
                                  do_subsumption, theta_exp)
