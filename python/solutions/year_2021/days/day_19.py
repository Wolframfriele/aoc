from tools.tools import ReadData, RunDay


class Matchy:
    def __init__(self, rules) -> None:
        pass

class Day19(RunDay):
    def __init__(self) -> None:
        self.day = 19
        self.test_part_1 = 2
        self.test_part_2 = 3

    def parse_input(self, day, test=True):
        start_data = ReadData(day, test, lines=False, read_int=False)
        start_data.special_split('\n\n')
        start_data.special_split('\n')
        return start_data

    def part_1(self, data):
        print(data)

        return 1

    def part_2(self, data):
        return 2


def main():
    today = Day19()
    today.run()


if __name__ == '__main__':
    main()
