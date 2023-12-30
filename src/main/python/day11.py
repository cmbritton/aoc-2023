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

    def print_universe(self):
        width = max(g.x for g in self.galaxies) + 1
        height = max(g.y for g in self.galaxies) + 1
        gid = 1
        for y in range(height):
            for x in range(width):
                g = Galaxy(gid, x, y)
                if g in self.galaxies:
                    print(gid, end='')
                    gid += 1
                else:
                    print('.', end='')
            print()

    def init_data(self, data: list[str]) -> None:
        y = 0
        gid = 1
        self.empty_rows = list(range(len(data)))
        self.empty_cols = list(range(len(data[0])))
        for line in data:
            for x in [i for i, l in enumerate(line) if l == '#']:
                self.galaxies.append(Galaxy(gid=gid, x=x, y=y))
                gid += 1
                self.empty_rows.remove(y) if y in self.empty_rows else None
                self.empty_cols.remove(x) if x in self.empty_cols else None
            y += 1

    def expand_universe(self, factor: int) -> None:
        # print(f'\nbefore:\n{self.print_universe()}')
        for i, g in enumerate(self.galaxies):
            k = sum([True for x in self.empty_cols if g.x >= x])
            j = 0 if factor == 1 else k
            self.galaxies[i] = Galaxy(gid=g.gid, x=g.x + (k * factor) - j, y=g.y)

        for i, g in enumerate(self.galaxies):
            k = sum([True for y in self.empty_rows if g.y >= y])
            j = 0 if factor == 1 else k
            self.galaxies[i] = Galaxy(gid=g.gid, x=g.x, y=g.y + (k * factor) - j)
        # print(f'\nafter:\n{self.print_universe()}')

    def sum_distances(self) -> int:
        answer = 0
        for g1, g2 in itertools.combinations(self.galaxies, 2):
            d = abs(g1.x - g2.x) + abs(g1.y - g2.y)
            answer += d
        return answer

    def solve_part_1(self, data: list[Any], **kwargs) -> Any:
        self.init_data(data)
        factor = kwargs['factor'] if 'factor' in kwargs else 1
        self.expand_universe(factor)
        return self.sum_distances()

    # 678626878094 is too high
    # 14985656 is too low

    def solve_part_2(self, data: list[Any], **kwargs) -> Any:
        factor = kwargs['factor'] if 'factor' in kwargs else 1000000
        return self.solve_part_1(data, factor=factor)


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
