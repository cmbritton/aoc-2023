#!/usr/bin/env python3
import os.path

from src.main.python.day10 import Solver


day = os.path.basename(__file__)[8:10]


def test_part_1_example():
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{day}-part1-example.data')
    solver = Solver()
    answer = solver.part_1(data_file_path)
    assert answer == 4


def test_part_2_example():
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{day}-part2-example.data')
    solver = Solver()
    answer = solver.part_2(data_file_path)
    assert answer == 10


def test_part_1():
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{day}.data')
    solver = Solver()
    answer = solver.part_1(data_file_path)
    assert answer == 6956


def test_part_2():
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{day}.data')
    solver = Solver()
    answer = solver.part_2(data_file_path)
    assert answer == 455
