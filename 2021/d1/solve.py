import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math
from util import *

YEAR = 2021
DAY = 1

def solve1(input: str):
    lines = input.splitlines()
    return sum(b > a for a, b in pairwise(list(map(int, lines))))

def solve2(input: str):
    lines = input.splitlines()
    return sum(b + c + d > a + b + c for a, b, c, d in more.windowed(list(map(int, lines)), 4))

examples = [
r"""
199
200
208
210
200
207
240
269
260
263
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