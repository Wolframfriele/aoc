from itertools import zip_longest
from tools.data import ReadData

### Parse input ###
line_coord = ReadData("2021/data/5_t.txt", lines=True, read_int=False)
line_coord.special_split(' -> ')
line_coord.special_split(',', make_int=True)

class Lines(object):
    def __init__(self, input_data):
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
        for y in range(max_y + 1):
            empty_horizontal = []
            for x in range(max_x + 1):
                empty_horizontal.append(0)
            self.line_map.append(empty_horizontal)
    
    def __repr__(self):
        output = ""
        for text_line in self.line_map:
            str_line = " ".join("{0}".format(n) for n in text_line)
            str_line += "\n"
            output += str_line
        return output

    def draw_line(self, start_coor, end_coor):
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
        for y, x in zip_longest(range((start_coor[1] + y_start_pad), (end_coor[1] + y_end_pad), y_direction), 
                                range((start_coor[0] + x_start_pad), (end_coor[0] + x_end_pad), x_direction)):          
            if y == None:
                y = start_coor[1]
            if x == None:
                x = end_coor[0]

            self.line_map[y][x] += 1
        
    def check_horizontal_or_vertical(self, start_coor, end_coor):
        return start_coor[0] == end_coor[0] or start_coor[1] == end_coor[1]

    def find_overlap(self):
        counter = 0
        for y in self.line_map:
            for x in y:
                if x >= 2:
                    counter += 1
        return counter

    def find_danger_zone(self, no_diagonal=True):
        for start_coor, end_coor in self.input_data:
            if no_diagonal:
                if self.check_horizontal_or_vertical(start_coor, end_coor):
                    self.draw_line(start_coor, end_coor)
            else:
                self.draw_line(start_coor, end_coor)
        
        return self.find_overlap()

# Part 1 (no_diagonal=True)
line_map = Lines(line_coord)
print(line_map.find_danger_zone(no_diagonal=True))
# Part 2 (no_diagonal=False)
print(line_map.find_danger_zone(no_diagonal=False))
