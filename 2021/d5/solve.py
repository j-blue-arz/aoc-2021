import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 5

def solve1(input: str):
    lines = input.splitlines()
    points = collections.defaultdict(int)
    for line in lines:
        x0, y0, x1, y1 = ints(line)
        if x0 == x1:
            if y1 >= y0:
                for i in range(y0, y1+1):
                    points[(x0, i)] += 1
            else:
                for i in range(y1, y0+1):
                    points[(x0, i)] += 1
        if y0 == y1:
            if x0 >= x1:
                for i in range(x1, x0+1):
                    points[(i, y0)] += 1
            else:
                for i in range(x0, x1+1):
                    points[(i, y0)] += 1

    return sum(points[p] > 1 for p in points)



def solve2(input: str):
    lines = input.splitlines()
    points = collections.defaultdict(int)
    for line in lines:
        x0, y0, x1, y1 = ints(line)
        if x0 == x1:
            if y1 >= y0:
                for i in range(y0, y1+1):
                    points[(x0, i)] += 1
            else:
                for i in range(y1, y0+1):
                    points[(x0, i)] += 1
        if y0 == y1:
            if x0 >= x1:
                for i in range(x1, x0+1):
                    points[(i, y0)] += 1
            else:
                for i in range(x0, x1+1):
                    points[(i, y0)] += 1

        else:
            if y0 > y1 and x0 > x1:  
                for y, x in zip(range(y0, y1-1, -1), range(x0, x1-1, -1)):
                    points[(x, y)] += 1
            elif y1 > y0 and x1 > x0:
                for y, x in zip(range(y0, y1+1), range(x0, x1+1)):
                    points[(x, y)] += 1
            elif y1 > y0 and x0 > x1:
                for y, x in zip(range(y0, y1+1), range(x0, x1-1, -1)):
                    points[(x, y)] += 1
            elif y0 > y1 and x1 > x0:
                for y, x in zip(range(y0, y1-1, -1), range(x0, x1+1)):
                    points[(x, y)] += 1
    return sum(points[key] > 1 for key in points)
    

examples = [
r"""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2


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