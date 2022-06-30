from time import perf_counter
from tools.tools import ReadData

### Parse input ###
data = ReadData("2021/data/12.txt", lines=True, read_int=False)
data.special_split('-')

class PassagePathing:
    def __init__(self, edges) -> None:
        self.nav_dict = {}
        # condtruct navigational dictionary
        for edge in edges:
            # add edge direction one
            if edge[1] != 'start' and edge[0] != 'end':
                if edge[0] not in self.nav_dict:
                    self.nav_dict[edge[0]] = [edge[1]]
                else:
                    self.nav_dict[edge[0]].append(edge[1])
            # add the edge in opposite direction
            if edge[0] != 'start' and edge[1] != 'end':
                if edge[1] not in self.nav_dict:
                    self.nav_dict[edge[1]] = [edge[0]]
                else:
                    self.nav_dict[edge[1]].append(edge[0])
        # Sort keys to match AoC examples
        for key in self.nav_dict:
            self.nav_dict[key].sort()
        # store the found routes
        self.routes = []

    def check_node(self, current_node, route, visited_double):
        current_route = route.copy()
        current_route.append(current_node)
        if current_node == 'end':
            self.routes.append(current_route)
        # check if in small cave without back track option
        else:
            for new_node in self.nav_dict[current_node]:
                if new_node.islower():
                    if visited_double == False:
                        if new_node in current_route:
                            self.check_node(new_node, current_route, visited_double=True)
                        else:
                            cave_maps.find_shortest_route()

                        if new_node not in current_route:
                            self.check_node(new_node, current_route, visited_double)
                else:
                    self.check_node(new_node, current_route, visited_double)

    def find_routes(self, allow_double_small=False):
        route = ['start']
        if allow_double_small:
            for new_node in self.nav_dict['start']:
                self.check_node(new_node, route, visited_double=False)
        else:
            for new_node in self.nav_dict['start']:
                self.check_node(new_node, route, visited_double=True)

    def print_input(self):
        print('Navigation Dictionary:')
        for key in self.nav_dict:
            print(key,'\t', self.nav_dict[key])
        print('\n')

    def print_routes(self):
        print('The found routes are:')
        for i in self.routes:
            print(i)
        print('\n')

    def find_shortest_route(self):
        print('Amount of routes found: ', len(self.routes))
        shortest = float('inf')
        for route in self.routes:
            if len(route) < shortest:
                shortest = len(route)
        print('The shortest route has a length of: ', shortest)


# Part 1
cave_maps = PassagePathing(data)
# cave_maps.print_input()
cave_maps.find_routes(allow_double_small=False)
# cave_maps.print_routes()
cave_maps.find_shortest_route()

# Part 2
cave_maps.find_routes(allow_double_small=True)
cave_maps.find_shortest_route()


# Part 1
start_p1 = perf_counter()

cave_maps = PassagePathing(data)
cave_maps.find_routes(allow_double_small=False)
cave_maps.find_shortest_route()

p1_run_time = perf_counter() - start_p1
print(f'Run time: {round(p1_run_time, 6)}')

# Part 2
start_p2 = perf_counter()

cave_maps.find_routes(allow_double_small=True)
cave_maps.find_shortest_route()

p2_run_time = perf_counter() - start_p2
print(f'Run time: {round(p2_run_time, 6)}')
