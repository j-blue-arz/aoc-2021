import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math
from heapq import *
from queue import PriorityQueue

from util import *

YEAR = 2021
DAY = 6

def solve1(input: str):
    f = ints(input)
    for i in range(80):
        f += [9]*f.count(0)
        f = [a if a > 0 else 7 for a in f]
        f = [a - 1 for a in f]

    return len(f)

def solve2(input: str):
    f = ints(input)
    c = collections.Counter(f)
    for i in range(256):
        c[9] += c[0]
        c[7] += c[0]
        for i in range(10):
            c[i] = c[i+1]
    return sum(c.values())


examples = [
r"""
3,4,3,1,2
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