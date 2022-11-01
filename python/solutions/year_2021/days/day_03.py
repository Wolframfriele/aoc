"""Day 3 module for solving Advent of Code"""
from statistics import multimode
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class ReadDiagnostics:
    """Class that helps with reading the diagnostics off the submarine."""

    def __init__(self, bit_array) -> None:
        self.bit_array = bit_array
        self.gamma_rate_bitstring = ""
        self.epsilon_rate_bitstring = ""

    def __repr__(self):
        return str(self.bit_array)

    def _get_most_common(self, bit_array: list[str], position: int) -> int:
        """Returns the most common bit for all lines in the array."""
        bits_in_position = []
        for bit in bit_array:
            bits_in_position.append(int(bit[position]))
        most_common = max(multimode(bits_in_position))
        return most_common

    def _bit_inverse(self, bit_string: str) -> str:
        """Inverses a bitstring"""
        inverse = ""
        if len(str(bit_string)) == 1:
            inverse_bool = not int(bit_string)
            if inverse_bool:
                inverse += "1"
            else:
                inverse += "0"
        else:
            for bit in bit_string:
                inverse_bool = not int(bit)
                if inverse_bool:
                    inverse += "1"
                else:
                    inverse += "0"
        return inverse

    def _filter_bits(self, bit_array: list[str], position: int, value) -> list[str]:
        """
        Return a bit_array with bitstrings that have the
        given value at the given position
        """
        new_bit_array = []
        for bit in bit_array:
            if bit[position] == str(value):
                new_bit_array.append(bit)
        return new_bit_array

    def _get_gamma_rate(self) -> int:
        """Calculate gama rate."""
        if len(self.gamma_rate_bitstring) == 0:
            bit_length = len(self.bit_array[0])
            for i in range(bit_length):
                self.gamma_rate_bitstring += str(
                    self._get_most_common(self.bit_array, i))
        return int(self.gamma_rate_bitstring, 2)

    def _get_epsilon_rate(self) -> int:
        """Calculate epsilon rate."""
        if len(self.gamma_rate_bitstring) == 0:
            self._get_gamma_rate()
        self.epsilon_rate_bitstring = self._bit_inverse(
            self.gamma_rate_bitstring)
        return int(self.epsilon_rate_bitstring, 2)

    def get_power_consumption(self) -> int:
        """calculate power consumption."""
        gamma_rate = self._get_gamma_rate()
        epsilon_rate = self._get_epsilon_rate()
        return gamma_rate * epsilon_rate

    def _get_oxygen_generator_rating(self) -> int:
        """Calculate oxygen generator rating."""
        filtered_bit_array = self.bit_array
        for i, __ in enumerate(self.bit_array[0]):
            most_common = self._get_most_common(filtered_bit_array, i)
            temp_filtered = self._filter_bits(
                filtered_bit_array, i, most_common)
            if len(temp_filtered) == 1:
                return int(temp_filtered[0], 2)
            else:
                filtered_bit_array = temp_filtered

    def _get_co2_scrubber_rating(self) -> int:
        """Calculate co2 scrubber rating."""
        filtered_bit_array = self.bit_array
        for i, __ in enumerate(self.bit_array[0]):
            most_common = self._get_most_common(filtered_bit_array, i)
            least_common = self._bit_inverse(most_common)
            temp_filtered = self._filter_bits(
                filtered_bit_array, i, least_common)
            if len(temp_filtered) == 1:
                return int(temp_filtered[0], 2)
            else:
                filtered_bit_array = temp_filtered

    def get_life_support_rating(self) -> int:
        """Calculate life support rating."""
        oxy_rate = self._get_oxygen_generator_rating()
        co2_rate = self._get_co2_scrubber_rating()
        return oxy_rate * co2_rate


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 3
        self.test_part_1 = 198
        self.test_part_2 = 230

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        diag_report = ReadData(day, test, lines=True, read_int=False)
        return diag_report

    def part_1(self, data):
        """Runs the code for part 1"""
        diagnostics = ReadDiagnostics(data)
        return diagnostics.get_power_consumption()

    def part_2(self, data):
        """Runs the code for part 2"""
        diagnostics = ReadDiagnostics(data)
        return diagnostics.get_life_support_rating()


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
