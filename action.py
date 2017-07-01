#!/usr/bin/puthon3
import person

class Action:
    def __init__(self):
        self.delta = {}
        self.prerequisites = {}
    def __call__(self, person_obj):
        assert(isinstance(person_obj, person.Person))
        for i in self.prerequisites:
            assert(self.prerequisites[i] <= person_obj.__getattribute__(i))
        for i in self.delta:
            person_obj.__setattr__(i, person_obj.__getattribute__(i)+self.delta[i])
