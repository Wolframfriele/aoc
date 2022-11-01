"""
File that serves as a template for all off the days
"""
from tools.tools import ReadData, RunDay


class Thingy:
    def __init__(self) -> None:
        pass


class Day1(RunDay):
    def __init__(self) -> None:
        self.day = 1
        self.test_part_1 = 7
        self.test_part_2 = 5

    def parse_input(self, day, test=True):
        return ReadData(day, test, lines=True, read_int=True)

    def part_1(self, data):
        run = Thingy()
        return run.check_increasing(data)

    def part_2(self, data):
        run = Thingy()
        return run.check_window_increasing(data)


def main():
    today = Day1()
    today.run()

if __name__ == '__main__':
    main()
