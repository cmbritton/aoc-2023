# [Advent of Code 2023](https://adventofcode.com/2023)

My solutions to Advent of Code (AoC) 2023 puzzles.

Some programmers aim to solve each puzzle in as few lines of code as possible.
Others create really cool animations of puzzle solutions. There are some
extremely skilled people in both camps.

I try to write understandable, maintainable, and extendable object-oriented
code.

## Development Environment

Here's what I use.

### Platform-Independent

* [IntelliJ IDEA](https://www.jetbrains.com/idea/)
* [Python](https://www.python.org/)
* [pipenv](https://pipenv.pypa.io/en/latest/)

### Platform-Specific

* [Windows 10 Pro](https://www.microsoft.com/en-us/software-download/windows10)
* [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) running
  an [Ubuntu 20.04 LTS](https://ubuntu.com/) distribution.

## Setup
Edit the `.env` file to match your environment. Then, run:

    pipenv install

## Run a Daily Puzzle

Run a single puzzle with:

    pipenv run day08.py

## Running Unit Tests

    pipenv run test

## Code Evolution

The logic for each solution is in the `dayxx.init_data`, `dayxx.solve_part_1`,
and `dayxx.solve_part_2` methods. Everything else is common code for reading
puzzle data, testing, outputting results, etc.

Most puzzle solutions follow a pattern you can discern from the commit
messages.

Any commit whose message begins with `WIP` is a work-in-progress checkpoint.
That version may not even work.

Commit messages that look like `Day 8 part 1 works` indicate the revision
that first achieved the correct answer. It might be sloppy. It might be slow.

Messages that contain the word `cleanup` indicate a revision where I removed
commented out lines of code, print statements, etc.

Messages with the word `refactor` mark a revision where I refactored the
original solution to improve readability, performance, or use some language
feature that I was not familiar with enough to use in my initial solution. 

## Results

No answers here! Just elapsed times for each puzzle solution.

| Puzzle                                                                     | Part 1 Elapsed Time | Part 2 Elapsed Time |
|----------------------------------------------------------------------------|--------------------:|--------------------:|
| [Day 1: Trebuchet?!](https://adventofcode.com/2023/1)                      | 735.20 microseconds |   1.44 milliseconds |
| [Day  2: Cube Conundrum](https://adventofcode.com/2023/2)                  | 968.80 microseconds |   1.07 milliseconds |
| [Day  3: Gear Ratios](https://adventofcode.com/2023/3)                     |   3.59 milliseconds |  19.29 milliseconds |
| [Day  4: Scratchcards](https://adventofcode.com/2023/4)                    |   1.65 milliseconds |   1.70 milliseconds |
| [Day  5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/5) |   6.34 milliseconds |  95.98 milliseconds |
| [Day 6: Wait For It](https://adventofcode.com/2023/6)                      |  67.70 microseconds |        1.06 seconds |
| [Day 7: Camel Cards](https://adventofcode.com/2023/7)                      |   5.18 milliseconds |  12.03 milliseconds |
| Day  8: Unavailable                                                        |            Unsolved |            Unsolved |
| Day  9: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 10: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 11: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 12: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 13: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 14: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 15: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 16: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 17: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 18: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 19: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 20: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 21: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 22: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 23: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 24: Unavailable                                                        |            Unsolved |            Unsolved |
| Day 25: Unavailable                                                        |            Unsolved |            Unsolved |
