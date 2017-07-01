#!/usr/bin/python3
import place
from actions import *

class Empty(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveEast(), MoveWest()]

class WallNorth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveEast(), MoveWest()]

class WallSouth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveEast(), MoveWest()]

class WallEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveWest()]

class WallWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveEast()]

class WallNorthEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveWest()]

class WallNorthWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveEast()]

class WallSouthEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveWest()]

class WallSouthWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveEast()]

class DeadEndNorth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth()]

class DeadEndSouth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth()]

class DeadEndEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveEast()]

class DeadEndWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveWest()]

class TradePoint(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [TradeMoneyForSatiation()]
