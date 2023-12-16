#!/usr/bin/env python3
"""
Day 3: Gear Ratios

https://adventofcode.com/2023/day/3
"""
import os
import re
from typing import Any

from src.main.python.util import AbstractSolver


class PartNumber:
    def __init__(self) -> None:
        super().__init__()
        self.start_x = 0
        self.end_x = 0
        self.y = 0
        self.value = 0

    def __key(self):
        return self.start_x, self.end_x, self.y, self.value

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, PartNumber):
            return self.__key() == other.__key()
        return NotImplemented

    @staticmethod
    def make_part_number(start_x: int, end_x: int, y: int,
                         value: int) -> 'PartNumber':
        part_number = PartNumber()
        part_number.start_x = start_x
        part_number.end_x = end_x
        part_number.y = y
        part_number.value = value
        return part_number


class Gear:
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.parts = None
        self.x = x
        self.y = y

    def __key(self):
        return self.x, self.y, frozenset(self.parts)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Gear):
            return self.__key() == other.__key()
        return NotImplemented


class Schematic:
    GEAR_PATTERN = re.compile(r'(\*)')
    PART_NUMBER_PATTERN = re.compile(r'(\d+)')

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

    def get_max_x(self):
        return len(self.data[0]) - 1

    def get_max_y(self):
        return len(self.data) - 1

    def is_part_number(self, part_number: PartNumber) -> bool:
        min_x = part_number.start_x - 1 if part_number.start_x > 0 else 0
        width = self.get_max_x()
        max_x = part_number.end_x + 1 if part_number.end_x < width else width
        min_y = part_number.y - 1 if part_number.y > 0 else 0
        height = self.get_max_y()
        max_y = part_number.y + 1 if part_number.y < height else height
        return self.is_adjacent(min_x, max_x, min_y, max_y)

    def find_adjacent_parts(self, x: int, y: int) -> set[PartNumber]:
        part_numbers = set()
        for m in self.PART_NUMBER_PATTERN.finditer(self.data[y]):
            if m.span()[0] <= x <= m.span()[1] - 1:
                part_number = PartNumber.make_part_number(m.span()[0],
                                                          m.span()[1] - 1,
                                                          y, int(m.group(1)))
                part_numbers.add(part_number)
        return part_numbers

    def find_parts_for_gear(self, potential_gear: Gear) -> set[PartNumber]:
        part_numbers = set()
        min_x = potential_gear.x - 1 if potential_gear.x > 0 else 0
        width = self.get_max_x()
        max_x = potential_gear.x + 1 if potential_gear.x < width else width
        min_y = potential_gear.y - 1 if potential_gear.y > 0 else 0
        height = self.get_max_y()
        max_y = potential_gear.y + 1 if potential_gear.y < height else height
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                part_numbers.update(self.find_adjacent_parts(x, y))
        return part_numbers

    def get_potential_gears(self, y: int, line: str) -> set[Gear]:
        potential_gears = set()
        for m in Schematic.GEAR_PATTERN.finditer(line):
            potential_gear = Gear(m.span()[0], y)
            potential_gear.parts = self.find_parts_for_gear(potential_gear)
            potential_gears.add(potential_gear)
        return potential_gears

    def find_gears(self) -> set[Gear]:
        gears = set()
        for y, line in enumerate(self.data):
            for potential_gear in self.get_potential_gears(y=y, line=line):
                if len(potential_gear.parts) == 2:
                    gears.add(potential_gear)
        return gears


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.schematic = None

    def init_data(self, data_file_path: str = None) -> Any:
        data = self.get_data(self.get_day(), data_file_path)
        self.schematic = Schematic()
        self.schematic.data = data
        part_numbers = set()
        for y, line in enumerate(data):
            for m in Schematic.PART_NUMBER_PATTERN.finditer(line):
                part_number = PartNumber.make_part_number(m.span()[0],
                                                          m.span()[1] - 1,
                                                          y, int(m.group(1)))
                part_numbers.add(part_number)
        self.schematic.part_numbers = list(part_numbers)
        return data

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        for part_number in self.schematic.part_numbers:
            if self.schematic.is_part_number(part_number):
                answer += part_number.value
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        answer = 0
        gears = self.schematic.find_gears()
        for gear in gears:
            parts = list(gear.parts)
            answer += parts[0].value * parts[1].value
        return answer


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
