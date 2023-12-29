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
        self.distance = -1
        self.is_inside = None

    def __str__(self):
        return (f'''
{{
    "x": {self.x},
    "y": {self.y},
    "neighbors": {self.neighbors},
    "kind": "{self.kind}",
    "distance": {self.distance},
    "is_inside": {self.is_inside}
}}''')

    @staticmethod
    def _is_n_s(kind):
        return kind == '|'

    def is_n_s(self):
        return self._is_n_s(self.kind)

    @staticmethod
    def _is_e_w(kind):
        return kind == '-'

    def is_e_w(self):
        return self._is_e_w(self.kind)

    @staticmethod
    def _is_n_e(kind):
        return kind == 'L'

    def is_n_e(self):
        return self._is_n_e(self.kind)

    @staticmethod
    def _is_n_w(kind):
        return kind == 'J'

    def is_n_w(self):
        return self._is_n_w(self.kind)

    @staticmethod
    def _is_s_w(kind):
        return kind == '7'

    def is_s_w(self):
        return self._is_s_w(self.kind)

    @staticmethod
    def _is_s_e(kind):
        return kind == 'F'

    def is_s_e(self):
        return self._is_s_e(self.kind)

    @staticmethod
    def _is_ground(kind):
        return kind == '.'

    def is_ground(self):
        return self._is_ground(self.kind)

    @staticmethod
    def _is_start(kind):
        return kind == 'S'

    def is_start(self):
        return self._is_start(self.kind)

    def is_main_loop(self):
        return self.distance >= 0 or self.is_start()

    def get_box_char(self):
        if self.is_main_loop():
            if self.is_s_e():
                return '┌'
                # return '┏'
            elif self.is_e_w():
                return '─'
                # return '━'
            elif self.is_s_w():
                return '┐'
                # return '┓'
            elif self.is_n_s():
                return '│'
                # return '┃'
            elif self.is_n_w():
                return '┘'
                # return '┛'
            elif self.is_n_e():
                return '└'
                # return '┗'
            elif self.is_start():
                return 'S'
        elif self.is_inside is None:
            return '.'
        elif self.is_inside:
            return 'I'
        else:
            return 'O'

    def negates_prev_vertex(self, prev_kind):
        return (Node._is_s_e(prev_kind) and self.is_s_w()
                or Node._is_n_e(prev_kind) and self.is_n_w())

    def is_vertex(self):
        return (self.is_main_loop() and not self.is_e_w()
                and not self.is_n_s() and not self.is_start()
                and not self.is_ground())


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.grid = []
        self.start = None

    def print_grid(self):
        print()
        print('  ', end='')
        for i in range(len(self.grid[0])):
            if i > 0 and i % 10 == 0:
                print(int(i / 10), end='')
            else:
                print(' ', end='')
        print()
        print('  ', end='')
        for i in range(len(self.grid[0])):
            print(i % 10, end='')
        print()
        print(' +', end='')
        for i in range(len(self.grid[0])):
            print('-', end='')
        print()
        for y in range(len(self.grid)):
            print(f'{y % 10}|', end='')
            for x in range(len(self.grid[y])):
                print(f'{self.grid[y][x].get_box_char()}', end='')
            print()

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

    def is_node_inside_loop(self, src_node):
        if src_node.is_main_loop():
            src_node.is_inside = False
            return False
        elif src_node.x == 0 or src_node.x == len(self.grid[0]) - 1:
            src_node.is_inside = False
            return False
        elif (self.grid[src_node.y][src_node.x - 1].is_inside is not None
              and not self.grid[src_node.y][src_node.x - 1].is_inside):
            src_node.is_inside = False
            return False
        elif (self.grid[src_node.y][src_node.x + 1].is_inside is not None
              and not self.grid[src_node.y][src_node.x + 1].is_inside):
            src_node.is_inside = False
            return False
        elif (src_node.y > 0
              and not self.grid[src_node.y - 1][src_node.x].is_main_loop()
              and not self.grid[src_node.y - 1][src_node.x].is_inside):
            src_node.is_inside = False
            return False

        crossing_count = 0
        prev_vertex = None
        for x in range(src_node.x, len(self.grid[0])):
            curr_node = self.grid[src_node.y][x]
            prev_node = self.grid[src_node.y][x - 1] if x > 0 else None
            if curr_node.is_main_loop():
                if prev_node.is_main_loop():
                    if curr_node.is_vertex() or curr_node.is_start():
                        if prev_vertex is not None:
                            if not curr_node.negates_prev_vertex(prev_vertex):
                                crossing_count += 1
                            prev_vertex = None
                        else:
                            prev_vertex = curr_node.kind
                    else:
                        if curr_node.is_n_s():
                            crossing_count += 1
                else:
                    if curr_node.is_vertex():
                        prev_vertex = curr_node.kind
                    else:
                        crossing_count += 1
        src_node.is_inside = crossing_count % 2 != 0
        return src_node.is_inside

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

    # 722 is too high
    # 456 is too high

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        distance = 1
        prev = self.start
        # self.print_grid()
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
        answer = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                node = self.grid[y][x]
                if not node.is_main_loop() and self.is_node_inside_loop(node):
                    answer += 1
        # self.print_grid()
        return answer


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
