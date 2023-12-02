#!/usr/bin/env python3
"""
Day 1: Tebuchet?!

https://adventofcode.com/2023/day/1
"""
import os
import re
from typing import Any

from src.main.python.util import AbstractSolver

DIGIT_NAMES = {
        'zero':  '0',
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9'
}

PATTERN = re.compile(r'\d')


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def init_data(self, data_file_path: str = None) -> Any:
        return self.get_data(self.get_day(), data_file_path)

    @staticmethod
    def line_to_value(line: str) -> int:
        matches = PATTERN.findall(line)
        if matches:
            value = int(str(matches[0]) + str(matches[-1]))
            print(f'line: {line}')
            print(f'value: {value}\n')
            return value
        else:
            raise Exception(f'No match, line={line}')

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        # for line in data:
        #     answer += self.line_to_value(line)
        return answer

    # 54571 is too low

    def solve_part_2(self, data: list[Any]) -> Any:
        answer = 0
        for line in data:
            it = re.finditer(
                    r'(one|two|three|four|five|six|seven|eight|nine|zero)',
                    line)
            for digit_name in it:
                line = line.replace(digit_name.group(1),
                                    DIGIT_NAMES[digit_name.group(1)])
            answer += self.line_to_value(line)
        return answer

    def get_day(self) -> str:
        return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
