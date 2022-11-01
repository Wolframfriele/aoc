"""Day 7 module for solving Advent of Code"""
import numpy as np
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class CrabLine:
    """
    Class that helps with calculating most efficient crab goal position.
    """

    def __init__(self, crab_positions) -> None:
        self.crab_positions = np.array(crab_positions)

    def calc_cost(self, pos, crab_engineering=False):
        """
        Calculates the cost of moving the crabs to a certain position.
        """
        total_cost = 0
        for crab in self.crab_positions:
            dist = abs(crab - pos)
            if crab_engineering:
                total_cost += int(dist * (dist + 1) / 2)
            else:
                total_cost += dist
        return total_cost

    def find_cheapest(self, crab_engineering=False):
        """
        Calculates the cheapest position for the crabs to move to.
        """
        cheapest_cost = float("inf")

        if crab_engineering:
            cheapest_pos = int(np.mean(self.crab_positions))
        else:
            cheapest_pos = int(np.median(self.crab_positions))

        # Check if values to the right of center are cheaper
        for pos in np.arange(cheapest_pos, self.crab_positions.max()):
            curr_cost = self.calc_cost(pos, crab_engineering)
            if curr_cost < cheapest_cost:
                cheapest_cost = curr_cost
                cheapest_pos = pos
            else:
                break

        # Check if values to the left of center are cheaper
        for pos in np.arange((cheapest_pos - 1), self.crab_positions.min(), -1):
            curr_cost = self.calc_cost(pos, crab_engineering)
            if curr_cost < cheapest_cost:
                cheapest_cost = curr_cost
                cheapest_pos = pos
            else:
                break
        return int(cheapest_pos), int(cheapest_cost)


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 7
        self.test_part_1 = 37
        self.test_part_2 = 168

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        data = ReadData(day, test, lines=False, read_int=False)
        data.special_split(",", make_int=True)
        return data

    def part_1(self, data):
        """Runs the code for part 1"""
        crab_help = CrabLine(data)
        return crab_help.find_cheapest(crab_engineering=False)[1]

    def part_2(self, data):
        """Runs the code for part 2"""
        crab_help = CrabLine(data)
        return crab_help.find_cheapest(crab_engineering=True)[1]


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
