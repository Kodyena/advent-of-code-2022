import numpy as np
import matplotlib.pyplot as plt


def sign(x):
    if(x == 0):
        return 0
    if(x > 0):
        return 1
    if(x < 0):
        return -1

def drop_sand(start_point):
    sand = set()
    while True:
        current_point = start_point
        while True:
            for dir in (1j, -1 + 1j, 1 + 1j):
                point_changed = False
                if((new_point := current_point + dir) not in sand and new_point not in rocks):
                    current_point = new_point 
                    point_changed = True
                    break
            
            if current_point.imag > max_y + 1 or current_point.imag == 0:
                return sand

            if not point_changed:
                sand.add(current_point)
                break


lines = [[np.array([int(n) for n in coord.split(",")]) for coord in line.split("->")] for line in open("Day14\Data.txt").read().split("\n")]
rocks = set()
for rock_list in lines:
    for (ax, ay), (bx, by) in zip(rock_list, rock_list[1:]):
        rocks.update([ax + ay * 1j + i * ( sign(bx - ax) + sign(by - ay) * 1j ) for i in range(max([abs(bx - ax), abs(by - ay)]) + 1)])

max_y = int(max(rocks, key=lambda c: c.imag).imag)


settled_sand_one = drop_sand(500)
print("Answer to Q1: {}".format(len(settled_sand_one)))

for n in range(500):
    rocks.add(500 - n + (max_y + 2) * 1j)
    rocks.add(500 + n + (max_y + 2) * 1j)

settled_sand_two = drop_sand(500)
print("Answer to Q2: {}".format(len(settled_sand_two) + 1))