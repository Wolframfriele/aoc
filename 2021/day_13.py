from tools.data import ReadData

### Parse input ###
dots = ReadData("2021/data/13.txt", lines=True, read_int=False)
dots.special_split(',', make_int=True)
folds = ReadData("2021/data/13_f.txt", lines=True, read_int=False)

class FoldingPaper(object):
    def __init__(self, dots) -> None:
        self.dots =  {(i[0], i[1]) for i in dots}
        super().__init__()

    def fold(self, fold_pos, fold_axis):
        after_fold = set()
        for coordinate in self.dots:
            x, y = coordinate
            if fold_axis == 'y':
                if y > fold_pos:
                    dist = y - fold_pos
                    new_y = fold_pos - dist
                    after_fold.add((x, new_y))
                else:
                    after_fold.add((x, y))
            else:
                if x > fold_pos:
                    dist = x - fold_pos
                    new_x = fold_pos - dist
                    after_fold.add((new_x, y))
                else:
                    after_fold.add((x, y))
        self.dots = after_fold
        return len(self.dots)

    def fold_instructions(self, instructions):
        for i in instructions:
            __, __, instruction = i.split()
            fold_axis, fold_pos = instruction.split('=')
            self.fold(int(fold_pos), fold_axis)

    def print_paper(self):
        # Find paper size
        max_x, max_y = 0, 0
        for i in self.dots:
            if i[0] > max_x:
                max_x = i[0]
            if i[1] > max_y:
                max_y = i[1]
        # create dots for all coordinates
        line = ['.' for i in range(max_x + 1)]
        paper = [line.copy() for i in range(max_y + 1)]

        for point in self.dots:
            x, y = point
            paper[y][x] = '#'

        for x in paper:
            for i in x:
                print(i, end=' ')
            print(end='\n')

# Part 1
paper = FoldingPaper(dots)
# print(paper.fold(655, fold_axis='x'))
# Part 2
paper.fold_instructions(folds)
paper.print_paper()
