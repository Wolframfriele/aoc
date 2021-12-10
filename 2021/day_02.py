import numpy as np
from tools.data import ReadData

### Parse input ###
steer_commands = ReadData("2021/data/2.txt", lines=True, read_int=False)
steer_commands.special_split()

class SteerSubmarine(object):
    def __init__(self, commands) -> None:
        self.commands = commands
        self.horizontal_position = 0
        self.depth = 0
        super().__init__()
    
    def execute_commands_p1(self):
        for command in self.commands:
            direction, amount = command
            amount = int(amount)
            if direction == "forward":
                self.horizontal_position += amount
            elif direction == "down":
                self.depth += amount
            elif direction == "up":
                self.depth -= amount

    def execute_commands(self):
        aim = 0
        for command in self.commands:
            direction, amount = command
            amount = int(amount)
            if direction == "forward":
                self.horizontal_position += amount
                self.depth += aim * amount
            elif direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount

    def get_position(self):
        return self.horizontal_position * self.depth

    def reset_position(self):
        self.horizontal_position = 0
        self.depth = 0
# Part 1
submarine = SteerSubmarine(steer_commands)
submarine.execute_commands_p1()
print(submarine.get_position())

# Part 2
submarine.reset_position()
submarine.execute_commands()
print(submarine.get_position())