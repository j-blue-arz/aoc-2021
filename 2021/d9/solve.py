import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 9

deltas = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def addd(a, b):
    return tuple(sum(c) for c in zip(a, b))

def digits(s):
    return list(map(int, s))

def solve1(input: str):
    lines = input.splitlines()
    
    lines = [digits(line) for line in lines]

    def is_inside(loc):
        row, column = loc
        return 0 <= row < len(lines) and 0 <= column < len(lines[0])

    def neighbors(r, c):
        return [addd((r, c), d) for d in deltas if is_inside(addd((r, c), d))]

    result = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if all(lines[neigh[0]][neigh[1]] > lines[r][c] for neigh in neighbors(r, c)):
                result += lines[r][c] + 1
    
    return result



def solve2(input: str):
    lines = input.splitlines()
    lines = [digits(line) for line in lines]

    def is_inside(loc):
        row, column = loc
        return 0 <= row < len(lines) and 0 <= column < len(lines[0])

    def neighbors(r, c):
        return [addd((r, c), d) for d in deltas if is_inside(addd((r, c), d))]

    def bfs(location):
        found = set()
        current = [location]
        while current:
            nextl = []
            for node in current:
                for child in neighbors(node[0], node[1]):
                    if child not in found and lines[child[0]][child[1]] > lines[node[0]][node[1]] and lines[child[0]][child[1]] != 9:
                        found.add(child)
                        nextl.append(child)
            current = nextl
        return found

    all_found = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if all(lines[neigh[0]][neigh[1]] > lines[r][c] for neigh in neighbors(r, c)):
                found = bfs((r, c))
                all_found.append(len(found) + 1)
    
    all_found.sort()
    return all_found[-1]*all_found[-2]*all_found[-3]


examples = [
r"""
2199943210
3987894921
9856789892
8767896789
9899965678
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