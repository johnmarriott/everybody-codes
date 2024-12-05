#!/usr/bin/env python

import fileinput

line = [line.strip() for line in fileinput.input()][0]

creature_potions_needed = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
    "x": 0,
}

for stride in range(1, 4):
    creature_groups = [line[i:i+stride] for i in range(0, len(line), stride)]

    potions_needed = 0

    for group in creature_groups:
        n_xs = group.count("x")
        extra_potions = max(0, stride - 1 - n_xs) * (stride - n_xs)
        creature_potions = sum([creature_potions_needed[creature] for creature in group])
        potions_needed += creature_potions + extra_potions
        
    print(f"for groups of {stride} creatures, {potions_needed} potions are needed")

