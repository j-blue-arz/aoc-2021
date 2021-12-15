import re
import collections
from itertools import *
from functools import reduce, cache
import more_itertools as more
import operator
import math
import heapq

from util import *

YEAR = 2021
DAY = 15

def solve(input: str):
    lines = input.splitlines()
    lines = [digits(line) for line in lines]
    grid = Grid(lines, cycle=True)
    target = Location(grid.height*5-1,grid.width*5-1)

    def value(loc):
        row, column = loc
        trow, tcol = row // grid.height, column // grid.width
        return ((grid[loc] + trow + tcol) - 1) % 9 + 1
    
    def is_inside(loc):
        row, column = loc
        return 0 <= row < grid.height*5 and 0 <= column < grid.width*5

    def dijkstra(start):
        done = set()
        distances = {start: 0}

        q = [(0, start)]

        while q:
            dist, node = heapq.heappop(q)
            if node in done:
                continue
            if node == target:
                return distances

            for neigh in [n for n in node.neighbors() if is_inside(n)]:
                neighdist = dist + value(neigh)
                if neigh not in distances or neighdist < distances[neigh]:
                    distances[neigh] = neighdist
                    heapq.heappush(q, (neighdist, neigh))
            done.add(node)
        
        return distances

    distances = dijkstra(Location(0, 0))
    return distances[target]


examples = [
r"""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""",r"""

""",r"""

""",r"""

""",r"""

""" 
]

if __name__ == "__main__":
    with_input = True
    run_with_examples_and_input(examples, solve, "Problem", with_input=with_input)