import re
import collections
from itertools import *
from functools import reduce
from sys import _xoptions
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 8
# 6 2 5 5 4 5 6 3 7 6
digits = {
    1 : {2, 5} ,
    4 : {1, 2, 3, 5} ,
    2 : {0, 2, 3, 4, 6} ,
    3 : {0, 2, 3, 5, 6} ,
    5 : {0, 1, 3, 5, 6} ,
    0 : {0, 1, 2, 4, 5, 6} ,
    6 : {0, 1, 3, 4, 5, 6} ,
    9 : {0, 1, 2, 3, 5, 6} ,
    7 : {0, 2, 5} ,
    8 : {0, 1, 2, 3, 4, 5, 6} 
}

def solve1(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0
    for line in lines:
        u, f = line.split("|")
        result += sum(1 for w in f.split() if len(w) in [len(digits[d]) for d in [1, 4, 7, 8]])

    
    return result

def positions_to_digit(positions):
    return [digit for digit, p in digits.items() if p == positions][0]

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0
    for line in lines:
        u, f = line.split("|")
        postosignal = {}
        p25 = set([w for w in u.split() if len(w) == 2][0])
        p025 = set([w for w in u.split() if len(w) == 3][0])
        p1235 = set([w for w in u.split() if len(w) == 4][0])
        postosignal[0], = (p025 - p25)
        p0 = set(postosignal[0])

        l6s = [set(w) for w in u.split() if len(w) == 6]
        l5s = [set(w) for w in u.split() if len(w) == 5]
        p0156 = reduce(set.intersection, l6s)
        postosignal[6], = (p0156 - p025 - p1235)
        p0 = set(postosignal[0])
        p6 = set(postosignal[6])

        postosignal[5], = (p0156 - p0 - p6) & p025
        p5 = set(postosignal[5])

        postosignal[1], = p0156 - p5 - p6 - p0
        p1 = set(postosignal[1])
        for l5 in l5s:
            remain = l5 - p0 - p5 - p1 - p6
            if len(remain) == 1:
                postosignal[3], = remain
        p3 = set(postosignal[3])

        for l5 in l5s:
            remain = l5 - p0 - p5 - p3 - p6 - p1
            if len(remain) == 1:
                postosignal[2], = remain
        p2 = set(postosignal[2])

        postosignal[4], = {"a", "b", "c", "d", "e", "f", "g"} - p0 - p1 - p2 - p3 - p5 - p6

        number = 0
        for d in f.split():
            positions = set(pos for pos, signal in postosignal.items() if signal in d)
            number *= 10
            number += positions_to_digit(positions)
        result += number

    return result

examples = [
r"""
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce

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