import re
import collections
from itertools import *
from functools import reduce, cache
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 12

def solve1(input: str):
    lines = input.splitlines()
    es = collections.defaultdict(list)
    for line in lines:
        a, b= line.split("-")
        es[a].append(b)
        es[b].append(a)

    def d(r, visited):
        if r == "end":
            return 1
        sum = 0
        for child in es[r]:
            if child.isupper() or child not in visited:
                sum += d(child, visited + (child,))
        return sum

    return d("start", ("start", ))

def solve2(input: str):
    lines = input.splitlines()
    es = collections.defaultdict(list)
    for line in lines:
        a, b= line.split("-")
        es[a].append(b)
        es[b].append(a)

    def d(r, visited, twice):
        if r == "end":
            return 1
        sum = 0
        for child in es[r]:
            if child.isupper() or child not in visited:
                sum += d(child, visited + (child,), twice)
            elif twice and visited.count(child) < 2:
                sum += d(child, visited + (child,), False)
        return sum

    return d("start", ("start", "start"), True)

examples = [
r"""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
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