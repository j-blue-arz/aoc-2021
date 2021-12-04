import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 4

def check(marks):
    for row in range(marks.height):
        if all(marks[row, c] == True for c in range(marks.width)):
            return True
    for col in range(marks.width):
        if all(marks[r, col] == True for r in range(marks.height)):
            return True
    return False


def solve1(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0
    nums = ints(lines[0])
    fields = []
    marks = {}
    for num, batch in enumerate(batches[1:]):
        ls = [list(map(int, line.split())) for line in batch]
        fields.append((num+1, Grid(ls)))
        marks[num +1] = Grid(buffer=[False]*25, width=5)
    for num in nums:
        for f, field in fields:
            loc = field.locate(num)
            if loc:
                marks[f][loc[0]] = True
            if check(marks[f]):
                return num * sum(fie for fie, mark in zip(field.buffer, marks[f].buffer) if not mark)
    

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    nums = ints(lines[0])
    fields = []
    marks = {}
    for num, batch in enumerate(batches[1:]):
        ls = [list(map(int, line.split())) for line in batch]
        fields.append((num+1, Grid(ls)))
        marks[num +1] = Grid(buffer=[False]*25, width=5)
    wins = []
    won = []
    for num in nums:
        for f, field in fields:
            if f in won:
                continue
            loc = field.locate(num)
            if loc:
                marks[f][loc[0]] = True
            if check(marks[f]):
                wins.append(num * sum(fie for fie, mark in zip(field.buffer, marks[f].buffer) if not mark))
                won.append(f)
    
    return wins[-1]

examples = [
r"""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

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