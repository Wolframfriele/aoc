"""Day 6 module for solving Advent of Code"""
from itertools import zip_longest
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class Lines:
    """Helps navigating the submarine."""

    def __init__(self, input_data) -> None:
        self.input_data = input_data
        max_x = 0
        max_y = 0
        for lines in input_data:
            for points in lines:
                if points[0] > max_x:
                    max_x = points[0]
                if points[1] > max_y:
                    max_y = points[1]
        self.line_map = []
        for _ in range(max_y + 1):
            empty_horizontal = []
            for _ in range(max_x + 1):
                empty_horizontal.append(0)
            self.line_map.append(empty_horizontal)

    def __repr__(self) -> str:
        output = ""
        for text_line in self.line_map:
            str_line = " ".join("{0}".format(n) for n in text_line)
            str_line += "\n"
            output += str_line
        return output

    def _draw_line(self, start_coor: tuple, end_coor: tuple) -> None:
        """
        Draws line on board, needs a start coordinate and an end coordinate.
        """
        x_direction = 1
        y_direction = 1
        x_start_pad = 0
        x_end_pad = 1
        y_start_pad = 0
        y_end_pad = 1
        if end_coor[0] < start_coor[0]:
            x_direction = -1
            x_start_pad = 0
            x_end_pad = -1
        if end_coor[1] < start_coor[1]:
            y_direction = -1
            y_start_pad = 0
            y_end_pad = -1
        for y, x in zip_longest(range((start_coor[1] + y_start_pad),
                                      (end_coor[1] + y_end_pad), y_direction),
                                range((start_coor[0] + x_start_pad),
                                      (end_coor[0] + x_end_pad), x_direction)):
            if y is None:
                y = start_coor[1]
            if x is None:
                x = end_coor[0]

            self.line_map[y][x] += 1

    def _check_horizontal_or_vertical(self, start_coor: tuple, end_coor: tuple) -> bool:
        """
        Checks if a line is horizontal or vertical.
        """
        return start_coor[0] == end_coor[0] or start_coor[1] == end_coor[1]

    def _find_overlap(self) -> int:
        """
        Counts the amount of points with overlap between lines and returns the count.
        """
        counter = 0
        for y in self.line_map:
            for x in y:
                if x >= 2:
                    counter += 1
        return counter

    def find_danger_zone(self, no_diagonal=True) -> int:
        """
        Finds the dangerous points to travel over, and returns the count.
        """
        for start_coor, end_coor in self.input_data:
            if no_diagonal:
                if self._check_horizontal_or_vertical(start_coor, end_coor):
                    self._draw_line(start_coor, end_coor)
            else:
                self._draw_line(start_coor, end_coor)

        return self._find_overlap()


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 5
        self.test_part_1 = 5
        self.test_part_2 = 12

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        line_coord = ReadData(day, test, lines=True, read_int=False)
        line_coord.special_split(' -> ')
        line_coord.special_split(sign=',', make_int=True)
        return line_coord

    def part_1(self, data):
        """Runs the code for part 1"""
        line_map = Lines(data)
        return line_map.find_danger_zone(no_diagonal=True)

    def part_2(self, data):
        """Runs the code for part 2"""
        line_map = Lines(data)
        return line_map.find_danger_zone(no_diagonal=False)


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
