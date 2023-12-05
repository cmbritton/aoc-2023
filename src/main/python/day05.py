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


STATE_MAP = {
        'seeds':                       State.SEEDS,
        'seed-to-soil map':            State.SEED_TO_SOIL,
        'soil-to-fertilizer map':      State.SOIL_TO_FERTILIZER,
        'fertilizer-to-water map':     State.FERTILIZER_TO_WATER,
        'water-to-light map':          State.WATER_TO_LIGHT,
        'light-to-temperature map':    State.LIGHT_TO_TEMP,
        'temperature-to-humidity map': State.TEMP_TO_HUMIDITY,
        'humidity-to-location map':    State.HUMIDITY_TO_LOCATION
}


class ValueMap:
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.data = []

    @staticmethod
    def apply(map_data: tuple[int, int, int], value: int) \
            -> tuple[bool, int]:
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
        for value_map in self.value_maps:
            result = value_map.map_value(result)
        return result


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.almanac = Almanac()

    @staticmethod
    def state_from_line(line: str, state: State) -> State:
        if ':' in line:
            state_label = line.strip().split(':', maxsplit=1)[0]
            if state_label in STATE_MAP:
                return STATE_MAP[state_label]
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
