class read_and_split(object):
    data_object = ''
    data_temp = []

    def __init__(self, data_path):
        data_read = open(data_path, 'r')
        self.data_object = data_read.read()
        data_read.close()

    def __repr__(self):
        if len(self.data_temp) == 0:
            return self.data_object
        else:
            return str(self.data_temp)

    def __len__(self):
        return len(self.data_object)

    def __getitem__(self, index):
        if len(self.data_temp) == 0:
            return self.data_object[index]
        else:
            return self.data_temp[index]

    def split_double_break(self):
        """If there is no temp data, it returns the data object split by double breaks and stores it in data_temp.
        If the data_temp already contains data (a previous split), this function uses that data and returns a double
        break split for each item in the array."""

        if len(self.data_temp) == 0:
            self.data_temp = self.data_object.split('\n\n')
            return self.data_object.split('\n\n')
        else:
            temp = []
            for item in self.data_temp:
                temp.append(item.split('\n\n'))
            self.data_temp = temp
            return temp

    def split_break(self):
        """If there is no temp data, it returns the data object split by breaks and stores it in data_temp.
        If the data_temp already contains data (a previous split), this function uses that data and returns a
        break split for each item in the array."""

        if len(self.data_temp) == 0:
            self.data_temp = self.data_object.split('\n')
            return self.data_object.split('\n')
        else:
            temp = []
            for item in self.data_temp:
                temp.append(item.split('\n'))
            self.data_temp = temp
            return temp