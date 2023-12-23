#!/usr/bin/env python3
"""
Day 8: Haunted Wasteland

https://adventofcode.com/2023/day/8
"""
import math
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
        start_nodes = list(filter(lambda n: n.name[2] == 'A', self.nodes.values()))
        end_nodes = list(filter(lambda n: n.name[2] == 'Z', self.nodes.values()))
        step_counts = dict()
        for start_node in start_nodes:
            current_node = start_node
            for end_node in end_nodes:
                step_count_key = f'{start_node.name}-{end_node.name}'
                step_counts[step_count_key] = 0
                done = False
                visited_stop_nodes = []
                while not done:
                    for step in self.directions:
                        current_node = self.nodes[getattr(current_node, step)]
                        step_counts[step_count_key] += 1
                        if current_node.name == end_node.name:
                            done = True
                            break
                        elif current_node.name[2] == 'Z':
                            if current_node in visited_stop_nodes:
                                step_counts[step_count_key] = 1
                                done = True
                                break
                            else:
                                visited_stop_nodes.append(current_node)

        return math.lcm(*step_counts.values())


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
