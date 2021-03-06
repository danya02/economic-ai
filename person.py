#!/usr/bin/python3
import logging
import actions
import random
import names
import place_map

class Person:
    def __init__(self, parents=None, real_biology=True):
        if parents is None:
            self.stats = {"strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 0}
            self.sex = random.randint(0, 1)
            self.name = names.generate_one_name(self.sex)
            self.surname = names.generate_one_surname()
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
        self.exhaustion_coefficient = lambda x: -x
        logging.info("A %s character named %s %s was created at point (%s,%s).", "male" if self.sex else "female", self.name, self.surname, str(self.x), str(self.y))
        logging.info("Attributes:")
        for i in self.stats:
            logging.info("%s: %s", i.capitalize(), str(self.stats[i]))

    def die(self, cause):
        logging.info("A character named %s %s died while at point (%s, %s). Cause of death: %s.", self.name, self.surname, str(self.x), str(self.y), cause)
        logging.info("Final attributes:")
        self.compute_satisfaction()
        for i in ["money", "satiation", "exhaustion", "satisfaction"]:
            logging.info("%s: %s", i.capitalize(), str(self.__getattribute__(i)))

    def __exit__(self):
        self.die("object destroyed by context manager")

    def act(self):
        self.select_target()
        if self.target is not None:
            if self.target[1] < self.y:
                actions.MoveNorth()(self)
            elif self.target[1] > self.y:
                actions.MoveSouth()(self)
            elif self.target[0] > self.x:
                actions.MoveEast()(self)
            elif self.target[0] < self.x:
                actions.MoveWest()(self)
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
            flag = False
            sat = 0
            for j in i.prerequisites:
                if self.__getattribute__(j) < i.prerequisites[j]:
                    flag = True
            if flag:
                continue
            try:
                sat += self.money_coefficient(self.money + i.delta["money"])
            except:
                sat += self.money_coefficient(self.money)
            try:
                sat += self.satiation_coefficient(self.satiation + i.delta["satiation"])
            except:
                sat += self.satiation_coefficient(self.satiation)
            try:
                sat += self.exhaustion_coefficient(self.exhaustion + i.delta["exhaustion"])
            except:
                sat += self.exhaustion_coefficient(self.exhaustion)
            if sat > max_sat:
                max_sat = sat
                max_act = i
        return max_sat, max_act

    def select_target(self):
        max_sat = 0
        max_sat_x = None
        max_sat_y = None
        for i, y in zip(place_map.map, range(len(place_map.map))):
            for j, x in zip(i, range(len(i))):
                a, b = self.compute_satisfaction_for_place(j)
                a -=self.exhaustion_coefficient(abs(self.x - j.x))
                a -= self.exhaustion_coefficient(abs(self.y - j.y))
                if a>max_sat:
                    max_sat = a
                    max_sat_x = x
                    max_sat_y = y
        if max_sat_x is None or max_sat_y is None:
            self.target = None
        else:
            self.target = (x, y, b)
            logging.debug("%s %s has chosen a target of (%s, %s)", self.name, self.surname, str(x), str(y))
