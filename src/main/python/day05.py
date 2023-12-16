#!/usr/bin/env python3
"""
Day 5: If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5
"""
from collections import namedtuple
from functools import reduce
from itertools import repeat
from typing import Any

from src.main.python.util import AbstractSolver

Rule = namedtuple('Rule', ['dst', 'src', 'size'])


def my_range(start, size):
    value = start
    while value < value + size:
        yield value
        value += 1


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.seeds = None
        self.rule_sets = []

    @staticmethod
    def apply_rule_set(rule_set: list[Rule], value: int) -> int:
        result = value
        for rule in rule_set:
            if rule.src <= value < rule.src + rule.size:
                return (value - rule.src) + rule.dst
        return result

    def apply_rule_sets(self, value: int) -> int:
        result = value
        for rule_set in self.rule_sets:
            result = self.apply_rule_set(rule_set, result)
        return result

    def process_seed_list(self, seed: int, size: int) -> int:
        # print(f'Processing {size} seeds starting with {seed}')
        # return min(list(map(self.apply_rule_sets, count(seed, size))))

        result = float('inf')
        value = seed
        while value < seed + size:
            result = min(result, self.apply_rule_sets(value))
            value += 1
        return result

    def init_data(self, data: list[str]) -> None:
        rule_set = None
        for line in data:
            line = line.strip()
            if line == '' in line:
                continue
            elif line.startswith('seeds'):
                _, seeds = line.split(': ')
                self.seeds = tuple(map(int, seeds.strip().split()))
                continue
            elif 'map:' in line:
                if rule_set is not None:
                    self.rule_sets.append(rule_set)
                rule_set = []
                continue
            rule_set.append(Rule(*map(int, line.strip().split())))
        if rule_set:
            self.rule_sets.append(rule_set)

    def solve_part_1(self, data: list[str]) -> Any:
        self.init_data(data)
        return reduce(lambda x, y: min(x, y),
                      map(self.process_seed_list, self.seeds, repeat(1)))

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        return reduce(lambda x, y: min(x, y),
                      map(self.process_seed_list, self.seeds[0::2],
                          self.seeds[1::2]))
        # l = list(
        #     map(self.process_seed_list, self.seeds[0::2], self.seeds[1::2]))
        # return min(l)

    # def get_day(self) -> str:
    #     return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
