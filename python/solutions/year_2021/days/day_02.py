"""Day 2 module for solving Advent of Code"""
from tools.data_helpers import ReadData
from tools.day_module import RunDay


def execute_commands(commands: list[str], use_aim=False) -> int:
    """Execute the commands and return the final position"""
    horizontal_pos, depth, aim = 0, 0, 0
    for command in commands:
        direction, amount = command
        amount = int(amount)
        if direction == "forward":
            horizontal_pos += amount
            if use_aim:
                depth += aim * amount
        elif direction == "down":
            if use_aim:
                aim += amount
            else:
                depth += amount
        elif direction == "up":
            if use_aim:
                aim -= amount
            else:
                depth -= amount
    return horizontal_pos * depth


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 2
        self.test_part_1 = 150
        self.test_part_2 = 900

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        steer_commands = ReadData(day, test, lines=True, read_int=False)
        steer_commands.special_split()
        return steer_commands

    def part_1(self, data):
        """Runs the code for part 1"""
        return execute_commands(data)

    def part_2(self, data):
        """Runs the code for part 2"""
        return execute_commands(data, use_aim=True)


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
