import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 16

def solve(input: str):
    B =  ""
    for c in input:
        b = bin(int(c, 16))[2:].zfill(4)
        B += b
    i = 0

    totalv = 0

    def get(length):
        nonlocal i
        if length > 0:
            result = B[i:i+length]
            i += length
            return result
    
    def geti(length):
        n = get(length)
        return int(n, 2)

    def parsenext():
        nonlocal totalv
        v = geti(3)
        totalv += v
        t = geti(3)
        if t == 4: # literal
            p = get(5)
            value = int(p[1:], 2)
            while p[0] == "1":
                p = get(5)
                value = value*16 + int(p[1:], 2)
            return value
        else: # operator
            lenid = geti(1)
            values = []
            if lenid == 0:
                l = geti(15)
                subpackage = i + l
                while i < subpackage:
                    values.append(parsenext())
            elif lenid == 1:
                l = geti(11)
                values = [parsenext() for _ in range(l)]
            match t:
                case 0:
                    return sum(values)
                case 1:
                    return math.prod(values)
                case 2:
                    return min(values)
                case 3:
                    return max(values)
                case 5:
                    return int(values[0] > values[1])
                case 6:
                    return int(values[0] < values[1])
                case 7:
                    return int(values[0] == values[1])
    
    return parsenext(), totalv

examples = [
r"""
C200B40A82
""",r"""
04005AC33890
""",r"""
880086C3E88112
""",r"""
CE00C43D881120
""",r"""
D8005AC2A8F0
""",r"""
F600BC2D8F
""",r"""
9C005AC2F8F0
""",r"""
9C0141080250320F1802104A08
"""
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve, "Problem", with_input=with_input)