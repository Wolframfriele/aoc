import math
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/7.txt", lines=False, read_int=False)
data.special_split(",")
horizontal_pos = [int(i) for i in data]

# print(horizontal_pos)
### Solutions ###

def calc_cost(pos_list, pos, crab_engineering=False):
    total_cost = 0
    for i in pos_list:
        if crab_engineering:
            dist = abs(i - pos)
            total_cost += int(dist * (dist+1) / 2)

        else:
            total_cost += abs(i - pos)
    
    return total_cost

def find_cheapest(pos_list, crab_engineering=False):
    cheapest_pos = 0
    cheapest_cost = 10000000000000000000000
    for pos in range(max(pos_list)+1):
        curr_cost = calc_cost(pos_list, pos, crab_engineering)
        # print(pos, curr_cost)
        if curr_cost < cheapest_cost:
            cheapest_cost = curr_cost
            cheapest_pos = pos
    return cheapest_pos, cheapest_cost

print("Cheapest", find_cheapest(horizontal_pos, crab_engineering=True))

#101571302