import re
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/10_t.txt", lines=True, read_int=False)
print(len(data))

class bcolors:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class SyntaxChecker(object):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    def __init__(self, navigation_data) -> None:
        self.navigation_data = navigation_data
        super().__init__()

    def check_legal_line(self, line):
        string = self.navigation_data[line]
        matched = [0 for i in range(len(string))]
        end_sign = ['>', ')', ']', '}']
        for i, char in enumerate(string):
            look_up = {
                        '>': ('<', ['(', '[', '{']),
                        ')': ('(', ['<', '[', '{']),
                        ']': ('[', ['(', '<', '{']),
                        '}': ('{', ['(', '[', '<'])
                      }
            if char in end_sign and matched[i] == 0:
                matched[i] = 1
                check_for, wrong = look_up[char]
                for x in range(i, -1, -1):
                    if string[x] == check_for and matched[x] == 0:
                        # self.print_matched(string, matched)
                        matched[x] = 1
                        break
                    elif string[x] in wrong and matched[x] == 0:
                        matched[i] = 2
                        matched[x] = 2
                        self.print_matched(string, matched)
                        return False, char
                else:
                    # self.print_matched(string, matched)
                    return False, char
        # self.print_matched(string, matched)
        return True, None

    def print_matched(self, string, matched):
        for i, char in enumerate(string):
            if matched[i] == 2:
                print(bcolors.FAIL + char + bcolors.RESET, end = " ")
            elif matched[i] == 1:
                print(bcolors.OK + char + bcolors.RESET, end = " ")
            else:
                print(bcolors.RESET + char + bcolors.RESET, end = " ")
        print("")

    def discard_corrupt_lines(self):
        score = 0
        discard = []
        for line in range(len(self.navigation_data)):
            legal, char = self.check_legal_line(line)
            if not legal:
                discard.append(line)
                score += self.score_table[char]
        for i in discard[::-1]:
            self.navigation_data.pop_data(i)
        return score

checker = SyntaxChecker(data)
print(checker.discard_corrupt_lines())
