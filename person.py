#!/usr/bin/python3
import actions
import random

class Person:
    def __init__(self, parents=None, real_biology=True):
        if parents is None:
            self.stats = {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 0}
            # TODO: Make name generation.
            self.name = ""
            # TODO: Make surname generation.
            self.surname = ""
            self.sex = random.choice([0, 1])
            self.x = 0
            self.y = 0
            for i in self.stats: # algorithm for generating attributes as used in D&D 5E
                d1 = random.randint(1, 6)
                d2 = random.randint(1, 6)
                d3 = random.randint(1, 6)
                d4 = random.randint(1, 6)
                self.stats[i] = sum([d1, d2, d3, d4]) - min(d1, d2, d3, d4)
        else:
            if not isinstance(parents, list):
                raise TypeError("Parents must be a list")
            if real_biology:
                if len(parents) != 2:
                    raise ValueError("There must be 2 parents (not "+str(len(parents))+")")
                if parents[0].sex == parents[1].sex:
                    raise ValueError("Parents must not have the same sex")
            parents_surnames = []
            parents_sexes = []
            # TODO: Choose a location for new person from location of parents.
            for i in parents:
                parents_surnames += [i.surname]
                parents_sexes += [i.sex]
            self.surname = random.choose(parents_surnames)
            self.sex = random.choice(parents_sexes)
        # TODO: Add more complex  gender identification not to annoy transgender users.
        self.gender = self.sex
        self.target = None
        self.satisfaction = 0
        self.money = 0
        self.money_coefficient = lambda x: x
        self.satiation = 0
        self.satiation_coefficient = lambda x: x
        self.exhaustion = 0
        self.exhaustion_coefficient = lambda x: x

    def act(self):
        if self.target is not None:
            if self.target[0] > self.x:
                actions.MoveNorth(self)
            elif self.target[0] < self.x:
                actions.MoveSouth(self)
            elif self.target[1] > self.y:
                actions.MoveWest(self)
            elif self.target[1] < self.y:
                actions.MoveEast(self)
            else:
                self.target[2](self)

    def compute_satisfaction(self):
        self.satisfaction = 0
        self.satisfaction += self.money_coefficient(self.money)
        self.satisfaction += self.satiation_coefficient(self.satiation)
        self.satisfaction += self.exhaustion_coefficient(self.exhaustion)

    def compute_satisfaction_for_place(self, place):
        max_sat = 0
        max_act = None
        for i in place.actions:
            sat = 0
            sat += self.money_coefficient(self.money + i.delta["money"])
            sat += self.satiation_coefficient(self.satiation + i.delta["satiation"])
            if sat > max_sat:
                max_sat = sat
                max_act = i
        return max_sat, max_act

    def select_target(self, place_map):
        max_sat = 0
        max_sat_x = None
        max_sat_y = None
        for i, y in zip(place_map, range(len(place_map))):
            for j, x in zip(i, range(len(place_map))):
                a, b = self.compute_satisfaction_for_place(j)
                a -=self.exhaustion_coefficient(abs(self.x - j.x))
                a -= self.exhaustion_coefficient(abs(self.y - j.y))
                if a>max_sat:
                    max_sat = a
                    max_sat_x = x
                    max_sat_y = y
        if max_sat_x is None or max_sat_y:
            self.target = None
        else:
            self.target = (x, y, b)
