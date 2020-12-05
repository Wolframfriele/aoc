import math


# Import Boarding Passes into list
boarding_passes_input = open('boarding_passes.txt', 'r')
boarding_passes = boarding_passes_input.read().split()
boarding_passes_input.close()


# Define boarding pass class
class ReadBoardingPass(object):
    def __init__(self, boarding_passes_list):
        self.boarding_passes = boarding_passes_list

    def __len__(self):
        return len(self.boarding_passes)

    def find_row(self, index):
        """'Finds the row for a boarding pass given as an index"""
        row_upp_limit = 127
        row_low_limit = 0
        for char in self.boarding_passes[index][:7]:
            if char == 'F':
                row_upp_limit = (row_upp_limit - ((row_upp_limit - row_low_limit) // 2)) - 1
            if char == 'B':
                row_low_limit = 1 + (row_low_limit + ((row_upp_limit - row_low_limit) // 2))
        return row_low_limit

    def find_column(self, index):
        """"Finds the column for a boarding pass given as an index"""
        row_upp_limit = 7
        row_low_limit = 0
        for char in self.boarding_passes[index][7:]:
            if char == 'L':
                row_upp_limit = (row_upp_limit - ((row_upp_limit - row_low_limit) // 2)) - 1
            if char == 'R':
                row_low_limit = 1 + (row_low_limit + ((row_upp_limit - row_low_limit) // 2))
        return row_low_limit

    def return_id(self, index):
        """"Returns the id for a boarding pass given as an index"""
        row = self.find_row(index)
        column = self.find_column(index)
        return (row * 8) + column


boarding = ReadBoardingPass(boarding_passes)

id_list = []
for i in range(len(boarding)):
    id_list.append(boarding.return_id(i))

print(sorted(id_list)[-1:])


