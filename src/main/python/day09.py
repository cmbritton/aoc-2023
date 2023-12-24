#!/usr/bin/env python3
"""
Day 9: Mirage Maintenance

https://adventofcode.com/2023/day/9
"""
from collections import deque
from itertools import pairwise
from typing import Any

from src.main.python.util import AbstractSolver


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.oasis_seqs = []

    @staticmethod
    def regress_seq(seq: list[int]) -> deque[list[int]]:
        done = False
        derived_seqs = deque()
        derived_seqs.append(seq)
        working_seq = seq
        while not done:
            derived_seq = list(map(lambda x: x[1] - x[0], pairwise(working_seq)))
            if all(map(lambda x: x == 0, derived_seq)):
                derived_seq.append(0)
                done = True
            derived_seqs.append(derived_seq)
            working_seq = derived_seq
        return derived_seqs

    @staticmethod
    def extrapolate_next_values(derived_seqs: deque[list[int]]) -> int:
        seq = derived_seqs.pop()
        while len(derived_seqs) > 0:
            value = seq[-1]
            seq = derived_seqs.pop()
            seq.append(seq[-1] + value)
        return seq[-1]

    def find_next_value(self, seq: list[int]) -> int:
        return self.extrapolate_next_values(self.regress_seq(seq))

    def init_data(self, data: list[str]) -> None:
        for line in data:
            self.oasis_seqs.append(list(map(int, line.split())))

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        answer = 0
        for seq in self.oasis_seqs:
            answer += self.find_next_value(seq)

        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        return 0


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
