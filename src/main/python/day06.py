#!/usr/bin/env python3
"""
Day 6: Wait For It

https://adventofcode.com/2023/day/6
"""
from collections import namedtuple
from typing import Any

from src.main.python.util import AbstractSolver

Race = namedtuple('Race', ['time', 'dist'])


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.races = None
        self.big_race = None

    def init_data(self, data: list[str]) -> None:
        t = tuple([int(x.strip()) for x in
                   data[0].split('Time:')[1].strip().split()])
        d = tuple([int(x.strip()) for x in
                   data[1].split('Distance:')[1].strip().split()])
        self.races = tuple([Race(x, y) for x, y in zip(t, d)])

        t2 = int(data[0].split('Time:')[1].strip().replace(' ', ''))
        d2 = int(data[1].split('Distance:')[1].strip().replace(' ', ''))
        self.big_race = Race(t2, d2)

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data)
        answer = 1
        for race in self.races:
            win_count = 0
            for hold_time in range(race.time + 1):
                if hold_time * (race.time - hold_time) > race.dist:
                    win_count += 1
            answer *= win_count
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data)
        start = 0
        for hold_time in range(self.big_race.time + 1):
            if hold_time * (self.big_race.time - hold_time) > self.big_race.dist:
                start = hold_time
                break
        end = 0
        for hold_time in range(self.big_race.time, 0, -1):
            if hold_time * (self.big_race.time - hold_time) > self.big_race.dist:
                end = hold_time
                break
        return end - start + 1


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
