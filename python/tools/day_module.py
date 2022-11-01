"""
Module that makes running the code of a day easier.
"""
from time import perf_counter
from abc import ABC, abstractmethod


class Timer:
    """
    Simplifies printing the runtime
    """

    def __init__(self, part) -> None:
        self.start = perf_counter()
        self.part = part
        self.run_time = 0.0

    def calculate_run_time(self) -> float:
        """
        Prints the runtime between initializing and calling runtime.
        """
        self.run_time = perf_counter() - self.start
        return self.run_time

    def __repr__(self) -> str:
        return f'Part {self.part} run time: {self.run_time} seconds'


class RunDay(ABC):
    """
    Abstract method that helps with running the code for the day.
    It requires a function to parse data, and to calculate answer
    to part 1 and part 2.
    """

    def __init__(self) -> None:
        self.test_part_1 = None
        self.test_part_2 = None
        self.day = None

    @abstractmethod
    def parse_input(self, day, test=True):
        """Get the data parsed correctly"""

    @abstractmethod
    def part_1(self, data):
        """Return the answer for part 1"""

    @abstractmethod
    def part_2(self, data):
        """Return the answer for part 2"""

    def run(self) -> None:
        """Runs test code until answer matches test case."""
        test_data = self.parse_input(self.day, test=True)
        test_result_p1 = self.part_1(test_data)

        assert test_result_p1 == self.test_part_1, \
        f"Part 1 answer does not match test data. Expected: {self.test_part_1} \
            but received: {test_result_p1}"
        data = self.parse_input(self.day, test=False)
        part1 = Timer(1)
        result_p1 = self.part_1(data)
        run_time_p1 = part1.calculate_run_time()
        print(f'\nDay {self.day} \n')
        print(part1)
        print(f'Answer Part 1: {result_p1} \n')

        if self.test_part_2:
            test_result_p2 = self.part_2(test_data)
            assert test_result_p2 == self.test_part_2, \
            f"Part 2 answer does not match test data. Expected: {self.test_part_2} \
                but received: {test_result_p2}"
            part2 = Timer(2)
            result_p2 = self.part_2(data)
            run_time_p2 = part2.calculate_run_time()
            print(part2)
            print(f'Answer Part 2: {result_p2}')

            percent_increase = round(run_time_p2 / run_time_p1 * 100, 2)
            print(f'Time increase: {percent_increase}% \n')
