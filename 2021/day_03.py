from statistics import multimode
from tools.data import ReadData

### Parse input ###
diag_report = ReadData("2021/data/3.txt", lines=True, read_int=False)

class ReadDiagnostics(object):
    bit_array = []
    gamma_rate_bitstring = ""
    epsilon_rate_bitstring = ""

    def __init__(self, bit_array):
        self.bit_array = bit_array

    def __repr__(self):
        return str(self.bit_array)
    
    def get_most_common(self, bit_array, position):
        bits_in_position = []
        for bit in bit_array:
            bits_in_position.append(int(bit[position]))
        most_common = max(multimode(bits_in_position))
        return most_common

    def bit_inverse(self, bit_string):
        inverse = ""
        if len(str(bit_string)) == 1:
            inverse_bool = not int(bit_string)
            if inverse_bool:
                inverse += "1"
            else:
                inverse += "0"
        else:
            for i in bit_string:
                inverse_bool = not int(i)
                if inverse_bool:
                    inverse += "1"
                else:
                    inverse += "0"
        return inverse

    def filter_bits(self, bit_array, position, value):
        new_bit_array = []
        for bit in bit_array:
            if bit[position] == str(value):
                new_bit_array.append(bit)
        return new_bit_array

    def get_gamma_rate(self):
        if len(self.gamma_rate_bitstring) == 0:
            bit_length = len(self.bit_array[0])
            for i in range(bit_length):
                self.gamma_rate_bitstring += str(self.get_most_common(self.bit_array, i))
        return int(self.gamma_rate_bitstring, 2)

    def get_epsilon_rate(self):
        epsilon_bitstring = ""
        if len(self.gamma_rate_bitstring) == 0:
            self.get_gamma_rate()
        self.epsilon_rate_bitstring = self.bit_inverse(self.gamma_rate_bitstring)
        return int(self.epsilon_rate_bitstring, 2)

    def get_power_consumption(self):
        gamma_rate = self.get_gamma_rate()
        epsilon_rate = self.get_epsilon_rate()
        return  gamma_rate * epsilon_rate

    def get_oxygen_generator_rating(self):
        filtered_bit_array = self.bit_array
        for i in range(len(self.bit_array[0])):
            most_common = self.get_most_common(filtered_bit_array, i)
            temp_filtered = self.filter_bits(filtered_bit_array, i, most_common)
            if len(temp_filtered) == 1:
                return int(temp_filtered[0], 2)
            else:
                filtered_bit_array = temp_filtered

    def get_co2_scrubber_rating(self):
        filtered_bit_array = self.bit_array
        for i in range(len(self.bit_array[0])):
            most_common = self.get_most_common(filtered_bit_array, i)
            least_common = self.bit_inverse(most_common)
            temp_filtered = self.filter_bits(filtered_bit_array, i, least_common)
            if len(temp_filtered) == 1:
                return int(temp_filtered[0], 2)
            else:
                filtered_bit_array = temp_filtered

    def get_life_support_rating(self):
        oxy_rate = self.get_oxygen_generator_rating()
        co2_rate = self.get_co2_scrubber_rating()
        return oxy_rate * co2_rate

# Part 1
diagnostics = ReadDiagnostics(diag_report)
print(diagnostics.get_power_consumption())

# Part 2
print(diagnostics.get_life_support_rating())