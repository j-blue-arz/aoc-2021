import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 11

result = 0
def flash(grid):
    flashed = set()
    total = 0

    def f(grid, r, c):
        nonlocal total
        nonlocal flashed
        total += 1
        flashed.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr = r+dr
                nc = c+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if not (r+dr, c+dc) in flashed:
                        grid[r+dr][c+dc] += 1
                        if grid[r+dr][c+dc] > 9:
                            f(grid, r+dr, c+dc)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 9 and (r, c) not in flashed:
                f(grid, r, c)
    return total, flashed

def solve1(input: str):
    lines = input.splitlines()
    result = 0
    grid = [digits(line) for line in lines]
    for j in range(100):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] += 1
                
        total, flashed = flash(grid)
        result += total
        for a, b in flashed:
            grid[a][b] = 0

    return result

def solve2(input: str):
    lines = input.splitlines()
    result = 0
    grid = [digits(line) for line in lines]
    for j in count(1):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] += 1
                
        total, flashed = flash(grid)
        if total == 100:
            return j
        result += total
        for a, b in flashed:
            grid[a][b] = 0


examples = [
r"""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526

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