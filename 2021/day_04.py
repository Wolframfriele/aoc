from tools.data import ReadData

### Parse input ###
bingo_input = ReadData("2021/data/4_t.txt", lines=False, read_int=False)
bingo_input.special_split('\n\n')
bingo_input.special_split('\n')

bingo_numbers = bingo_input[0][0]
bingo_numbers = [int(i) for i in bingo_numbers.split(',')]

bingo_cards = []
for card in bingo_input[1:]:
    single_card = []
    for line in card:
        split_line = [int(i) for i in line.split()]
        single_card.append(split_line)
    bingo_cards.append(single_card)

class Bingo(object):
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

# Part 1
bingo = Bingo(bingo_numbers, bingo_cards)
# bingo.find_winning_board()

# Part 2
print(bingo.last_winning_board())
