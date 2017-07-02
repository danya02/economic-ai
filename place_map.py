#!/usr/bin/python3
import places

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
