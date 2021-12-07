import math
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/7_t.txt", lines=False, read_int=False)
data.special_split(",")
horizontal_pos = [int(i) for i in data]

# print(horizontal_pos)
### Solutions ###

def calc_cost(pos_list, pos):
    total_cost = 0
    for i in pos_list:
        total_cost += abs(i - pos)
    
    return total_cost

def find_cheapest(pos_list):
    cheapest_pos = 0
    cheapest_cost = sum(pos_list)
    for pos in range(max(pos_list)+1):
        curr_cost = calc_cost(pos_list, pos)
        # print(pos, curr_cost)
        if curr_cost < cheapest_cost:
            cheapest_cost = curr_cost
            cheapest_pos = pos
    return cheapest_pos, cheapest_cost

print("Cheapest", find_cheapest(horizontal_pos))