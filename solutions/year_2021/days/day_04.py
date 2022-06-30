"""Day 4 module for solving Advent of Code"""
from tools.data_helpers import ReadData
from tools.day_module import RunDay


class Bingo:
    """Class to play Bino against the submarine."""

    def __init__(self, bingo_numbers, bingo_cards) -> None:
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
                for __ in line:
                    game_state_line.append(False)
                game_state_card.append(game_state_line)
            self.game_state.append(game_state_card)

        self.not_won_cards = list(range(len(self.bingo_cards)))

    def _get_bingo_numbers(self) -> list[int]:
        """returns the bingo nummers."""
        return self.bingo_numbers

    def _get_bingo_cards(self) -> list:
        """returns the bingo cards."""
        return self.bingo_cards

    def _get_card(self, i) -> tuple:
        """returns a single bingo card."""
        return (self.bingo_cards[i], self.game_state[i])

    def _mark_number(self, num) -> None:
        """Marks a bingo number."""
        for idx, card in enumerate(self.bingo_cards):
            for y, line in enumerate(card):
                for x, entry in enumerate(line):
                    if entry == num:
                        self.game_state[idx][y][x] = True

    def _check_win(self) -> bool:
        """
        Check if cards are won, if this is
        the case it will return the won cards
        """
        won_cards = []
        for i in self.not_won_cards:
            card = self.game_state[i]
            for line in card:
                if sum(line) == 5:
                    if i not in won_cards:
                        won_cards.append(i)
                for x, __ in enumerate(line):
                    column = card[0][x] + card[1][x] + \
                        card[2][x] + card[3][x] + card[4][x]
                    if column == 5:
                        if i not in won_cards:
                            won_cards.append(i)
        if len(won_cards) > 0:
            return won_cards
        return False

    def _get_card_score(self, card: list) -> int:
        """Returns the score of a card."""
        total_score = 0
        for y, line in enumerate(self.game_state[card[0]]):
            for x, entry in enumerate(line):
                if not entry:
                    total_score += self.bingo_cards[card[0]][y][x]
        return total_score

    def _get_win_score(self, current_num: int, winning_card: int) -> int:
        """Returns win score."""
        return current_num * self._get_card_score(winning_card)

    def find_winning_board(self):
        """
        Returns the winning board number,
        the card and the score.
        """
        winning_card = False
        for num in self.bingo_numbers:
            self._mark_number(num)
            winning_card = self._check_win()
            if winning_card:
                score = self._get_win_score(num, winning_card)
                return num, winning_card, score

    def last_winning_board(self):
        """Returns the last won board."""
        for num in self.bingo_numbers:
            self._mark_number(num)
            winning_card = False
            winning_card = self._check_win()
            if len(self.not_won_cards) == 1:
                if isinstance(winning_card, list):
                    score = self._get_win_score(num, winning_card)
                    return num, winning_card, score
            if isinstance(winning_card, list):
                for card in winning_card:
                    try:
                        self.not_won_cards.remove(card)
                    except IndexError:
                        pass


class Day(RunDay):
    """Class to run the day"""

    def __init__(self) -> None:
        super().__init__()
        self.day = 4
        self.test_part_1 = 4512
        self.test_part_2 = 1924

    def parse_input(self, day, test=True):
        """Prep the data for processing."""
        bingo_input = ReadData(day, test, lines=False, read_int=False)
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
        return bingo_numbers, bingo_cards

    def part_1(self, data):
        """Runs the code for part 1"""
        bingo_numbers, bingo_cards = data
        bingo = Bingo(bingo_numbers, bingo_cards)
        return bingo.find_winning_board()[2]

    def part_2(self, data):
        """Runs the code for part 2"""
        bingo_numbers, bingo_cards = data
        bingo = Bingo(bingo_numbers, bingo_cards)
        return bingo.last_winning_board()[2]


def main():
    """Run the code for the day"""
    today = Day()
    today.run()


if __name__ == '__main__':
    main()
