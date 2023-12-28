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


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.grid = []
        self.start = None

    def get_start_neighbors(self, node):
        assert node.is_start()
        if not node.neighbors:
            node.neighbors = []
            n_neighbor = self.grid[node.y - 1][node.x]
            if (self.get_neighbors(n_neighbor) and node in
                    self.get_neighbors(n_neighbor)):
                node.neighbors.append(n_neighbor)

            w_neighbor = self.grid[node.y][node.x - 1]
            if (self.get_neighbors(w_neighbor) and node in
                    self.get_neighbors(w_neighbor)):
                node.neighbors.append(w_neighbor)

            s_neighbor = self.grid[node.y + 1][node.x]
            if (self.get_neighbors(s_neighbor) and node in
                    self.get_neighbors(s_neighbor)):
                node.neighbors.append(s_neighbor)

            w_neighbor = self.grid[node.y][node.x + 1]
            if (self.get_neighbors(w_neighbor) and node in
                    self.get_neighbors(w_neighbor)):
                node.neighbors.append(w_neighbor)
        assert len(node.neighbors) == 2
        return node.neighbors

    def get_neighbors(self, node):
        if not node.neighbors:
            if node.is_n_s():
                node.neighbors = [self.grid[node.y - 1][node.x],
                                  self.grid[node.y + 1][node.x]]
            elif node.is_e_w():
                node.neighbors = [self.grid[node.y][node.x - 1],
                                  self.grid[node.y][node.x + 1]]
            elif node.is_n_e():
                node.neighbors = [self.grid[node.y - 1][node.x],
                                  self.grid[node.y][node.x + 1]]
            elif node.is_n_w():
                node.neighbors = [self.grid[node.y - 1][node.x],
                                  self.grid[node.y][node.x - 1]]
            elif node.is_s_w():
                node.neighbors = [self.grid[node.y + 1][node.x],
                                  self.grid[node.y][node.x - 1]]
            elif node.is_s_e():
                node.neighbors = [self.grid[node.y + 1][node.x],
                                  self.grid[node.y][node.x + 1]]
            elif node.is_start():
                node.neighbors = self.get_start_neighbors(node)
            elif node.is_ground():
                pass
            else:
                raise Exception(f'Unknown kind: {node.kind}')
        return node.neighbors

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
        curr = self.get_neighbors(prev)[0]
        while curr is not self.start:
            curr.distance = distance
            distance += 1
            if self.get_neighbors(curr)[0] != prev:
                prev = curr
                curr = self.get_neighbors(curr)[0]
            else:
                prev = curr
                curr = self.get_neighbors(curr)[1]

        distance = 1
        prev = self.start
        curr = self.get_neighbors(prev)[1]
        while curr is not self.start:
            distance += 1
            if distance < curr.distance:
                curr.distance = distance
            if self.get_neighbors(curr)[0] != prev:
                prev = curr
                curr = self.get_neighbors(curr)[0]
            else:
                prev = curr
                curr = self.get_neighbors(curr)[1]

        answer = 0
        prev = self.start
        curr = self.get_neighbors(prev)[0]
        while curr is not self.start:
            if curr.distance > answer:
                answer = curr.distance
            if self.get_neighbors(curr)[0] != prev:
                prev = curr
                curr = self.get_neighbors(curr)[0]
            else:
                prev = curr
                curr = self.get_neighbors(curr)[1]
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
