

passport_raw_data = open('passports.txt', 'r')
passports_split = passport_raw_data.read().split('\n\n')
passport_raw_data.close()
passports = []



for passport in passports_split:
    passports.append([item.strip() for item in passport.split()])

valid_passports = 0

for passport in passports:
    valid = 0
    for field in passport:
        if field[:3] == 'byr':
            valid += 1
        if field[:3] == 'iyr':
            valid += 1
        if field[:3] == 'eyr':
            valid += 1
        if field[:3] == 'hgt':
            valid += 1
        if field[:3] == 'hcl':
            valid += 1
        if field[:3] == 'ecl':
            valid += 1
        if field[:3] == 'pid':
            valid += 1
    if valid == 7:
        valid_passports += 1

print(valid_passports)