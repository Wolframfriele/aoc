from time import perf_counter
import numpy as np
from ..tools.tools import ReadData

### Parse input ###
data = ReadData("2021/data/11.txt", lines=True, read_int=False)

class SimulateFlashes:
    def __init__(self, octo_map) -> None:
        self.step = 0
        self.flash_counter = 0
        self.sync = False
        self.octo_map = np.array([[int(i) for i in line] for line in octo_map])
        self.flashed_in_iteration = np.zeros((10, 10))

    def increment_step(self):
        self.step += 1
        self.octo_map += 1
        iter = np.nditer(self.octo_map, flags=['multi_index'])
        for i in iter:
            if i > 9:
                self.flash(iter.multi_index)
        iter_2 = np.nditer(self.flashed_in_iteration, flags=['multi_index'])
        for i in iter_2:
            if i == 1:
                self.octo_map[iter_2.multi_index] = 0
        if np.sum(self.flashed_in_iteration) == 100:
            self.sync = True
        self.flashed_in_iteration = np.zeros((10, 10))

    def flash(self, index):
        direction = ((1, -1), (0, -1), (-1, -1), (-1, 0),
                   (-1, 1), (0, 1), (1, 1), (1, 0))
        y, x = index
        if 0 <= x <= 9 and 0 <= y <= 9:
            self.flashed_in_iteration[index] = 1
            self.flash_counter += 1
            for d in direction:
                d_y, d_x = d
                self.increment_pos((y + d_y, x + d_x))
            self.octo_map[index] = 0

    def increment_pos(self, index):
        if 0 <= index[0] <= 9 and 0 <= index[1] <= 9:
            self.octo_map[index] += 1
            if self.octo_map[index] > 9 and self.flashed_in_iteration[index] == 0:
                self.flash(index)

    def simulate(self, end_step=False, show_steps=False):
        if end_step:
            for __ in range(1, end_step + 1):
                self.increment_step()
                if show_steps:
                    print(f'{self.step}, {self.flash_counter}')
        else:
            while not self.sync:
                self.increment_step()
                if show_steps:
                    print(f'{self.step}, {self.flash_counter}')
        return self.step, self.flash_counter

# Part 1
start_p1 = perf_counter()

octos = SimulateFlashes(data)
print(octos.simulate(100))

p1_run_time = perf_counter() - start_p1
print(f'Run time: {round(p1_run_time, 6)}')

# Part 2
start_p2 = perf_counter()

print(octos.simulate())

p2_run_time = perf_counter() - start_p2
print(f'Run time: {round(p2_run_time, 6)}')
