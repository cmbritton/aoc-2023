#!/usr/bin/env python3
"""
Day 7: Camel Cards

https://adventofcode.com/2023/day/7
"""
from collections import Counter
from typing import Any

from src.main.python.util import AbstractSolver


class Hand(object):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    CARDS = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
    }

    def __init__(self, cards: str, bid: int) -> None:
        super().__init__()
        self.cards = cards
        self.bid = bid
        self._strength = self._calc_strength(cards)

    def __eq__(self, other: 'Hand'):
        if other is None:
            return False
        return self.cards == other.cards

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other: 'Hand') -> bool:
        if other is None:
            return False
        if self.strength == other.strength:
            return self._tie_breaker(other) < 0
        else:
            return self.strength < other.strength

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if other is None:
            return True
        return not self.__lt__(other) and not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def _tie_breaker(self, other: 'Hand') -> int:
        for i in range(5):
            if type(self).CARDS[self.cards[i]] < type(self).CARDS[
                    other.cards[i]]:
                return -1
            elif type(self).CARDS[self.cards[i]] > type(self).CARDS[
                    other.cards[i]]:
                return 1
        return 0

    @staticmethod
    def _calc_strength(cards: str) -> int:
        c = Counter(cards)
        counts = list(c.values())
        if 5 in counts:
            return Hand.FIVE_OF_A_KIND
        elif 4 in counts:
            return Hand.FOUR_OF_A_KIND
        elif 2 in counts and 3 in counts:
            return Hand.FULL_HOUSE
        elif 3 in counts:
            return Hand.THREE_OF_A_KIND
        elif counts.count(2) == 2:
            return Hand.TWO_PAIR
        elif counts.count(2) == 1:
            return Hand.ONE_PAIR

        return Hand.HIGH_CARD

    @property
    def strength(self) -> int:
        if self._strength is None:
            self._strength = self._calc_strength(self.cards)
        return self._strength

    @strength.setter
    def strength(self, value: int) -> None:
        self._strength = value


class HandJ(Hand):
    CARDS = {
            'J': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'Q': 11,
            'K': 12,
            'A': 13
    }

    def __init__(self, cards: str, bid: int) -> None:
        super().__init__(cards, bid)
        self.aux_cards = None
        self.wild_card = None

    def _calc_strength(self, cards: str) -> int:
        temp_strength = super()._calc_strength(cards)
        if 'J' not in cards:
            return temp_strength

        best_cards = None
        best_strength = Hand.HIGH_CARD
        for card in HandJ.CARDS.keys():
            temp_cards = self.cards.replace('J', card)
            temp_strength = super()._calc_strength(temp_cards)
            if temp_strength > best_strength:
                best_cards = temp_cards
                best_strength = temp_strength
                self.wild_card = card

        if best_cards is not None:
            self.aux_cards = best_cards
            self.strength = best_strength
            return best_strength

        return temp_strength


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.hands = []

    def init_data(self, data: list[str], hand_type) -> None:
        for line in data:
            hand, bid = line.split()
            self.hands.append(hand_type(hand, int(bid)))
        self.hands.sort()

    def compute_winnings(self) -> int:
        answer = 0
        for index, hand in enumerate(self.hands):
            answer += (hand.bid * (index + 1))
        return answer

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data(data, Hand)
        return self.compute_winnings()

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data(data, HandJ)
        return self.compute_winnings()


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
