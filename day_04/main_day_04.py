# import data
passport_raw_data = open('passports.txt', 'r')
passports_split = passport_raw_data.read().split('\n\n')
passport_raw_data.close()
passports = []

# split into field per password
for passport in passports_split:
    passports.append([item.strip() for item in passport.split()])

passports_clean = []

# add fields to dictionary
for passport in passports:
    passports_dict = {}
    for field in passport:
        passports_dict[field[:3]] = field[4:]
    passports_clean.append(passports_dict)

valid_passports = 0

checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in passports_clean:
    valid = 0
    for key in passport:
        if key == 'byr':
            if len(passport[key]) == 4:
                if 2002 >= int(passport[key]) >= 1920:
                    valid += 1
        if key == 'iyr':
            if len(passport[key]) == 4:
                if 2020 >= int(passport[key]) >= 2010:
                    valid += 1
        if key == 'eyr':
            if len(passport[key]) == 4:
                if 2030 >= int(passport[key]) >= 2020:
                    valid += 1
        if key == 'hgt':
            if passport[key][-2:] == 'cm':
                if 193 >= int(passport[key][:-2]) >= 150:
                    valid += 1
            if passport[key][-2:] == 'in':
                if 76 >= int(passport[key][:-2]) >= 59:
                    valid += 1
        if key == 'hcl':
            if passport[key][:1] == '#':
                if len(passport[key][1:]) == 6:
                    accepted_char = '0123456789abcdef'
                    accepted = True
                    for i in passport[key][1:]:
                        if i not in accepted_char:
                            accepted = False
                    if accepted:
                        valid += 1
        if key == 'ecl':
            accepted_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if passport[key] in accepted_ecl:
                valid += 1
        if key == 'pid':
            if len(passport[key]) == 9:
                valid += 1

    if valid == 7:
        valid_passports += 1

print(valid_passports)