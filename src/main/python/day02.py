#!/usr/bin/env python3
"""
Day 1: Tebuchet?!

https://adventofcode.com/2023/day/1
"""
import os
from typing import Any

from src.main.python.util import AbstractSolver


class Round:
    def __init__(self, cube_counts: dict[str, int]) -> None:
        super().__init__()
        self.cube_counts = cube_counts


class Game:
    def __init__(self, game_id, rounds) -> None:
        super().__init__()
        self.game_id = int(game_id)
        self.rounds = rounds


class Bag:
    def __init__(self) -> None:
        super().__init__()
        self.games = []

    def add_game(self, game: Game):
        self.games.append(game)


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def parse_round(round_data: str) -> Round:
        cubes_data = round_data.split(',')
        cube_counts = dict()
        for cube_data in cubes_data:
            cube_count, cube_color = cube_data.strip().split(' ')
            cube_counts[cube_color] = int(cube_count)
        return Round(cube_counts)

    def parse_rounds(self, rounds_data: list[str]) -> list[Round]:
        rounds = []
        for round_data in rounds_data:
            rounds.append(self.parse_round(round_data))
        return rounds

    def parse_line(self, line: str) -> Game:
        game_data, rounds_data = line.split(':')
        _, game_id = game_data.split(' ')
        rounds = self.parse_rounds(rounds_data.split(';'))
        return Game(game_id, rounds)

    def init_data(self, data_file_path: str = None) -> Any:
        data = self.get_data(self.get_day(), data_file_path)
        games = []
        for line in data:
            games.append(self.parse_line(line))
        return games

    def is_round_valid(self, reference_round: Round, round: Round):
        for cube_color, cube_count in round.cube_counts.items():
            if cube_count > reference_round.cube_counts[cube_color]:
                return False
        return True

    def is_game_valid(self, reference_round: Round, game: Game):
        for round in game.rounds:
            if not self.is_round_valid(reference_round, round):
                return False
        return True

    def get_valid_games(self, reference_round: Round,
                        games: list[Game]) -> list[Game]:
        valid_games = []
        for game in games:
            if self.is_game_valid(reference_round, game):
                valid_games.append(game)
        return valid_games

    def solve_part_1(self, games: list[Game]) -> Any:
        answer = 0
        reference_round = Round({'red': 12, 'green': 13, 'blue': 14})
        valid_games = self.get_valid_games(reference_round, games)
        for game in valid_games:
            answer += game.game_id
        return answer

    def solve_part_2(self, games: list[Game]) -> Any:
        answer = 0
        return answer

    def get_day(self) -> str:
        return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
