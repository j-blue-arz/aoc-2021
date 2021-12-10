import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 10

def corrupt(line):
    q = collections.deque()
    for c in line:
        if c in "{[<(":
            q.append(c)
        else:
            m = q.pop()
            matches = {"(":")", "<":">", "[": "]", "{":"}"}
            if matches[m] != c:
                return True

def solve1(input: str):
    lines = input.splitlines()
    result = 0
    q = collections.deque()
    for line in lines:
        for c in line:
            if c in "{[<(":
                q.append(c)
            else:
                m = q.pop()
                matches = {"(":")", "<":">", "[": "]", "{":"}"}
                points = {")":3, ">":25137, "]":57, "}":1197}
                if matches[m] != c:
                    result += points[c]                    

    
    return result

def solve2(input: str):
    lines = input.splitlines()
    result = []
    q = collections.deque()
    for line in lines:
        score = 0
        if(corrupt(line)):
            continue
        for c in line:
            if c in "{[<(":
                q.append(c)
            else:
                m = q.pop()
        if q:
            while q:
                points = {"(":1, "<":4, "[":2, "{":3}
                score *= 5
                score += points[q.pop()]
            result.append(score)
    result.sort()
    return result[(len(result) - 1) // 2]

examples = [
r"""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]

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