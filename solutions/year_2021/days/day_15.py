import numpy as np
from queue import PriorityQueue
from tools.tools import ReadData

### Parse input ###
risk_map = ReadData("2021/data/15.txt", lines=True, read_int=False)

class Graph:
    dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
    def __init__(self, weighted_grid):
        self.grid = np.array([list(map(int, i)) for i in list(map(list, weighted_grid))])
        self.max_x = len(self.grid[0]) - 1
        self.max_y = len(self.grid) - 1

    def get_neighbors(self, node):
        neighbors = []
        x, y = node
        for d in self.dirs:
            new_x, new_y = x + d[0], y + d[1]
            x_in_range = 0 <= new_x <= self.max_x
            y_in_range = 0 <= new_y <= self.max_y
            if x_in_range and y_in_range:
                neighbors.append((new_x, new_y))
        return neighbors

    def get_weight(self, nodes):
        risk = []
        for node in nodes:
            x, y = node
            risk.append(self.grid[y, x])
        return risk

    def extend_graph(self, times):
        new_graph = self.grid
        extend_x = self.grid
        for __ in range(times):
            extend_x = (extend_x + 1) % 10
            if_zero = extend_x == 0
            extend_x[if_zero] = 1
            new_graph = np.append(new_graph, extend_x, 1)
        extend_y = new_graph
        for __ in range(times):
            extend_y = (extend_y + 1) % 10
            if_zero = extend_y == 0
            extend_y[if_zero] = 1
            new_graph = np.append(new_graph, extend_y, 0)
        self.grid = new_graph
        # Update max values
        self.max_x = len(self.grid[0]) - 1
        self.max_y = len(self.grid) - 1

class FindShortest:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.lowest_weight = {}
        self.explore = PriorityQueue()
        super().__init__()

    def find_route(self, start=(0,0), goal=None):
        if goal is None:
            goal = (self.graph.max_x, self.graph.max_y)

        # label nodes to inf except start
        self.lowest_weight[start] = 0
        self.explore.put((self.lowest_weight[start], start))
        
        while not self.explore.empty():
            current = self.explore.get()
            current_weight_in_queue, current_node = current
            current_lowest_weight = self.lowest_weight[current_node]
            if current_lowest_weight == current_weight_in_queue:
                neighbors = self.graph.get_neighbors(current_node)
                neighbor_weights = self.graph.get_weight(neighbors)
                
                # Update lowest found dictionary
                for neighbor_weight, neighbor in zip(neighbor_weights, neighbors):
                    neighbor_total_weight = current_lowest_weight + neighbor_weight
                    if neighbor_total_weight < self.lowest_weight.get(neighbor, float('inf')):
                        self.lowest_weight[neighbor] = neighbor_total_weight
                        self.explore.put((neighbor_total_weight, neighbor))
                    
        return self.lowest_weight[goal]

# Part 1
# graph = Graph(risk_map)
# maps = FindShortest(graph)
# print(maps.find_route())

# Part 2
graph = Graph(risk_map)
graph.extend_graph(4)
maps = FindShortest(graph)
print(maps.find_route())
