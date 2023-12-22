#!/usr/bin/env python3
"""
Day 8: Haunted Wasteland

https://adventofcode.com/2023/day/8
"""
from collections import namedtuple
from typing import Any

from src.main.python.util import AbstractSolver

Node = namedtuple('Node', ['name', 'L', 'R'])


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.directions = None
        self.nodes = dict()

    def init_data(self, data: list[str]) -> None:
        for line in data:
            if not line.strip():
                continue
            elif not self.directions:
                self.directions = line
                continue
            name = line[:3]
            left = line[7:10]
            right = line[12:15]
            self.nodes[name] = Node(name=name, L=left, R=right)

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        done = False
        count = 0
        node = self.nodes['AAA']
        while not done:
            for step in self.directions:
                node = self.nodes[getattr(node, step)]
                count += 1
                if node.name == 'ZZZ':
                    done = True
                    break
        return count

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        return 0


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
