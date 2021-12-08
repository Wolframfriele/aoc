from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/8.txt", lines=True, read_int=False)
data.special_split("|")
data.special_split()


### Solutions ###
class DigitTracker(object):
    def __init__(self) -> None:
        self.digit = [{'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
                      {'a', 'b', 'c', 'd', 'e', 'f', 'g'}]
        self.len_5 = []
        self.len_6 = []
        super().__init__()

    def update_tracker(self, input):
        str_set = {i for i in input}
        input_len = len(input)
        if input_len == 2:
            self.digit[3] = self.digit[3].intersection(str_set)
            self.digit[6] = self.digit[6].intersection(str_set)
            # Remove found from other sets
            self.digit[1] = self.digit[1].difference(self.digit[3])
            self.digit[2] = self.digit[2].difference(self.digit[3])
            self.digit[4] = self.digit[4].difference(self.digit[3])
            self.digit[5] = self.digit[5].difference(self.digit[3])
        elif input_len == 3:
            self.digit[0] = str_set.difference(self.digit[3])
            # Remove found from other sets
            self.digit[1] = self.digit[1].difference(self.digit[0])
            self.digit[2] = self.digit[2].difference(self.digit[0])
            self.digit[4] = self.digit[4].difference(self.digit[0])
            self.digit[5] = self.digit[5].difference(self.digit[0])
        elif input_len == 4:
            self.digit[1] = str_set.difference(self.digit[3])
            self.digit[2] = str_set.difference(self.digit[3])
            # Remove found from other sets
            self.digit[4] = self.digit[4].difference(self.digit[1])
            self.digit[5] = self.digit[5].difference(self.digit[1])
        elif input_len == 5:
            if len(self.len_5) < 2:
                self.len_5.append(str_set)
            else:
                self.len_5.append(str_set)
                intersect = self.len_5[0].intersection(self.len_5[1])
                intersect = intersect.intersection(self.len_5[2])
                intersect = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}.difference(intersect)
                self.digit[1] = self.digit[1].intersection(intersect)
                self.digit[4] = self.digit[4].intersection(intersect)
                # Remove found from other sets
                self.digit[2] = self.digit[2].difference(self.digit[1])
                self.digit[5] = self.digit[5].difference(self.digit[1])
                self.digit[5] = self.digit[5].difference(self.digit[4])

        elif input_len == 6:
            if len(self.len_6) < 2:
                self.len_6.append(str_set)
            else:
                self.len_6.append(str_set)
                intersect = self.len_6[0].intersection(self.len_6[1])
                intersect = intersect.intersection(self.len_6[2])
                intersect = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}.difference(intersect)
                self.digit[3] = self.digit[3].intersection(intersect)
                # Remove found from others
                self.digit[6] = self.digit[6].difference(self.digit[3])
                self.build_decoder()
    
    def build_decoder(self):
        self.set_0 = self.digit[0] | self.digit[1] | self.digit[3] | self.digit[4] | self.digit[5] | self.digit[6]
        self.set_2 = self.digit[0] | self.digit[2] | self.digit[3] | self.digit[4] | self.digit[5]
        self.set_3 = self.digit[0] | self.digit[2] | self.digit[3] | self.digit[5] | self.digit[6]
        self.set_5 = self.digit[0] | self.digit[1] | self.digit[2] | self.digit[5] | self.digit[6]
        self.set_6 = self.digit[0] | self.digit[1] | self.digit[2] | self.digit[4] | self.digit[5] | self.digit[6]
        self.set_9 = self.digit[0] | self.digit[1] | self.digit[2] | self.digit[3] | self.digit[5] | self.digit[6]

    def decode_input(self, input):
        length = len(input)
        if length == 2:
            return 1
        elif length == 4:
            return 4
        elif length == 3:
            return 7
        elif length == 7:
            return 8
        else:
            str_set = {i for i in input}
            if str_set == self.set_0:
                return 0
            elif str_set == self.set_2:
                return 2
            elif str_set == self.set_3:
                return 3
            elif str_set == self.set_5:
                return 5
            elif str_set == self.set_6:
                return 6
            elif str_set == self.set_9:
                return 9

    def get_digit(self):
        return self.digit

class DigitizerDecode(object):
    def __init__(self, input_output) -> None:
        self.input_data = []
        self.output_data = []
        for i in input_output:
            self.input_data.append(i[0])
            self.output_data.append(i[1])
        super().__init__()

    def check_easy_number(self, output_String):
        if len(output_String) == 2:
            return True, 1
        elif len(output_String) == 4:
            return True, 4
        elif len(output_String) == 3:
            return True, 7
        elif len(output_String) == 7:
            return True, 8
        return False, None
    
    def count_known_value(self):
        known_counter = 0
        for outputs in self.output_data:
            for output in outputs:
                easy_truth, easy_value = self.check_easy_number(output)
                if easy_truth:
                    known_counter += 1
        return known_counter

    def decode_line(self, index):
        number = ""
        self.input_data[index].sort(key=len)
        decoder = DigitTracker()
        for i in self.input_data[index]:
            decoder.update_tracker(i)
        for i in self.output_data[index]:
            number += str(decoder.decode_input(i))
        return int(number)

    def decode_input(self):
        total = 0
        for i in range(len(self.output_data)):
            total += self.decode_line(i)
        return total

digits = DigitizerDecode(data)
print(digits.decode_input())
