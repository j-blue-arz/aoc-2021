import re
import collections
from itertools import *
from functools import reduce
from typing import Counter
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 14

def solve1(input: str):
    lines = input.splitlines()
    start = lines[0]
    replace = {}
    for line in lines[2:]:
        f, t = line.split(" -> ")
        replace[f] = t
    occ = collections.defaultdict(int)
    for a, b in pairwise(start):
        occ[a+b] += 1
    for _ in range(40):
        newocc = collections.defaultdict(int)
        for s in occ.keys():
            a, b = s[0], s[1]
            c = replace[a+b]
            newocc[a + c] += occ[s]
            newocc[c + b] += occ[s]
        occ = newocc
    c = collections.Counter()
    
    for s in occ.keys():
        c[s[0]] += occ[s]
        c[s[1]] += occ[s]
    c[lines[0][0]] += 1
    c[lines[0][-1]] += 1
    for s in c.keys():
        c[s] = c[s] // 2
    g = c.most_common()
    return g[0][1] - g[-1][1]

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0

    return result

examples = [
r"""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
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