#!/usr/bin/env python3
"""
Day 11: Cosmic Expansion

https://adventofcode.com/2023/day/11
"""
from enum import Enum
from typing import Any

from src.main.python.util import AbstractSolver


class Node(object):
    class Kind(Enum):
        Space = 0
        Galaxy = 1

    _prev_id = 0

    def __init__(self, kind: str) -> None:
        super().__init__()
        Node._prev_id += 1
        self.id = Node._prev_id
        if '.' == kind:
            self.kind = Node.Kind.Space
        else:
            self.kind = Node.Kind.Galaxy

    def __str__(self):
        return '.' if self.kind == Node.Kind.Space else '#'

    @staticmethod
    def _is_space(kind: 'Node.Kind') -> bool:
        return Node.Kind.Space == kind

    def is_space(self) -> bool:
        return self._is_space(self.kind)

    @staticmethod
    def _is_galaxy(kind: 'Node.Kind') -> bool:
        return Node.Kind.Galaxy == kind

    def is_galaxy(self) -> bool:
        return self._is_galaxy(self.kind)


class Grid(object):
    def __init__(self) -> None:
        super().__init__()
        self._grid = []

    def get_node(self, x: int, y: int) -> Node:
        return self._grid[y][x]

    def get_col(self, x: int) -> list[Node]:
        return [row[x] for row in self._grid]

    def get_row(self, y: int) -> list[Node]:
        return self._grid[y]

    def append(self, row: list[Node]) -> None:
        self._grid.append(row)

    def insert_empty_row(self, y: int) -> None:
        row = [Node('.') for i in range(len(self._grid[0]))]
        self._grid.insert(y, row)

    def insert_empty_col(self, x: int):
        for y in range(len(self._grid)):
            self._grid[y].insert(x, Node('.'))

    def expand_rows(self) -> None:
        empty_row_indexes = []
        for y in range(len(self._grid)):
            if all([n.is_space() for n in self._grid[y]]):
                empty_row_indexes.append(y)

        for i, y in enumerate(empty_row_indexes):
            self.insert_empty_row(i + y)

    def expand_cols(self) -> None:
        empty_col_indexes = []
        for x in range(len(self._grid[0])):
            if all(n.is_space() for n in self.get_col(x)):
                empty_col_indexes.append(x)

        for i, x in enumerate(empty_col_indexes):
            self.insert_empty_col(i + x)

    def expand_space(self) -> None:
        self.expand_rows()
        self.expand_cols()


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.grid = Grid()

    def init_data(self, data: list[str]) -> None:
        for line in data:
            row = []
            for c in line.strip():
                row.append(Node(kind=c))
            self.grid.append(row)
        self.grid.expand_space()

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        answer = 0

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
