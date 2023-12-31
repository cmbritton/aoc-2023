#!/usr/bin/env python3
"""
Day 4: Scratchcards

https://adventofcode.com/2023/day/4
"""
import sys
from typing import Any

from src.main.python.util import AbstractSolver


class Card:
    def __init__(self) -> None:
        super().__init__()
        self.card_id = None
        self.my_numbers = None
        self.winning_numbers = None
        self.card_count = 1

    @staticmethod
    def make_card(card_id: str, my_numbers: tuple[int, ...],
                  winning_numbers: tuple[int, ...]):
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
        self.cards = None

    def init_data(self, data: list[str]) -> None:
        self.cards = []
        for line in data:
            label, rest = line.split(':')
            winning_numbers_str, my_numbers_str = rest.strip().split('|')
            winning_numbers_list = winning_numbers_str.strip().split()
            winning_numbers = tuple(
                    [int(x.strip()) for x in winning_numbers_list])
            my_numbers_list = my_numbers_str.strip().split()
            my_numbers = tuple([int(x.strip()) for x in my_numbers_list])
            self.cards.append(
                    Card.make_card(label, my_numbers, winning_numbers))

    def add_winnings(self, index: int, winning_count: int) -> int:
        score = 0
        if winning_count > 0:
            for card in self.cards[index + 1:index + winning_count]:
                score += self.add_winnings(index + 1, card.winning_count())
        score += winning_count
        return score

    def solve_part_1(self, data: list[str]) -> Any:
        self.init_data(data)
        answer = 0
        for card in self.cards:
            winning_count = card.winning_count()
            if winning_count > 0:
                answer += 2 ** (winning_count - 1)
        return answer

    def solve_part_2(self, data: list[str]) -> Any:
        self.init_data(data)
        for index, card in enumerate(self.cards):
            winning_count = card.winning_count()
            if winning_count > 0:
                for c in self.cards[index + 1:index + winning_count + 1]:
                    c.card_count += 1 * card.card_count

        total = 0
        for card in self.cards:
            total += card.card_count
        return total


def main() -> None:
    sys.setrecursionlimit(1500000)
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
