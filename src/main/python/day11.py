#!/usr/bin/env python3
"""
Day 11: Cosmic Expansion

https://adventofcode.com/2023/day/11
"""
import itertools
from collections import namedtuple
from typing import Any

from src.main.python.util import AbstractSolver

Galaxy = namedtuple('Galaxy', ['gid', 'x', 'y'])


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.galaxies = []
        self.empty_cols = None
        self.empty_rows = None

    def init_data(self, data: list[str]) -> None:
        y = 0
        gid = 1
        self.empty_rows = list(range(len(data)))
        self.empty_cols = list(range(len(data[0])))
        self.galaxies.clear()
        for line in data:
            for x in [i for i, l in enumerate(line) if l == '#']:
                self.galaxies.append(Galaxy(gid=gid, x=x, y=y))
                gid += 1
                self.empty_rows.remove(y) if y in self.empty_rows else None
                self.empty_cols.remove(x) if x in self.empty_cols else None
            y += 1

    def expand_universe(self, factor: int) -> None:
        for i, g in enumerate(self.galaxies):
            k = sum([True for x in self.empty_cols if g.x >= x])
            self.galaxies[i] = Galaxy(gid=g.gid, x=g.x + (k * factor) - k,
                                      y=g.y)

        for i, g in enumerate(self.galaxies):
            k = sum([True for y in self.empty_rows if g.y >= y])
            self.galaxies[i] = Galaxy(gid=g.gid, x=g.x,
                                      y=g.y + (k * factor) - k)

    def sum_distances(self) -> int:
        answer = 0
        for g1, g2 in itertools.combinations(self.galaxies, 2):
            d = abs(g1.x - g2.x) + abs(g1.y - g2.y)
            answer += d
        return answer

    def solve_part_1(self, data: list[Any], **kwargs) -> Any:
        self.init_data(data)
        factor = kwargs['factor'] if 'factor' in kwargs else 2
        self.expand_universe(factor)
        return self.sum_distances()

    def solve_part_2(self, data: list[Any], **kwargs) -> Any:
        factor = kwargs['factor'] if 'factor' in kwargs else 1000000
        return self.solve_part_1(data, factor=factor)


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
