import re
from tools.data import ReadData
# NNCB
### Parse input ###
polymer_template_read = ReadData("2021/data/14.txt", lines=True, read_int=False)
polymer_template_read.special_split(' -> ')

class Polymerization(object):
    def __init__(self, polymer_template) -> None:
        # self.poly_template = polymer_template
        self.poly_rules = {}
        for rule in polymer_template:
            pair, insert = rule
            self.poly_rules[pair] = insert
        self.poly = ''
        super().__init__()

    def extend_polymer(self, input_polymer, steps):
        self.poly = input_polymer
        for __ in range(steps):
            print(__)
            changes = []
            for idx, __ in enumerate(self.poly):
                current = self.poly[idx-1:idx+1]
                if current in self.poly_rules:
                    insert = self.poly_rules[current]
                    changes.append((idx, insert))
            changes.sort()
            for i, change in enumerate(changes):
                idx, insert = change
                self.poly = self.poly[:idx + i] + insert + self.poly[idx + i:]
    
    def commom_elements(self):
        check_values = set(self.poly)
        amounts = []
        for value in check_values:
            count = self.poly.count(value)
            amounts.append((count, value))
        amounts.sort()
        most_common, least_common = amounts[-1], amounts[0]
        print(f'Most common: {most_common}, least common: {least_common}')
        print(f'answer = {most_common[0] - least_common[0]}')

# Part 1
poly = Polymerization(polymer_template_read)
# poly.extend_polymer('NNCB', steps=10) # Test code
poly.extend_polymer('SHHBNFBCKNHCNOSHHVFF', steps=40) # Test code
poly.commom_elements()

# Part 2
