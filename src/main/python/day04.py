#!/usr/bin/env python3
"""
Day 4: Scratchcards

https://adventofcode.com/2023/day/4
"""
import os
from typing import Any

from src.main.python.util import AbstractSolver


class Card:
    def __init__(self) -> None:
        super().__init__()
        self.winning_numbers = []
        self.my_numbers = []


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    def init_data(self, data_file_path: str = None) -> Any:
        cards = []
        data = self.get_data(self.get_day(), data_file_path)
        for line in data:
            label, rest = line.split(':')
            winning_numbers_str, my_numbers_str = rest.strip().split('|')
            winning_numbers_list = winning_numbers_str.strip().split()
            winning_numbers = [int(x.strip()) for x in winning_numbers_list]
            my_numbers_list = my_numbers_str.strip().split()
            my_numbers = [int(x.strip()) for x in my_numbers_list]
            card = Card()
            card.my_numbers = my_numbers
            card.winning_numbers = winning_numbers
            cards.append(card)

        return cards

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        for card in data:
            winning_count = -1
            for my_number in card.my_numbers:
                if my_number in card.winning_numbers:
                    winning_count += 1
            if winning_count >= 0:
                answer += 2 ** winning_count
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
