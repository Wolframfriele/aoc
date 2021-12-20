from tools.data import ReadData

### Parse input ###
polymer_rules_read = ReadData("2021/data/14.txt", lines=True, read_int=False)
polymer_rules_read.special_split(' -> ')

class Polymerization(object):
    def __init__(self, polymer_rules) -> None:
        self.poly_rules = {pair:ins for pair, ins in polymer_rules}
        self.pairs = {pair:0 for pair, __ in polymer_rules}
        self.elements = {}
        super().__init__()

    def extend_polymer(self, polymer_template, steps):
        for idx, __ in enumerate(polymer_template):
            pair = polymer_template[idx-1:idx+1]
            if pair in self.pairs:
                self.pairs[pair] += 1
        for __ in range(steps):
            self.poly_extend_iteration()
        self.update_elements()
        self.commom_elements()

    def poly_extend_iteration(self):
        itr_pairs = {pair:0 for pair, __ in self.poly_rules.items()}
        for pair, amount in self.pairs.items():
            if amount > 0:
                insert = self.poly_rules[pair]
                pair1, pair2 = pair[0] + insert, insert + pair[1]
                itr_pairs[pair1] += amount
                itr_pairs[pair2] += amount
        for key, value in itr_pairs.items():
            self.pairs[key] = value

    def update_elements(self):
        elements = {}
        for pair, amount in self.pairs.items():
            element1, element2 = pair
            elements[element1] = elements.get(element1, 0) + amount
            elements[element2] = elements.get(element2, 0) + amount
        for key, value in elements.items():
            elements[key] = value
        self.elements = elements

    def commom_elements(self):
        min_value, min_key, max_value, max_key = float('inf'), '', 0, ''
        for key, value in self.elements.items():
            if value < min_value:
                min_value, min_key = value, key
            if value > max_value:
                max_value, max_key = value, key
        print(f'Most common: {max_value, max_key}, least common: {min_value, min_key}')
        print(f'answer = {(max_value - min_value) // 2}')

# Part 1
poly = Polymerization(polymer_rules_read)
# poly.extend_polymer('NNCB', steps=40) # Test code
poly.extend_polymer('SHHBNFBCKNHCNOSHHVFF', steps=10)