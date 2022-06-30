from tools import read_and_split


# init data object
customs_answers = read_and_split('customs_answers.txt')

customs_answers.split_double_break()
customs_answers.split_break()

# part 1
total_answers = 0
for group in customs_answers:
    unique_answers = []
    for person_answers in group:
        for answer in person_answers:
            if answer not in unique_answers:
                unique_answers.append(answer)
    total_answers += len(unique_answers)
    
print('Part one answer = {}'.format(total_answers))

# part 2
total_answers2 = 0
for group in customs_answers:
    sets = map(set, group)
    total_answers2 += len(set.intersection(*sets))

print('Part two answe = {}'.format(total_answers2))
