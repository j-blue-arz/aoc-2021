import re
import collections
from itertools import *
from functools import reduce
import more_itertools as more
import operator
import math

from util import *

YEAR = 2021
DAY = 20

def solve1(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0
    mask = batches[0][0]

    grid = Grid(batches[1])

    def enhance(grid, border="0"):
        b = 2
        hb = b // 2
        newgrid = Grid(height = grid.height + b, width = grid.width + b)
        for row in range(-hb, grid.height+hb):
            for col in range(-hb, grid.width+hb):
                index = ""
                for drow in [-1, 0, 1]:
                    for dcol in [-1, 0, 1]:
                        if not grid.is_inside(Location(row + drow, col + dcol)):
                            index = index + border
                        else:
                            index = index + ("1" if (grid[row + drow, col + dcol] == "#") else "0")
                index = int(index, 2)
                newgrid[row+hb, col+hb] = mask[index]
        return newgrid

    for i in range(50):
        border = str(i % 2)
        grid = enhance(grid, border=border)

    result = 0
    for row in range(0, grid.height):
        for col in range(0, grid.width):
            result += grid[row , col] == "#"
    
    return result

def solve2(input: str):
    lines = input.splitlines()
    batches = read_batches(input)
    result = 0

    return result

examples = [
r"""
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
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