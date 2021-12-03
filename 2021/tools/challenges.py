"""
Tools that are probably unique to each days challenge
"""
from statistics import mode

class ReadDiagnostics(object):
    bit_array = []
    restructured_bit_array = []
    gamma_rate_bitstring = ""
    epsilon_rate_bitstring = ""

    def __init__(self, bit_array):
        self.bit_array = bit_array

    def __repr__(self):
        return str(self.bit_array)

    def build_restructure_array(self):
        for i in self.bit_array[0]:
            self.restructured_bit_array.append([])
        return len(self.restructured_bit_array)

    def restructure_bits(self):
        for bit in self.bit_array:
            for i, value in enumerate(bit):
                self.restructured_bit_array[i].append(int(value))
    
    def get_most_common(self):
        most_common = ""
        for i in self.restructured_bit_array:
            most_common += str(mode(i))
        return most_common

    def bit_inverse(self, bit_string):
        inverse = ""
        for i in bit_string:
            inverse_bool = not int(i)
            if inverse_bool:
                inverse += "1"
            else:
                inverse += "0"
        return inverse

    def get_gamma_rate(self):
        if len(self.restructured_bit_array) == 0:
            self.build_restructure_array()
            self.restructure_bits()
        self.gamma_rate_bitstring = self.get_most_common()
        return int(self.gamma_rate_bitstring, 2)

    def get_epsilon_rate(self):
        epsilon_bitstring = ""
        if len(self.restructured_bit_array) == 0:
            self.build_restructure_array()
            self.restructure_bits()
        if self.gamma_rate_bitstring:
            self.epsilon_rate_bitstring = self.bit_inverse(self.gamma_rate_bitstring)
        else:
            self.gamma_rate_bitstring = self.get_most_common()
            self.epsilon_rate_bitstring = self.bit_inverse(self.gamma_rate_bitstring)
        return int(self.epsilon_rate_bitstring, 2)

    def get_power_consumption(self):
        gamma_rate = self.get_gamma_rate()
        epsilon_rate = self.get_epsilon_rate()
        return  gamma_rate * epsilon_rate