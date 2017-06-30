#!/usr/bin/puthon3

class Action:
    def __init__(self):
        self.delta = {}
        self.prerequisites = {}
    def __call__(self, person):
        assert(isinstance(person, Person))
        for i in self.prerequisites:
            assert(self.prerequisites[i] <= person.__getattr__(i))
        for i in self.delta:
            person.__setattr__(i, person.__getattr__(i)+self.delta[i])
