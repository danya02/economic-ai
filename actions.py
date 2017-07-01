#!/usr/bin/python3
import action

class MoveNorth(action.Action):
    def __init__(self):
        self.delta = {"x": 0, "y": 1, "exhaustion":1}
        self.prerequisites = {}

class MoveSouth(action.Action):
    def __init__(self):
        self.delta = {"x": 0, "y": -1, "exhaustion":1}
        self.prerequisites = {}

class MoveEast(action.Action):
    def __init__(self):
        self.delta = {"x": 1, "y": 0, "exhaustion":1}
        self.prerequisites = {}

class MoveWest(action.Action):
    def __init__(self):
        self.delta = {"x": -1, "y": 0, "exhaustion":1}
        self.prerequisites = {}

class TradeMoneyForSatiation(action.Action):
    def __init__(self):
        self.delta = {"money": -1, "satiation": 1}
        self.prerequisites = {"money": 1}

class Pass(action.Action):
    def __init__(self):
        self.delta = {}
        self.prerequisites = {}
