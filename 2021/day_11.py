import numpy as np
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/11.txt", lines=True, read_int=False)

class SimulateFlashes(object):
    def __init__(self, octo_map) -> None:
        self.step = 0
        temp = []
        for line in octo_map:
            temp.append([int(i) for i in line])
        self.octo_map = np.array(temp)
        self.flashed_in_iteration = np.zeros((10, 10))
        self.flash_counter = 0
        self.sync = False
        super().__init__()

    def print_state(self):
        print(self.octo_map)

    def increment_step(self):
        self.step += 1
        self.octo_map += 1
        it = np.nditer(self.octo_map, flags=['multi_index'])
        for i in it:
            if i > 9:
                self.flash(it.multi_index)
        # self.print_state()
        it_2 = np.nditer(self.flashed_in_iteration, flags=['multi_index'])
        for i in it_2:
            if i == 1:
                self.octo_map[it_2.multi_index] = 0
        if np.sum(self.flashed_in_iteration) == 100:
            self.sync = True
        self.flashed_in_iteration = np.zeros((10, 10))
    
    def flash(self, index):
        y, x = index
        if 0 <= x <= 9 and 0 <= y <= 9:
            self.flashed_in_iteration[index] = 1
            self.flash_counter += 1
            dir = [(1, -1), (0, -1), (-1, -1), (-1, 0),
                   (-1, 1), (0, 1), (1, 1), (1, 0)]
            for d in dir:
                self.increment_pos((y + d[0], x + d[1]))
            self.octo_map[index] = 0

    def increment_pos(self, index):
        if 0 <= index[0] <= 9 and 0 <= index[1] <= 9:
            self.octo_map[index] += 1
            if self.octo_map[index] > 9 and self.flashed_in_iteration[index] == 0:
                self.flash(index)

    def simulate_for(self, end_step):
        for i in range(1, end_step + 1):
            self.increment_step()
            print(f'Step: {self.step}, amount of flashes: {self.flash_counter}')

    def simulate_till_sync(self):
        while not self.sync:
            self.increment_step()
            print(f'Step: {self.step}, amount of flashes: {self.flash_counter}')
        return self.step

# Part 1
octos = SimulateFlashes(data)
# octos.simulate_for(100)

# Part 2
print(octos.simulate_till_sync())