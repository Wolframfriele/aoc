import numpy as np
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/7.txt", lines=False, read_int=False)
data.special_split(",", make_int=True)

# print(data)
class CrabLine(object):
    def __init__(self, crab_positions) -> None:
        self.crab_positions = np.array(crab_positions)
        super().__init__()

    def calc_cost(self, pos, crab_engineering=False):
        total_cost = 0
        for i in self.crab_positions:
            if crab_engineering:
                dist = abs(i - pos)
                total_cost += int(dist * (dist+1) / 2)
            else:
                total_cost += abs(i - pos)
        return total_cost

    def find_cheapest(self, crab_engineering=False):
        cheapest_pos = 0
        cheapest_cost = float("inf")

        search_start = np.median(self.crab_positions)

        for pos in np.arange(search_start, self.crab_positions.max()):
            curr_cost = self.calc_cost(pos, crab_engineering)
            # print(pos, curr_cost)
            if curr_cost < cheapest_cost:
                cheapest_cost = curr_cost
                cheapest_pos = pos
            else:
                break

        for pos in np.arange((search_start - 1), self.crab_positions.min()):
            curr_cost = self.calc_cost(pos, crab_engineering)
            # print(pos, curr_cost)
            if curr_cost < cheapest_cost:
                cheapest_cost = curr_cost
                cheapest_pos = pos
            else:
                break

        return int(cheapest_pos), int(cheapest_cost)

crab_help = CrabLine(data)
print(crab_help.find_cheapest(crab_engineering=True))
