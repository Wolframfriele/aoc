"""
Tools that are probably unique to each days challenge
"""
from statistics import multimode
from itertools import count, zip_longest
from typing import Counter

class DepthControl(object):
    def __init__(self):
        super().__init__()

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

class Bingo(object):
    bingo_numbers = []
    bingo_cards = []
    game_state = []
    not_won_cards = []
    won_cards = []

    def __init__(self, bingo_numbers, bingo_cards):
        self.bingo_numbers = []
        self.bingo_cards = []
        self.game_state = []
        self.not_won_cards = []
        self.bingo_numbers = bingo_numbers
        self.bingo_cards = bingo_cards
        
        for card in bingo_cards:
            game_state_card = []
            for line in card:
                game_state_line = []
                for entry in line:
                    game_state_line.append(False)
                game_state_card.append(game_state_line)   
            self.game_state.append(game_state_card)
        
        self.not_won_cards = list(range(len(self.bingo_cards)))

    def get_bingo_numbers(self):
        return self.bingo_numbers

    def get_bingo_cards(self):
        return self.bingo_cards

    def get_card(self, i):
        return (self.bingo_cards[i], self.game_state[i])

    def mark_number(self, num):
        for i, card in enumerate(self.bingo_cards):
            for y, line in enumerate(card):
                for x, entry in enumerate(line):
                    if entry == num:
                        self.game_state[i][y][x] = True

    def check_win(self):
        won_cards = []
        for i in self.not_won_cards:
            # print("checking card: ", i)
            card = self.game_state[i]
            for line in card:
                if sum(line) == 5:
                    if i not in won_cards:
                        won_cards.append(i)
                for x, entry in enumerate(line):
                    column = card[0][x] + card[1][x] + card[2][x] + card[3][x] + card[4][x]
                    if column == 5:
                        if i not in won_cards:
                            won_cards.append(i)
        if len(won_cards) > 0:
            return won_cards
        return False

    def get_card_score(self, card):
        total_score = 0
        for y, line in enumerate(self.game_state[card]):
            for x, entry in enumerate(line):
                if entry == False:
                    total_score += self.bingo_cards[card][y][x]
        return total_score

    def get_win_score(self, current_num, winning_card):
        return current_num * self.get_card_score(winning_card)

    def find_winning_board(self):
        winning_card = False
        for num in self.bingo_numbers:
            self.mark_number(num)
            winning_card = self.check_win()
            if winning_card:
                score = self.get_win_score(num, winning_card)
                return num, winning_card, score

    def last_winning_board(self):
        for num in self.bingo_numbers:
            # print(num)
            self.mark_number(num)
            winning_card = False
            winning_card = self.check_win()
            # print("Winning card:", winning_card, "in: ", self.not_won_cards)
            if len(self.not_won_cards) == 1:
                if type(winning_card) == list:
                    score = self.get_win_score(num, winning_card[0])
                    return num, winning_card, score
            if type(winning_card) == list:
                for i in winning_card:
                    try:
                        self.not_won_cards.remove(i)
                    except:
                        pass

class Lines(object):
    # input_data = []
    # line_map = []

    def __init__(self, input_data):
        self.input_data = input_data
        max_x = 0
        max_y = 0
        for lines in input_data:
            for points in lines:
                if points[0] > max_x:
                    max_x = points[0]
                if points[1] > max_y:
                    max_y = points[1]
        self.line_map = []
        for y in range(max_y + 1):
            empty_horizontal = []
            for x in range(max_x + 1):
                empty_horizontal.append(0)
            self.line_map.append(empty_horizontal)
    
    def __repr__(self):
        output = ""
        for text_line in self.line_map:
            str_line = " ".join("{0}".format(n) for n in text_line)
            str_line += "\n"
            output += str_line
        return output

    def draw_line(self, start_coor, end_coor):
        x_coor = [start_coor[0], end_coor[0]]
        y_coor = [start_coor[1], end_coor[1]]
        for y, x in zip_longest(range(min(y_coor), (max(y_coor) + 1)), range(min(x_coor), (max(x_coor) + 1))):
            if y == None:
                y = min(y_coor)
            if x == None:
                x = min(x_coor)

            self.line_map[y][x] += 1
        
    def check_horizontal_or_vertical(self, start_coor, end_coor):
        return start_coor[0] == end_coor[0] or start_coor[1] == end_coor[1]

    def find_overlap(self):
        counter = 0
        for y in self.line_map:
            for x in y:
                if x >= 2:
                    counter += 1
        return counter

    def find_danger_zone(self, no_diagonal=True):
        for start_coor, end_coor in self.input_data:
            if no_diagonal:
                if self.check_horizontal_or_vertical(start_coor, end_coor):
                    self.draw_line(start_coor, end_coor)
            else:
                if not self.check_horizontal_or_vertical(start_coor, end_coor):
                    print(start_coor, end_coor)
                self.draw_line(start_coor, end_coor)
        
        return self.find_overlap()
