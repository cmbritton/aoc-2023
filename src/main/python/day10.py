#!/usr/bin/env python3
"""
Day 10: Pipe Maze

https://adventofcode.com/2023/day/10
"""
from typing import Any

from src.main.python.util import AbstractSolver


class Node(object):

    def __init__(self, x, y, kind) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.neighbors = None
        self.kind = kind
        self.distance = 0

    def __str__(self):
        return (f'''
{{
    "x": {self.x},
    "y": {self.y},
    "neighbors": {self.neighbors},
    "kind": "{self.kind}",
    "distance": {self.distance}
}}''')

    def is_n_s(self):
        return self.kind == '|'

    def is_e_w(self):
        return self.kind == '-'

    def is_n_e(self):
        return self.kind == 'L'

    def is_n_w(self):
        return self.kind == 'J'

    def is_s_w(self):
        return self.kind == '7'

    def is_s_e(self):
        return self.kind == 'F'

    def is_ground(self):
        return self.kind == '.'

    def is_start(self):
        return self.kind == 'S'

    def get_start_neighbors(self, grid):
        if not self.neighbors:
            self.neighbors = []
            if (grid[self.y - 1][self.x].get_neighbors(grid) and self in
                    grid[self.y - 1][self.x].get_neighbors(grid)):
                self.neighbors.append(grid[self.y - 1][self.x])
            if (grid[self.y][self.x - 1].get_neighbors(grid) and
                    self in grid[self.y][self.x - 1].get_neighbors(grid)):
                self.neighbors.append(grid[self.y][self.x - 1])
            if (grid[self.y + 1][self.x].get_neighbors(grid) and self
                    in grid[self.y + 1][self.x].get_neighbors(grid)):
                self.neighbors.append(grid[self.y + 1][self.x])
            if (grid[self.y][self.x + 1].get_neighbors(grid) and self
                    in grid[self.y][self.x + 1].get_neighbors(grid)):
                self.neighbors.append(grid[self.y][self.x + 1])
        assert len(self.neighbors) == 2
        return self.neighbors

    def get_neighbors(self, grid):
        if not self.neighbors:
            if self.is_n_s():
                self.neighbors = [grid[self.y - 1][self.x],
                                  grid[self.y + 1][self.x]]
            elif self.is_e_w():
                self.neighbors = [grid[self.y][self.x - 1],
                                  grid[self.y][self.x + 1]]
            elif self.is_n_e():
                self.neighbors = [grid[self.y - 1][self.x],
                                  grid[self.y][self.x + 1]]
            elif self.is_n_w():
                self.neighbors = [grid[self.y - 1][self.x],
                                  grid[self.y][self.x - 1]]
            elif self.is_s_w():
                self.neighbors = [grid[self.y + 1][self.x],
                                  grid[self.y][self.x - 1]]
            elif self.is_s_e():
                self.neighbors = [grid[self.y + 1][self.x],
                                  grid[self.y][self.x + 1]]
            elif self.is_start():
                self.neighbors = self.get_start_neighbors(grid)
            elif self.is_ground():
                pass
            else:
                raise Exception(f'Unknown kind: {self.kind}')
        return self.neighbors


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.grid = []
        self.start = None

    def init_data(self, data: list[str]) -> None:
        for y in range(len(data)):
            row = []
            for x in range(len(data[y])):
                node = Node(x, y, data[y][x])
                if node.is_start():
                    self.start = node
                row.append(node)
            self.grid.append(row)

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        distance = 1
        prev = self.start
        curr = prev.get_neighbors(self.grid)[0]
        while curr is not self.start:
            curr.distance = distance
            distance += 1
            if curr.get_neighbors(self.grid)[0] != prev:
                prev = curr
                curr = curr.get_neighbors(self.grid)[0]
            else:
                prev = curr
                curr = curr.get_neighbors(self.grid)[1]

        distance = 1
        prev = self.start
        curr = prev.get_neighbors(self.grid)[1]
        while curr is not self.start:
            distance += 1
            if distance < curr.distance:
                curr.distance = distance
            if curr.get_neighbors(self.grid)[0] != prev:
                prev = curr
                curr = curr.get_neighbors(self.grid)[0]
            else:
                prev = curr
                curr = curr.get_neighbors(self.grid)[1]

        answer = 0
        prev = self.start
        curr = prev.get_neighbors(self.grid)[0]
        while curr is not self.start:
            if curr.distance > answer:
                answer = curr.distance
            if curr.get_neighbors(self.grid)[0] != prev:
                prev = curr
                curr = curr.get_neighbors(self.grid)[0]
            else:
                prev = curr
                curr = curr.get_neighbors(self.grid)[1]
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
