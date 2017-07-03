#!/usr/bin/python3
import logging
import random
import places
import person
import place_map

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

is_biology_realistic = True # controls checks at creation of person

female = 0
male = 1

global epoch
epoch = 0
people = [person.Person()]
people[0].money = 100
people[0].money_coefficient = lambda x: x*2

o = places.Empty
n = places.WallNorth
e = places.WallEast
s = places.WallSouth
w = places.WallWest
q = places.WallNorthWest
z = places.WallSouthWest
p = places.WallNorthEast
m = places.WallSouthEast
a = places.TradePoint

map = [
[q, n, n, p],
[w, a, o, e],
[w, o, a, e],
[z, s, s, m]]

place_map.map = map

def parse_positions():
    for i, y in zip(place_map.map, range(len(place_map.map))):
        for j, x in zip(i, range(len(i))):
            place_map.map[x][y] = place_map.map[x][y]()
            place_map.map[x][y].x = x
            place_map.map[x][y].y = y

parse_positions()

def do_one_epoch():
    global epoch
    epoch += 1
    for i in people:
        i.act()
        i.compute_satisfaction()
    print("epoch:", epoch, " money:", people[0].money, " satiation:", people[0].satiation, " satisfaction:", people[0].satisfaction)
    input()

try:
    while 1:
        do_one_epoch()
except KeyboardInterrupt:
    for i in people:
        i.die("simulator closed")
