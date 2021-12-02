import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math
from more_itertools.more import windowed

from more_itertools.recipes import triplewise

from util import *

YEAR = 2021
DAY = 2

def solve1(input: str):
    lines = input.splitlines()
    h, d = 0, 0
    for line in lines:
        c, s = line.split()
        if "forward" in c:
            h += int(s)
        if "down" in c:
            d += int(s)
        if "up" in c:
            d -= int(s)
    
    return h*d

def solve2(input: str):
    lines = input.splitlines()
    h, d = 0, 0
    aim = 0
    for line in lines:
        c, s = line.split()
        if "forward" in c:
            h += int(s)
            d += int(s)*aim
        if "down" in c:
            aim += int(s)
        if "up" in c:
            aim -= int(s)
    
    return h*d

examples = [
r"""
forward 5
down 5
forward 8
up 3
down 8
forward 2
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