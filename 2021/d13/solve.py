import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 13

def solve1(input: str):
    ds, folds = input.split("\n\n")
    dots = set()
    for dot in ds.splitlines():
        x, y = dot.split(",")
        dots.add((int(x), int(y)))
    for fold in folds.splitlines():
        c, pos = fold.split("=")
        c = c[-1]
        pos = int(pos)
        newdots = set()
        if c == "x":
            for dot in iter(dots):
                if dot[0] < pos:
                    newdots.add(dot)
                else:
                    newdots.add((dot[0] - (dot[0]-pos)*2, dot[1]))
        elif c == "y":
            for dot in iter(dots):
                if dot[1] < pos:
                    newdots.add(dot)
                else:
                    newdots.add((dot[0], dot[1] - (dot[1]-pos)*2))
        dots = newdots
    maxx, maxy = 0, 0
    for dot in dots:
        maxx = max(dot[0], maxx)
        maxy = max(dot[1], maxy)
    width = maxx + 1
    height = maxy + 1
    buffer = [" "] * width * height
    grid = Grid(buffer=buffer, width=width)
    for dot in dots:
        grid[(dot[1], dot[0])] = "#"
    return grid

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0

    return result

examples = [
r"""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""",r"""

""",r"""

""",r"""

""",r"""

""" 
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve1, "Problem 1", with_input=with_input)
    run_with_examples_and_input(examples, solve2, "Problem 2", with_input=with_input)