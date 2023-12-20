#!/usr/bin/env python3
"""
Day 5: If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5
"""
from collections import namedtuple
from functools import reduce
from typing import Any

from src.main.python.util import AbstractSolver

Rule = namedtuple('Rule', ['dst', 'src', 'size'])

Interval = namedtuple('Interval', ['start', 'size'])


class Solver(AbstractSolver):
    def __init__(self) -> None:
        super().__init__()
        self.seed_intervals = []
        self.rule_sets = []

    def find_low_interval(self, rule: Rule, interval: Interval) -> Any:
        if self.is_leading_overlap(rule, interval) or self.is_spanned_overlap(
                rule, interval):
            return Interval(interval.start, rule.src - interval.start)
        elif self.is_interval_less_than(rule, interval):
            return interval
        else:
            return None

    @staticmethod
    def is_interval_start_in_rule_span(rule: Rule, interval: Interval) -> bool:
        return rule.src <= interval.start <= rule.src + rule.size - 1

    @staticmethod
    def is_interval_end_in_rule_span(rule: Rule, interval: Interval) -> bool:
        return (rule.src <= interval.start + interval.size - 1 <= rule.src +
                rule.size - 1)

    @staticmethod
    def is_interval_span_include_rule_span(rule: Rule,
                                           interval: Interval) -> bool:
        return (interval.start <= rule.src and
                interval.start + interval.size - 1 >= rule.src + rule.size - 1)

    def is_leading_overlap(self, rule: Rule, interval: Interval):
        return (not self.is_interval_start_in_rule_span(rule, interval)
                and self.is_interval_end_in_rule_span(rule, interval))

    def is_trailing_overlap(self, rule: Rule, interval: Interval):
        return (self.is_interval_start_in_rule_span(rule, interval)
                and not self.is_interval_end_in_rule_span(rule, interval))

    def is_contained_overlap(self, rule: Rule, interval: Interval):
        return (self.is_interval_start_in_rule_span(rule, interval)
                and self.is_interval_end_in_rule_span(rule, interval))

    @staticmethod
    def is_spanned_overlap(rule: Rule, interval: Interval):
        return (interval.start <= rule.src
                and interval.start + interval.size - 1 >= rule.src +
                rule.size - 1)

    @staticmethod
    def is_interval_greater(rule: Rule, interval: Interval):
        return (interval.start > rule.src + rule.size - 1
                and interval.start + interval.size - 1 > rule.src +
                rule.size - 1)

    @staticmethod
    def is_interval_less_than(rule: Rule, interval: Interval):
        return (interval.start < rule.src
                and interval.start + interval.size - 1 < rule.src)

    def find_match_interval(self, rule: Rule, interval: Interval) -> Any:
        if self.is_leading_overlap(rule, interval):
            return Interval(rule.src,
                            interval.start + interval.size - rule.src)
        elif self.is_trailing_overlap(rule, interval):
            return Interval(interval.start,
                            rule.src + rule.size - interval.start)
        elif self.is_contained_overlap(rule, interval):
            return interval
        elif self.is_spanned_overlap(rule, interval):
            return Interval(rule.src, rule.size)
        else:
            return None

    def find_high_interval(self, rule: Rule, interval: Interval) -> Any:
        if self.is_trailing_overlap(rule, interval) or self.is_spanned_overlap(
                rule, interval):
            return Interval(rule.src + rule.size,
                            (interval.start + interval.size) - (
                                    rule.src + rule.size))
        elif self.is_interval_greater(rule, interval):
            return interval
        else:
            return None

    def split_interval(self, rule: Rule, interval: Interval) \
            -> (Interval, Interval, Interval):
        low_interval = self.find_low_interval(rule, interval)
        match_interval = self.find_match_interval(rule, interval)
        high_interval = self.find_high_interval(rule, interval)
        return low_interval, match_interval, high_interval

    def apply_rule(self, rule: Rule, interval: Interval) \
            -> (Interval, Interval, Interval):
        low_interval, match_interval, high_interval \
            = self.split_interval(rule, interval)
        if match_interval:
            start = rule.dst + (match_interval.start - rule.src)
            match_interval = Interval(start, match_interval.size)
        return low_interval, match_interval, high_interval

    def apply_rule_set(self, rule_set: list[Rule], interval: Interval) \
            -> list[Interval]:
        result = []
        if interval and len(rule_set) > 0:
            low_interval, match_interval, high_interval = self.apply_rule(
                    rule_set[0], interval)
            s1 = low_interval.size if low_interval else 0
            s2 = match_interval.size if match_interval else 0
            s3 = high_interval.size if high_interval else 0
            assert sum([s1, s2, s3]) == interval.size
            if match_interval:
                result.append(match_interval)
            if len(rule_set) > 1:
                low_interval_matches = self.apply_rule_set(rule_set[1:],
                                                           low_interval)
                if low_interval_matches:
                    result.extend(low_interval_matches)
                high_interval_matches = self.apply_rule_set(rule_set[1:],
                                                            high_interval)
                if high_interval_matches:
                    result.extend(high_interval_matches)
            else:
                if low_interval:
                    result.append(low_interval)
                if high_interval:
                    result.append(high_interval)

        return result

    def apply_rule_sets(self, rule_sets: list[list[Rule]],
                        interval: Interval) -> list[Interval]:
        result = []
        result2 = []
        if rule_sets:
            result.extend(self.apply_rule_set(rule_sets[0], interval))
            if len(rule_sets) > 1:
                for interval2 in result:
                    result2.extend(
                            self.apply_rule_sets(rule_sets[1:], interval2))
            else:
                result2.extend(result)
        return result2

    def solve(self):
        intervals = []
        for interval in self.seed_intervals:
            a = self.apply_rule_sets(self.rule_sets, interval)
            intervals.extend(a)
        return reduce(self.min_interval, intervals)

    @staticmethod
    def min_interval(interval_1: Interval, interval_2: Interval) -> Interval:
        if interval_1.start < interval_2.start:
            return interval_1
        else:
            return interval_2

    def init_data_part_2(self, data: list[str]) -> None:
        rule_set = None
        for line in data:
            line = line.strip()
            if line == '' in line:
                continue
            elif line.startswith('seeds'):
                _, seeds = line.split(': ')
                values = seeds.strip().split()
                for seed, size in zip(values[::2], values[1::2]):
                    seed_interval = Interval(start=int(seed), size=int(size))
                    self.seed_intervals.append(seed_interval)
                continue
            elif 'map:' in line:
                if rule_set is not None:
                    self.rule_sets.append(rule_set)
                rule_set = []
                continue
            rule_set.append(Rule(*map(int, line.strip().split())))
        if rule_set:
            self.rule_sets.append(rule_set)

    def init_data_part_1(self, data: list[str]) -> None:
        rule_set = None
        for line in data:
            line = line.strip()
            if line == '' in line:
                continue
            elif line.startswith('seeds'):
                _, seeds = line.split(': ')
                for seed in seeds.strip().split():
                    seed_interval = Interval(start=int(seed), size=1)
                    self.seed_intervals.append(seed_interval)
                continue
            elif 'map:' in line:
                if rule_set is not None:
                    self.rule_sets.append(rule_set)
                rule_set = []
                continue
            rule_set.append(Rule(*map(int, line.strip().split())))
        if rule_set:
            self.rule_sets.append(rule_set)

    def solve_part_1(self, data: list[Any]) -> Any:
        self.init_data_part_1(data)
        return self.solve().start

    def solve_part_2(self, data: list[Any]) -> Any:
        self.init_data_part_2(data)
        return self.solve().start


def main() -> None:
    solver = Solver()
    solver.run()


if __name__ == "__main__":
    main()
