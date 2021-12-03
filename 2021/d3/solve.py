import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 3

def solve1(input: str):
    lines = input.splitlines()
    gamma = 0
    eps = 0
    for i in range(len(lines[0])):
        gamma = gamma * 2
        eps = eps * 2
        gamma += sum(int(line[i]) for line in lines) > len(lines) // 2
        eps += sum(int(line[i]) for line in lines) < len(lines) // 2
        
    return gamma * eps

def solve2(input: str):
    lines = input.splitlines()
    a = lines[:]
    b = lines[:]
    for i in range(len(lines[0])):
        if len(a) > 1:
            most = int(sum(int(line[i]) for line in a) >= ((len(a) + 1) // 2))
            a = [line for line in a if int(line[i]) == most]
        if len(b) > 1:
            most = int(sum(int(line[i]) for line in b) >= ((len(b) + 1) // 2))
            b = [line for line in b if int(line[i]) != most]
    x = int(a[0], 2)
    y = int(b[0], 2)
    return x * y

examples = [
r"""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
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