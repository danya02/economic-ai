#!/usr/bin/python3
import random
import places

is_biology_realistic = True # controls checks at creation of person

female = 0
male = 1

epoch = 0
people = []

o = places.Empty()
n = places.WallNorth()
e = places.WallEast()
s = places.WallSouth()
w = places.WallWest()
q = places.WallNorthWest()
z = places.WallSouthWest()
p = places.WallNorthEast()
m = places.WallSouthEast()

place_map = [
[q, n, n, n, n, n, n, p],
[w, o, o, o, o, o, o, e],
[w, o, o, o, o, o, o, e],
[w, o, o, o, o, o, o, e],
[w, o, o, o, o, o, o, e],
[w, o, o, o, o, o, o, e],
[w, o, o, o, o, o, o, e],
[z, s, s, s, s, s, s, m]]

def do_one_epoch():
    epoch += 1
    for i in people:
        i.select_target(place_map)
        i.act()
