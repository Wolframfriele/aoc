import csv


# import the data into an array
with open('day_02/password_list.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    passwords =[]
    for row in rows:
            passwords.append(row)

# function to find the number of valid passwords
def findValidRule1(password_list):
    valid_count = 0
    for row in password_list:
        count = row[3].count(row[2])
        if count >= int(row[0]) and count <= int(row[1]):
            valid_count += 1

    return valid_count

def findValidRule2(password_list):
    valid_counter = 0
    for row in password_list:

        check1 = row[3][int(row[0])-1] == row[2]
        check2 = row[3][int(row[1])-1] == row[2]
        if check1 ^ check2:
            valid_counter += 1

    return valid_counter

print(findValidRule2(passwords))