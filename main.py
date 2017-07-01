#!/usr/bin/python3
import random
import places
import person

is_biology_realistic = True # controls checks at creation of person

female = 0
male = 1

global epoch
epoch = 0
people = [person.Person()]
people[0].money = 100
people[0].money_coefficient = lambda x: x*2

a = places.TradePoint()

place_map = [[a]]

def do_one_epoch():
    global epoch
    epoch += 1
    for i in people:
        i.select_target(place_map)
        i.act()
        i.compute_satisfaction()
    print("epoch:", epoch, " money:", people[0].money, " satiation:", people[0].satiation, " satisfaction:", people[0].satisfaction)
    input()

while 1:
    do_one_epoch()
