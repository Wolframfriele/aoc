from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/10.txt", lines=True, read_int=False)
print(len(data))

class bcolors:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class SyntaxChecker:
    def __init__(self, navigation_data) -> None:
        self.navigation_data = navigation_data
        self.matched_lines = []

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
                        self.matched_lines.append(matched)
                        return False, char
                else:
                    # self.print_matched(string, matched)
                    self.matched_lines.append(matched)
                    return False, char
        # self.print_matched(string, matched)
        self.matched_lines.append(matched)
        return True, None

    def discard_corrupt_lines(self):
        score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
        score = 0
        discard = []
        for line in range(len(self.navigation_data)):
            legal, char = self.check_legal_line(line)
            if not legal:
                discard.append(line)
                score += score_table[char]
        for i in discard[::-1]:
            self.navigation_data.pop_data(i)
            self.matched_lines.pop(i)
        return score

    def complete_lines(self):
        all_scores = []
        score_table = {"(":1, "[": 2, "{": 3, "<": 4}
        look_up = {'<': '>', '(': ')', '[': ']', '{': ']'}
        for i, line in enumerate(self.navigation_data):
            score = 0
            queue = []
            matched = self.matched_lines[i]
            # self.print_matched(line, matched)
            for x, match in enumerate(matched):
                if match == 0:
                    queue.append(line[x])
            queue.reverse()
            for char in queue:
                score = score * 5
                score += score_table[char]
            all_scores.append(score)

        all_scores.sort()
        midle = len(all_scores) // 2
        return all_scores[midle]


    def print_matched(self, string, matched):
        for i, char in enumerate(string):
            if matched[i] == 2:
                print(bcolors.FAIL + char + bcolors.RESET, end = " ")
            elif matched[i] == 1:
                print(bcolors.OK + char + bcolors.RESET, end = " ")
            else:
                print(bcolors.RESET + char + bcolors.RESET, end = " ")
        print("")

# Part 1
checker = SyntaxChecker(data)
print(checker.discard_corrupt_lines())

# Part 2
print(checker.complete_lines())