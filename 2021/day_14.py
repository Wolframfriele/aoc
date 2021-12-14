import re
from tools.data import ReadData
# NNCB
### Parse input ###
polymer_template_read = ReadData("2021/data/14_t.txt", lines=True, read_int=False)
polymer_template_read.special_split(' -> ')

class Polymerization(object):
    def __init__(self, polymer_template) -> None:
        self.poly_template = polymer_template
        self.poly = ''
        super().__init__()

    def extend_polymer(self, input_polymer, steps):
        self.poly = input_polymer
        for __ in range(steps):
            changes = []
            for rule in self.poly_template:
                pair, insert = rule
                result = re.finditer(pair, self.poly, flags=0)
                for i in result:
                    if __ == 2 and pair == 'BB':
                        print(i.span())
                    index = i.span()[0] + 1
                    if index > 0:
                        changes.append((index, insert))

            changes.sort()
            for i, change in enumerate(changes):
                index, insert = change
                self.poly = self.poly[:index + i] + insert + self.poly[index + i:]
        print(changes)
        print('step 2: \t', 'NBCCNBBBCBHCB')
        print('actual: \t', self.poly)
        print('step 3: \t', 'NBBBCNCCNBBNBNBBCHBHHBCHB')
        print(self.poly == 'NBBBCNCCNBBNBNBBCHBHHBCHB')


# Part 1
poly = Polymerization(polymer_template_read)
poly.extend_polymer('NNCB', steps=3)

# Part 2
