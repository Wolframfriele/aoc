"""
Set of functions to better import data and chop it to a workable format.
"""

class ReadData(object):
    def __init__(self, path, lines=True, read_int=False):
        with open(path, "r") as f:
            if lines:
                if read_int:
                    self.data = [int(line.rstrip('\n')) for line in f]
                else:
                    self.data = [line.rstrip('\n') for line in f]
            else:
                self.data = f.read()

    def __repr__(self):
        return str(self.data)
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def pop_data(self, index):
        return self.data.pop(index)

    def special_split(self, sign=None, make_int=False):
        def recursive_split(data):
            if type(data) is str:
                if make_int:
                    return [int(i) for i in data.split(sign)]
                return data.split(sign)
            elif type(data) is list:
                if type(data[0]) is str:
                    if make_int:
                        temp = [i.split(sign) for i in data]
                        return [[int(i) for i in top] for top in temp]
                    return [i.split(sign) for i in data]
                elif type(data[0]) is list:
                    return [list(map(recursive_split, i)) for i in data]
        self.data = recursive_split(self.data)