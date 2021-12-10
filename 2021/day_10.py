import re
from tools.data import ReadData

### Parse input ###
data = ReadData("2021/data/10_t.txt", lines=True, read_int=False)
# data = [list(map(int, i)) for i in data]
print(data)

class SyntaxChecker(object):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 5137}
    regex = r"(\(\)|{}|\[\]|<>|\[\])"
    def __init__(self, navigation_data) -> None:
        self.navigation_data = navigation_data
        super().__init__()

    def check_line(self, line):
        string = self.navigation_data[line]
        subst = ""
        # You can manually specify the number of replacements by changing the 4th argument
        result = re.sub(self.regex, subst, string, 0)
        return result

checker = SyntaxChecker(data)
print(checker.check_line(1))