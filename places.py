#!/usr/bin/python3
import place
from actions import *

class Empty(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveEast(), MoveWest(), Pass()]

class WallNorth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveEast(), MoveWest(), Pass()]

class WallSouth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveEast(), MoveWest(), Pass()]

class WallEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveWest(), Pass()]

class WallWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveSouth(), MoveEast(), Pass()]

class WallNorthEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveWest(), Pass()]

class WallNorthWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), MoveEast(), Pass()]

class WallSouthEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveWest(), Pass()]

class WallSouthWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), MoveEast(), Pass()]

class DeadEndNorth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveNorth(), Pass()]

class DeadEndSouth(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveSouth(), Pass()]

class DeadEndEast(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveEast(), Pass()]

class DeadEndWest(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [MoveWest(), Pass()]

class TradePoint(place.Place):
    def _set_values(self):
        self.delta = {}
        self.prerequisites = {}
        self.actions = [TradeMoneyForSatiation(), Pass()]
