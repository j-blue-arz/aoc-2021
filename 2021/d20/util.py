from __future__ import annotations

import re
import typing

import more_itertools

T = typing.TypeVar("T")

class Grid(typing.Generic[T]):
    LocationType = typing.Iterable[int]

    def __init__(self, lines: typing.List[typing.List[T]] = None, buffer: typing.List[T] = None, width: int = None, height: int = None, cycle = False):
        if lines:
            self.width = len(lines[0])
            self.height = len(lines)
            self.buffer = list(more_itertools.flatten(lines))
        elif width and height:
            self.width = width
            self.height = height
            self.buffer = ["."] * width * height
        elif buffer and width:
            self.buffer = buffer
            self.width = width
            self.height = len(buffer) // width
        if self.width * self.height != len(self.buffer):
            raise Exception("size does not match content")
        self.cycle = cycle
    
    def __getitem__(self, location: LocationType) -> T:
        row, column = location
        if self.cycle:
            column = column % self.width
            row = row % self.height
        if row < 0 or row >= self.height:
            raise Exception(f"Out of bounds: row {row} is not in [0, {self.height})")
        if column < 0 or column >= self.width:
            raise Exception(f"Out of bounds: column {column} is not in [0, {self.width})")
        return self.buffer[row * self.width + column]
    
    def __setitem__(self, location, value):
        row, column = location
        self.buffer[row * self.width + column] = value
    
    def is_inside(self, location: LocationType):
        row, column = location
        return 0 <= row < self.height and 0 <= column < self.width

    def locate(self, item: T):
        return [(row, column) for row in range(self.height) for column in range(self.width) if self[row, column] == item]
    
    def __str__(self):
        lines = more_itertools.chunked(self.buffer, self.width)
        result = "\n".join("".join(map(str, line)) for line in lines)
        return result  

    def __repr__(self):
        return self.__str__()

DIRECTIONS_NESW = "NESW"

DIRECTION_TO_DELTA = {
    "N": [-1, 0],
    "E": [0, 1],
    "S": [1, 0],
    "W": [0, -1]
}

def add_iters(*iters: typing.Iterable) -> typing.Iterator:
    return (sum(a) for a in zip(*iters))

class Location(typing.Iterable[int]):
    def __init__(self, *coordinates):
        self._tuple = tuple(coordinates)
        self._d = len(self._tuple)
    
    def neighbors(self, directions = DIRECTIONS_NESW) -> typing.List[Location]:
        return [self + DIRECTION_TO_DELTA[direction] for direction in directions]

    def __add__(self, delta):
        return Location(*add_iters(self._tuple, delta))
    
    def __iter__(self):
        return self._tuple.__iter__()

    def __neg__(self):
        negated = (-d for d in self._tuple)
        return Location(*negated)

    def __eq__(self, other):
        return isinstance(self, type(other)) and \
            self._d == other._d and \
            all(a == b for a, b in zip(self._tuple, other._tuple))
    
    def __getitem__(self, x: int) -> int:
        return self._tuple[x]

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self._tuple.__hash__() 
    
    def __lt__(self, other):
        return self._tuple < other._tuple

    def __str__(self):
        return f"{self._tuple}"

    def __repr__(self):
        return self.__str__()

### conversion ###

def ints(s: str) -> typing.List[int]:
    return list(map(int, re.findall(r"-?\d+", s)))

def digits(s: str) -> typing.List[int]:
    return list(map(int, re.findall(r"\d", s)))

################### scaffolding #################################

#### input ####
def read_batches(input):
    batches = input.split("\n\n")
    return list(map(str.splitlines, batches))

#### running ####

def read_input():
    with open("input") as file:
        return file.read().strip()

def iterate_examples(example_strings):
    examples = list(map(str.strip, example_strings))
    while examples and not examples[-1]: examples.pop()
    return examples

def run_with_examples_and_input(examples, solver, title, with_input=True):
    print(title)
    for num, example in enumerate(iterate_examples(examples)):
        result = solver(example)
        if result is not None:
            print(f"Result example {num}:\n{result}")
            print("-"*10)
    if with_input:
        input = read_input()
        result = solver(input)
        if result is not None:
            print("-"*15)
            print(f"Result real:\n{result}")
        print("="*15)