import numpy as np
from tools.data import ReadData

### Parse input ###
sea_depth = ReadData("2021/data/1.txt", lines=True, read_int=True)

class DepthChecker(object):
    def __init__(self, sea_depth) -> None:
        self.sea_depth = np.array(sea_depth)
        super().__init__()

    def check_increasing(self):
        curr_depth = sea_depth[0]
        counter = 0
        for i in self.sea_depth:
            if i > curr_depth:
                counter += 1
            curr_depth = i
        return counter
    
    def check_window_increasing(self):
        curr_depth = self.sea_depth[0] + self.sea_depth[1] + self.sea_depth[2]
        counter = 0
        for i in range(len(sea_depth)):
            try:
                sliding_window = self.sea_depth[i] + self.sea_depth[(i+1)] + self.sea_depth[(i+2)]
            except IndexError:
                break
            if sliding_window > curr_depth:
                counter += 1

            curr_depth = sliding_window
        return counter

checker = DepthChecker(sea_depth)
print("Part 1: ", checker.check_increasing())
print("Part 2: ", checker.check_window_increasing())
