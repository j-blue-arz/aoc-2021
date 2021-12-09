import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 7

def solve1(input: str):
    a = ints(input)
    c = sum(a)
    for j in range(min(a), max(a)):
        m = sum(abs(x - j) for x in a)
        if m < c:
            c = m
    return c

def solve2(input: str):
    a = ints(input)
    c = sum(a)*sum(a)
    for j in range(min(a), max(a)):
        m = sum((abs(x - j)*(abs(x - j)+1))//2 for x in a)
        if m < c:
            c = m
    return c

examples = [
r"""
16,1,2,0,4,2,7,1,2,14
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