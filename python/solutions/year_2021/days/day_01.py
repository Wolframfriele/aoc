"""Day 1 module for solving Advent of Code"""
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class DepthChecker:
    """Checks the depth of the submarine"""

    def check_increasing(self, sea_depth: list[int]) -> int:
        """Checks for how many steps the depth increases."""
        curr_depth = sea_depth[0]
        counter = 0
        for depth in sea_depth:
            if depth > curr_depth:
                counter += 1
            curr_depth = depth
        return counter

    def check_window_increasing(self, sea_depth: list[int], window_size=3) -> int:
        """Checks if a certain window size is increasing in depth."""
        curr_depth = sum(sea_depth[:window_size])
        counter = 0
        for i, __ in enumerate(sea_depth):
            if i + 2 <= len(sea_depth):
                sliding_window = sum(sea_depth[i:i + window_size])

                if sliding_window > curr_depth:
                    counter += 1

            curr_depth = sliding_window
        return counter


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 1
        self.test_part_1 = 7
        self.test_part_2 = 5

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        return ReadData(day, test, lines=True, read_int=True)

    def part_1(self, data):
        """Runs the code for part 1"""
        checker = DepthChecker()
        return checker.check_increasing(data)

    def part_2(self, data):
        """Runs the code for part 2"""
        checker = DepthChecker()
        return checker.check_window_increasing(data)


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
