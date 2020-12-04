# import data

passport_raw_data = open('passports.txt', 'r')
passports_split = passport_raw_data.read().split('\n\n')
passport_raw_data.close()
passports = []


for passport in passports_split:
    passports.append([item.strip() for item in passport.split()])

passports_clean = []

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
        if key in checks:
            valid += 1
    if valid == 7:
        valid_passports += 1

print(valid_passports)