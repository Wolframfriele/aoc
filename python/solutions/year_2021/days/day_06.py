"""Day 6 module for solving Advent of Code"""
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class LantarnFish:
    """Class to simulate the behaviour of lantarn fish"""

    def __init__(self, start_population) -> None:
        self.age_previous_day = {0: 0, 1: 0, 2: 0,
                                 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

        for fish in start_population:
            self.age_previous_day[fish] += 1

    def _new_day(self) -> None:
        """
        Simulates one new day of lantarn fish.
        """
        age_new_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for age in age_new_day:
            if age == 0:
                age_new_day[6] = self.age_previous_day[0]
                age_new_day[8] = self.age_previous_day[0]
            else:
                age_new_day[age - 1] += self.age_previous_day[age]
        self.age_previous_day = age_new_day

    def simulate_fish(self, days: int) -> int:
        """
        Simulates for certain amount of days.
        """
        for __ in range(days):
            self._new_day()
        return sum(self.age_previous_day.values())


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 6
        self.test_part_1 = 5934
        self.test_part_2 = 26984457539

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        lantern_start_pop = ReadData(day, test, lines=False, read_int=False)
        lantern_start_pop.special_split(',', make_int=True)
        return lantern_start_pop

    def part_1(self, data):
        """Runs the code for part 1"""
        lantarn_sim = LantarnFish(data)
        return lantarn_sim.simulate_fish(80)

    def part_2(self, data):
        """Runs the code for part 2"""
        lantarn_sim = LantarnFish(data)
        return lantarn_sim.simulate_fish(256)


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
