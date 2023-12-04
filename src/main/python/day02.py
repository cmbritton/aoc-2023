#!/usr/bin/env python3
"""
Day 2: Cube Conundrum

https://adventofcode.com/2023/day/2
"""
import os
from collections import defaultdict
from typing import Any

from src.main.python.util import AbstractSolver


class GameRound:
    def __init__(self, cube_counts: dict[str, int]) -> None:
        super().__init__()
        self.cube_counts = cube_counts


class Game:
    def __init__(self, game_id, game_rounds) -> None:
        super().__init__()
        self.game_id = int(game_id)
        self.game_rounds = game_rounds


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def parse_game_round(game_round_data: str) -> GameRound:
        cubes_data = game_round_data.split(',')
        cube_counts = dict()
        for cube_data in cubes_data:
            cube_count, cube_color = cube_data.strip().split(' ')
            cube_counts[cube_color] = int(cube_count)
        return GameRound(cube_counts)

    def parse_game_rounds(self, game_rounds_data: list[str]) -> list[
        GameRound]:
        game_rounds = []
        for game_round_data in game_rounds_data:
            game_rounds.append(self.parse_game_round(game_round_data))
        return game_rounds

    def parse_line(self, line: str) -> Game:
        game_data, game_rounds_data = line.split(':')
        _, game_id = game_data.split(' ')
        rounds = self.parse_game_rounds(game_rounds_data.split(';'))
        return Game(game_id, rounds)

    def init_data(self, data_file_path: str = None) -> Any:
        data = self.get_data(self.get_day(), data_file_path)
        games = []
        for line in data:
            games.append(self.parse_line(line))
        return games

    def is_game_round_valid(self, reference_round: GameRound,
                            game_round: GameRound):
        for cube_color, cube_count in game_round.cube_counts.items():
            if cube_count > reference_round.cube_counts[cube_color]:
                return False
        return True

    def is_game_valid(self, reference_round: GameRound, game: Game):
        for game_round in game.game_rounds:
            if not self.is_game_round_valid(reference_round, game_round):
                return False
        return True

    def get_valid_games(self, reference_round: GameRound,
                        games: list[Game]) -> list[Game]:
        valid_games = []
        for game in games:
            if self.is_game_valid(reference_round, game):
                valid_games.append(game)
        return valid_games

    def get_min_games(self, games: list[Game]) -> list[Game]:
        min_games = []
        for game in games:
            min_game_round = defaultdict(lambda: 0)
            for game_round in game.game_rounds:
                for cube_color, cube_count in game_round.cube_counts.items():
                    min_game_round[cube_color] = max(
                            min_game_round[cube_color], cube_count)
            min_games.append(Game(game.game_id, [min_game_round]))
        return min_games

    def solve_part_1(self, games: list[Game]) -> Any:
        answer = 0
        reference_round = GameRound({'red': 12, 'green': 13, 'blue': 14})
        valid_games = self.get_valid_games(reference_round, games)
        for game in valid_games:
            answer += game.game_id
        return answer

    def solve_part_2(self, games: list[Game]) -> Any:
        answer = 0
        min_games = self.get_min_games(games)
        for game in min_games:
            game_power = 1
            for min_cube_color, min_cube_count in game.game_rounds[0].items():
                game_power *= min_cube_count
            answer += game_power
        return answer

    def get_day(self) -> str:
        return os.path.basename(__file__)[3:5]


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
