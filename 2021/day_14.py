import re
from tools.data import ReadData
# NNCB
### Parse input ###
polymer_template_read = ReadData("2021/data/14_t.txt", lines=True, read_int=False)
polymer_template_read.special_split(' -> ')

class Polymerization(object):
    def __init__(self, polymer_template) -> None:
        # self.poly_template = polymer_template
        self.poly_rules = {}
        for rule in polymer_template:
            pair, insert = rule
            self.poly_rules[pair] = insert
        self.poly = ''
        self.elements = {}
        super().__init__()

    def extend_polymer(self, input_polymer, steps):
        self.poly = input_polymer
        for element in input_polymer:
            self.elements[element] = self.elements.get(element, 0) + 1
        for idx, __ in enumerate(self.poly):
            current_pair = self.poly[idx-1:idx+1]
            self.split_pair(current_pair, steps)

    def split_pair(self, pair, ttl):
        alive = ttl > 0
        if pair in self.poly_rules and alive:
            insert = self.poly_rules[pair]
            self.elements[insert] = self.elements.get(insert, 0) + 1
            pair1, pair2 = pair[0] + insert, insert + pair[1]
            self.split_pair(pair1, ttl - 1)
            self.split_pair(pair2, ttl - 1)
            print(self.elements, ttl)
    
    def commom_elements(self):
        min_value, min_key, max_value, max_key = float('inf'), '', 0, ''
        for key, value in self.elements.items():
            if value < min_value:
                min_value, min_key = value, key
            if value > max_value:
                max_value, max_key = value, key
        print(f'Most common: {max_value, max_key}, least common: {min_value, min_key}')
        print(f'answer = {max_value - min_value}')

# Part 1
poly = Polymerization(polymer_template_read)
poly.extend_polymer('NNCB', steps=10) # Test code
# poly.extend_polymer('SHHBNFBCKNHCNOSHHVFF', steps=10) # Test code
poly.commom_elements()
