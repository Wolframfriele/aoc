"""
Tools that make parsing the advent of code data easier.
"""

from functools import partial


class ReadData:
    """
    Helper function to read advent of code input data from text files.
    Has options to directly convert to lists and integers.
    """

    def __init__(self, day=1, test=True, lines=True, read_int=False) -> None:
        folder = 'solutions/year_2021/data/'
        if test:
            path = f'{folder}{day}_t.txt'
        else:
            path = f'{folder}{day}.txt'
        with open(path, "r") as file:
            if lines:
                if read_int:
                    self.data = [int(line.rstrip('\n')) for line in file]
                else:
                    self.data = [line.rstrip('\n') for line in file]
            else:
                self.data = file.read()

    def __repr__(self) -> str:
        return str(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int):
        return self.data[index]

    def pop_data(self, index: int):
        """
        Pops element at index
        """
        return self.data.pop(index)

    def recursive_split(self, data, sign=None, make_int=False):
        """
        Helper function to recursively split input data.
        This helps with handeling situations whith lists in lists.
        """
        if isinstance(data, str):
            if make_int:
                return_data = [int(i) for i in data.split(sign)]
            else:
                return_data = data.split(sign)
        else:
            if isinstance(data[0], str):
                if make_int:
                    temp = [i.split(sign) for i in data]
                    return_data = [[int(i) for i in top] for top in temp]
                else:
                    return_data = [i.split(sign) for i in data]
            else:
                frozen_split = partial(
                    self.recursive_split, sign=sign, make_int=make_int)
                return_data = [list(map(frozen_split, i, )) for i in data]
        return return_data

    def special_split(self, sign=None, make_int=False) -> None:
        """
        Set data element to result of the recursive split.
        """
        self.data = self.recursive_split(
            self.data, sign=sign, make_int=make_int)
