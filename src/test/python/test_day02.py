#!/usr/bin/env python3
import os.path

from src.main.python.day02 import Solver


day = os.path.basename(__file__)[8:10]


def test_part_1_example():
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{day}-example.data')
    solver = Solver()
    answer = solver.part_1(data_file_path)
    assert answer == 8


def test_part_2_example():
    data_file_path = os.path.join(os.environ.get('TEST_RESOURCES_DIR_PATH'),
                                  f'day{day}-example.data')
    solver = Solver()
    answer = solver.part_2(data_file_path)
    assert answer == 2286


def test_part_1():
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{day}.data')
    solver = Solver()
    answer = solver.part_1(data_file_path)
    assert answer == 2265


def test_part_2():
    data_file_path = os.path.join(os.environ.get('RESOURCES_DIR_PATH'),
                                  f'day{day}.data')
    solver = Solver()
    answer = solver.part_2(data_file_path)
    assert answer == 64097
