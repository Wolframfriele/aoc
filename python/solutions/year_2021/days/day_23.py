from unittest import TestCase
from queue import Queue
from dataclasses import dataclass

A = 1
B = 10
C = 100
D = 1000

# never stop on the space immediately outside any room

# move from the hallway into a room (unless destination)

# it will stay in that spot until it can move into a room


## Convert to graph

#   ABCDEFGHIJKLMN
# 1"#############" Way to represent coordinates, left to right If somethig is # ignore it.
# 2"#...........#" If something is a . add it as a node + check neighbors and add those as directions
# 3"###B#C#B#D###" Each letter is tied to a location
# 4"  #A#D#C#A#  "   
# 5"  #########  " 

## Possible graph representations

# {
#   "C2": ["D2"],
#   "D2": ["C2", "E2"]
# }
# amphipod = {
#   position, goal, movement_cost
# }

@dataclass
class Amphipod:
    position: str
    goal: str
    movement_cost: int


class Parser:

    def __init__(self, input: str) -> None:
        self.input = input

    def get_walls(self, input: str) -> None:
        pass

@dataclass
class Graph:
    pass    

class Solver:

    def __init__(self) -> None:
        self.frontier = Queue()
        self.reached = set()

    def __extract_starting_position(self):
        pass

    def __build_graph(self):
        pass

    def __solve(self):
        while not self.frontier.empty():
            current = self.frontier.get()
            for next in graph.neighbors(current):
                if next not in self.reached:
                    self.frontier.put(next)
                    self.reached.add(next)

    def part_a(self, input: str):
        self.reached.add(start)
        self.frontier.put(start)


        


class PartATestCases(TestCase):

    def SetUp(self):
        self.solver = Solver()

    def test_case_a(self):
        input = (
            "#############"
            "#...........#"
            "###B#C#B#D###"
            "  #A#D#C#A#"
            "  #########  "
        )
        expected = 12521
        self.assertEqual(self.solver.part_a(input=input), expected)


def main():
    """Run the main function"""
    part_a_input = (
        "#############"
        "#...........#"
        "###B#B#C#D###"
        "  #D#C#A#A#  "
        "  #########  "
    )
    
    solver = Solver()
    print(solver.part_a(input=part_a_input))


if __name__ == '__main__':
    main()
