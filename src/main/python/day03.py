#!/usr/bin/env python3
"""
Day 1: Gear Ratios

https://adventofcode.com/2023/day/3
"""
import os
import re
from typing import Any

from src.main.python.util import AbstractSolver


class PartNumber:
    def __init__(self) -> None:
        super().__init__()
        self.startX = 0
        self.endX = 0
        self.y = 0
        self.value = 0


class Schematic:
    def __init__(self) -> None:
        super().__init__()
        self.data = []
        self.part_numbers = []

    def is_adjacent(self, min_x: int, max_x: int, min_y: int,
                    max_y: int) -> bool:
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if self.data[y][x] == '.':
                    continue
                char_value = ord(self.data[y][x])
                if 32 < char_value < 48 or \
                        57 < char_value < 65 or \
                        90 < char_value < 127:
                    return True
        return False

    def is_part_number(self, part_number: PartNumber) -> bool:
        min_x = part_number.startX - 1 if part_number.startX > 0 else 0
        width = len(self.data[0]) - 1
        max_x = part_number.endX + 1 if part_number.endX < width else width
        min_y = part_number.y - 1 if part_number.y > 0 else 0
        height = len(self.data) - 1
        max_y = part_number.y + 1 if part_number.y < height else height
        return self.is_adjacent(min_x, max_x, min_y, max_y)


class Solver(AbstractSolver):
    PATTERN = re.compile(r'(\d+)')

    def __init__(self) -> None:
        super().__init__()
        self.schematic = None

    def init_data(self, data_file_path: str = None) -> Any:
        data = self.get_data(self.get_day(), data_file_path)
        self.schematic = Schematic()
        self.schematic.data = data
        part_numbers = []
        for y, line in enumerate(data):
            for m in Solver.PATTERN.finditer(line):
                part_number = PartNumber()
                part_number.value = int(m.group(1))
                part_number.startX = m.span()[0]
                part_number.endX = m.span()[1] - 1
                part_number.y = y
                part_numbers.append(part_number)
        self.schematic.part_numbers = part_numbers
        return data

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        for part_number in self.schematic.part_numbers:
            if self.schematic.is_part_number(part_number):
                answer += part_number.value
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        answer = 0
        return answer

    def get_day(self) -> str:
        return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
