import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 17

def solve(input: str):
    fromx, tox, fromy, toy = ints(input)
    
    def inrange(x, y):
        return fromx <= x <= tox  and fromy <= y <= toy
    
    def abort(x, y):
        return y < fromy or x > tox
    
    maxy_global = 0
    
    def simulate(vlox, vloy):
        nonlocal maxy_global
        maxy = 0
        x, y = 0, 0
        a = []
        for _ in count():
            x += vlox
            y += vloy

            if vlox > 0:
                vlox -= 1
            elif vlox < 0:
                vlox += 1

            vloy -= 1
            maxy = max(y, maxy)
            if abort(x, y):
                return 0
            if inrange(x, y):
                maxy_global = max(maxy_global, maxy)
                return 1
    
    
    return sum(simulate(vlox, vloy) for vlox in range(0, 126) for vloy in range(-160,300)), maxy_global

examples = [
r"""
target area: x=20..30, y=-10..-5
""",r"""

""",r"""

""",r"""

""",r"""

""" 
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve, "Problem 1", with_input=with_input)