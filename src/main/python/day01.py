#!/usr/bin/env python3
"""
Day 1: Trebuchet?!

https://adventofcode.com/2023/day/1
"""
import re
from typing import Any

from src.main.python.util import AbstractSolver

DIGIT_MAP = {
        '0':     0,
        'zero':  0,
        '1':     1,
        'one':   1,
        '2':     2,
        'two':   2,
        '3':     3,
        'three': 3,
        '4':     4,
        'four':  4,
        '5':     5,
        'five':  5,
        '6':     6,
        'six':   6,
        '7':     7,
        'seven': 7,
        '8':     8,
        'eight': 8,
        '9':     9,
        'nine':  9
}

PATTERN = re.compile(r'\d')

FIRST_DIGIT_PATTERN = re.compile(
        r'(\d|zero|one|two|three|four|five|six|seven|eight|nine).*')
LAST_DIGIT_PATTERN = re.compile(
        r'.*(\d|zero|one|two|three|four|five|six|seven|eight|nine)')


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def find_first_digit(line: str) -> int:
        return DIGIT_MAP[FIRST_DIGIT_PATTERN.findall(line)[0]]

    @staticmethod
    def find_last_digit(line: str) -> int:
        return DIGIT_MAP[LAST_DIGIT_PATTERN.findall(line)[0]]

    def line_to_value_part2(self, line: str) -> int:
        return self.find_first_digit(line) * 10 + self.find_last_digit(line)

    @staticmethod
    def line_to_value(line: str) -> int:
        matches = PATTERN.findall(line)
        if matches:
            return int(str(matches[0]) + str(matches[-1]))
        else:
            raise Exception(f'No match, line={line}')

    def solve_part_1(self, data: list[str]) -> Any:
        answer = 0
        for line in data:
            answer += self.line_to_value(line)
        return answer

    def solve_part_2(self, data: list[str]) -> Any:
        answer = 0
        for line in data:
            answer += self.line_to_value_part2(line)
        return answer


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
