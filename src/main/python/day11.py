#!/usr/bin/env python3
"""
Day 11: Cosmic Expansion

https://adventofcode.com/2023/day/11
"""
import itertools
from collections import namedtuple
from typing import Any

from src.main.python.util import AbstractSolver

Galaxy = namedtuple('Galaxy', ['galaxy_id', 'x', 'y'])


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.galaxies = []

    def init_data(self, data: list[str]) -> None:
        y = 0
        galaxy_id = 1
        row_expand_indexes = list(range(len(data)))
        col_expand_indexes = list(range(len(data[0])))
        for line in data:
            for x in [i for i, l in enumerate(line) if l == '#']:
                self.galaxies.append(Galaxy(galaxy_id=galaxy_id, x=x, y=y))
                galaxy_id += 1
                row_expand_indexes.remove(y) if y in row_expand_indexes else None
                col_expand_indexes.remove(x) if x in col_expand_indexes else None
            y += 1

        for i, galaxy in enumerate(self.galaxies):
            k = sum([True for x in col_expand_indexes if galaxy.x >= x])
            self.galaxies[i] = Galaxy(galaxy_id=galaxy.galaxy_id, x=galaxy.x+k, y=galaxy.y)

        for i, galaxy in enumerate(self.galaxies):
            k = sum([True for y in row_expand_indexes if galaxy.y >= y])
            self.galaxies[i] = Galaxy(galaxy_id=galaxy.galaxy_id, x=galaxy.x, y=galaxy.y+k)

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        answer = 0
        for g1, g2 in itertools.combinations(self.galaxies, 2):
            d = abs(g1.x - g2.x) + abs(g1.y - g2.y)
            answer += d
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        answer = 0
        return answer


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
