#!/usr/bin/env python3
"""
Day 5: If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5
"""
import os
from enum import auto, Enum
from typing import Any

from src.main.python.util import AbstractSolver


class State(Enum):
    SEEDS = auto()
    SEED_TO_SOIL = auto()
    SOIL_TO_FERTILIZER = auto()
    FERTILIZER_TO_WATER = auto()
    WATER_TO_LIGHT = auto()
    LIGHT_TO_TEMP = auto()
    TEMP_TO_HUMIDITY = auto()
    HUMIDITY_TO_LOCATION = auto()


class ValueMap:
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.data = []

    def apply(self, map_data: tuple[int, int, int], value: int) -> tuple[bool, int]:
        if map_data[1] <= value <= map_data[1] + map_data[2]:
            return True, value - map_data[1] + map_data[0]
        return False, value

    def map_value(self, value: int) -> int:
        result = value
        for map_data in self.data:
            rule_applied, result = self.apply(map_data, result)
            if rule_applied:
                break
        return result


class Almanac:
    def __init__(self) -> None:
        super().__init__()
        self.seeds = None
        self.value_maps = []

    def map_seed(self, seed: int) -> int:
        result = seed
        # print(f'\nseed = {result}')
        for value_map in self.value_maps:
            result = value_map.map_value(result)
            # print(f'{value_map.name} result = {result}')
        return result

class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.almanac = Almanac()

    @staticmethod
    def state_from_line(line: str, prev_state: State) -> State:
        state = prev_state
        if line.startswith('seeds:'):
            state = State.SEEDS
        elif line.startswith('seed-to-soil map:'):
            state = State.SEED_TO_SOIL
        elif line.startswith('soil-to-fertilizer map:'):
            state = State.SOIL_TO_FERTILIZER
        elif line.startswith('fertilizer-to-water map:'):
            state = State.FERTILIZER_TO_WATER
        elif line.startswith('water-to-light map:'):
            state = State.WATER_TO_LIGHT
        elif line.startswith('light-to-temperature map:'):
            state = State.LIGHT_TO_TEMP
        elif line.startswith('temperature-to-humidity map:'):
            state = State.TEMP_TO_HUMIDITY
        elif line.startswith('humidity-to-location map:'):
            state = State.HUMIDITY_TO_LOCATION

        return state

    def init_data(self, data_file_path: str = None) -> Any:
        data = self.get_data(self.get_day(), data_file_path)
        state = None
        value_map = None
        for line in data:
            if line.strip() == '':
                continue
            prev_state = state
            state = self.state_from_line(line, state)
            if state != prev_state:
                if State.SEEDS == state:
                    _, seeds = line.split(': ')
                    self.almanac.seeds = tuple(map(int, seeds.strip().split()))
                else:
                    if value_map is not None:
                        self.almanac.value_maps.append(value_map)
                    value_map = ValueMap()
                    value_map.name = state.name
                continue
            value_map.data.append(tuple(map(int, line.strip().split())))
        self.almanac.value_maps.append(value_map)

        return data

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = -1
        for seed in self.almanac.seeds:
            x = self.almanac.map_seed(seed)
            if x < answer or -1 == answer:
                answer = x
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
