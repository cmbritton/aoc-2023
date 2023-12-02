#!/usr/bin/env python3
"""
Day 1: Tebuchet?!

https://adventofcode.com/2023/day/1
"""
import os
import re
from typing import Any

from src.main.python.util import AbstractSolver


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def init_data(self, data_file_path: str = None) -> Any:
        return self.get_data(self.get_day(), data_file_path)

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        pattern = re.compile(r'\d')
        for line in data:
            matches = pattern.findall(line)
            if matches:
                value = int(str(matches[0]) + str(matches[-1]))
                answer += value
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        return 2

    def get_day(self) -> str:
        return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
