import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 18

def explode(fishes):

    def explode_1(fishes, a):
        if isinstance(fishes[1], list):
            explode_1(fishes[1], a)
        else:
            fishes[1] += a

    def explode_0(fishes, a):
        if isinstance(fishes[0], list):
            explode_0(fishes[0], a)
        else:
            fishes[0] += a

    def explode_down(fishes, d):
        if isinstance(fishes, list):
            if d == 4:
                return True, True, fishes[0], fishes[1]
            else:
                for i, elem in enumerate(fishes):
                    exp, adjust, a, b = explode_down(elem, d+1)
                    if exp:
                        fishes[i] = 0
                    if adjust:
                        if i == 1 and a > 0:
                            if isinstance(fishes[0], list):
                                explode_1(fishes[0], a)
                            else:
                                fishes[0] += a
                            return False, True, 0, b
                        elif i == 0 and b > 0:
                            if isinstance(fishes[1], list):
                                explode_0(fishes[1], b)
                            else:
                                fishes[1] += b
                            return False, True, a, 0
                        else:
                            return False, True, a, b
        return False, False, 0, 0
    
    _, adj, _, _ = explode_down(fishes, 0)
    return adj

def split(fishes):
    if isinstance(fishes[0], list):
        if(split(fishes[0])):
            return True
    elif fishes[0] >= 10:
        fishes[0] = [fishes[0] // 2, (fishes[0]+1) // 2]
        return True
    if isinstance(fishes[1], list):
        if(split(fishes[1])):
            return True
    elif fishes[1] >= 10:
        fishes[1] = [fishes[1] // 2, (fishes[1]+1) // 2]
        return True
    return False

def magnitude(fishes):
    if isinstance(fishes, int):
        return fishes
    return 3 * magnitude(fishes[0]) + 2 * magnitude(fishes[1])

def reduce(fishes):
    a = True
    while a:
        a = explode(fishes)
        while a:
            a = explode(fishes)
        a = split(fishes)

def solve1(input: str):
    lines = input.splitlines()
    current = eval(lines[0])

    for line in lines[1:]:
        current = [current, eval(line)]
        reduce(current)
    
    return magnitude(current)

def solve2(input: str):
    lines = input.splitlines()
    maxsum = 0
    for a, b in permutations(lines, 2):
        c = [eval(a), eval(b)]
        reduce(c)
        maxsum = max(maxsum, magnitude(c))


    return maxsum

examples = [
r"""
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]

""",r"""

""" 
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve1, "Problem 1", with_input=with_input)
    run_with_examples_and_input(examples, solve2, "Problem 2", with_input=with_input)