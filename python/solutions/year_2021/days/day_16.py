"""
Decode the structure of your hexadecimal-encoded BITS transmission;
what do you get if you add up the version numbers in all packets?
"""
from tools.tools import ReadData, Timer

class BITSReader:
    conversion_dict = {
                        '0': '0000', '1': '0001', '2': '0010',
                        '3': '0011', '4': '0100', '5': '0101',
                        '6': '0110', '7': '0111', '8': '1000',
                        '9': '1001', 'A': '1010', 'B': '1011',
                        'C': '1100', 'D': '1101', 'E': '1110',
                        'F': '1111'
    }

    def __init__(self, hex_string) -> None:
        self.bit_string = ''
        for char in hex_string:
            self.bit_string += self.conversion_dict[char]
        self.version = int(self.bit_string[:3], 2)
        self.type_id = int(self.bit_string[3:6], 2)


def main():
    ### Parse input ###
    data = ReadData(16, test=True, lines=False, read_int=False)
    reader = BITSReader(data)

    # Part 1
    part1 = Timer(1)

    part1.run_time()

    # Part 2
    part2 = Timer(2)

    part2.run_time()

if __name__ == '__main__':
    main()
