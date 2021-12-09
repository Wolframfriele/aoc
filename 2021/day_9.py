import numpy as np
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/9.txt", lines=True, read_int=False)
height_map = [list(map(int, i)) for i in data]

# print(height_map)
class MapChecker(object):
    def __init__(self, height_map) -> None:
        self.height_map = height_map
        self.lowest_points = []
        self.max_x = len(self.height_map[0]) - 1
        self.max_y = len(self.height_map) - 1
        super().__init__()
    
    def get_height(self, point):
        x, y = point
        if x < 0 or y < 0 or x > self.max_x or y > self.max_y:
            return 10
        else:
            return self.height_map[y][x]

    def get_neighboors_height(self, point):
        x, y = point
        above = self.get_height((x, y - 1))
        below = self.get_height((x, y + 1))
        left = self.get_height((x - 1, y))
        right = self.get_height((x + 1, y))
        return above, below, left, right

    def check_if_lowest(self, point):
        above, below, left, right = self.get_neighboors_height(point)
        h = self.get_height(point)
        if h < above and h < below and h < left and h < right:
            self.lowest_points.append(point)
            return self.get_height(point) + 1
        return 0

    def find_lowest_points(self):
        self.risk = 0
        for y in range(len(self.height_map)):
            for x in range(len(self.height_map[0])):
                lowest = self.check_if_lowest((x, y))
                if lowest:
                    self.risk += lowest
        return self.lowest_points

    def get_risk(self):
        return self.risk

    def generate_fill_map(self):
        self.fill_map = []
        for y in self.height_map:
            self.fill_map.append([1 if x < 9 else 0 for x in y])

    def get_fill_point(self, point):
        x, y = point
        if x < 0 or y < 0 or x > self.max_x or y > self.max_y:
            return 0
        else:
            return self.fill_map[y][x]

    def set_point(self, point, value=0):
        self.fill_map[point[1]][point[0]] = value

    def boundary_fill(self, point, boundary=0, fill_value=0):
        x, y = point
        if self.get_fill_point(point):
            self.basin_size += 1
            self.set_point(point)
            self.boundary_fill((x - 1, y), boundary, fill_value)
            self.boundary_fill((x + 1, y), boundary, fill_value)
            self.boundary_fill((x, y - 1), boundary, fill_value)
            self.boundary_fill((x, y + 1), boundary, fill_value)

    def find_basin_sizes(self):
        self.basin_sizes = []
        for point in self.lowest_points:
            self.basin_size = 0
            self.boundary_fill(point)
            self.basin_sizes.append(self.basin_size)
        return self.basin_sizes

    def get_largest_basins(self):
        self.basin_sizes.sort(reverse=True)
        return self.basin_sizes[0] * self.basin_sizes[1] * self.basin_sizes[2]

# Part 1
cave_map = MapChecker(height_map)
cave_map.find_lowest_points()
print(cave_map.get_risk())

# part 2
cave_map.generate_fill_map()
cave_map.find_basin_sizes()
print(cave_map.get_largest_basins())
