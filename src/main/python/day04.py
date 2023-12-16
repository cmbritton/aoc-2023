#!/usr/bin/env python3
"""
Day 4: Scratchcards

https://adventofcode.com/2023/day/4
"""
import os
import sys
from typing import Any

from src.main.python.util import AbstractSolver


class Card:
    def __init__(self) -> None:
        super().__init__()
        self.card_id = None
        self.my_numbers = []
        self.winning_numbers = []

    @staticmethod
    def make_card(card_id: str, my_numbers: list[int],
                  winning_numbers: list[int]):
        card = Card()
        card.card_id = card_id
        card.my_numbers = my_numbers
        card.winning_numbers = winning_numbers
        return card

    def winning_count(self) -> int:
        winning_count = 0
        for my_number in self.my_numbers:
            if my_number in self.winning_numbers:
                winning_count += 1
        return winning_count


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.data = None

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
            cards.append(Card.make_card(label, my_numbers, winning_numbers))

        self.data = cards
        return cards

    def add_winnings(self, index: int, winning_count: int) -> int:
        score = 0
        if winning_count > 0:
            for card in self.data[index + 1:index + winning_count]:
                score += self.add_winnings(index + 1, card.winning_count())
        score += winning_count
        return score

    def solve_part_1(self, data: list[Any]) -> Any:
        answer = 0
        for card in data:
            winning_count = card.winning_count()
            if winning_count > 0:
                answer += 2 ** (winning_count - 1)
        return answer

    def solve_part_2(self, data: list[Any]) -> Any:
        answer = len(data)
        for index, card in enumerate(data):
            winning_count = card.winning_count()
            if winning_count > 0:
                answer += self.add_winnings(index, winning_count)

        return answer


def main() -> None:
    sys.setrecursionlimit(1500000)
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
