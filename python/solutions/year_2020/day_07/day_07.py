from data import ReadData

### Parse input ###
data = ReadData("2020/day_07/test.txt", lines=True, read_int=False)
for i in data:
    print(i)
data.special_split(" ")
### Solutions ###

rules = {}

for i in data:
    color = " ".join(i[:2])
    contains = " ".join(i[4:]).split(", ")
    if contains == "no other bags":
        rules[color] = 0
    else:
        for part in contains:
            single = part.split(" ")
            rules[color] = 
    # print(color)
    print(contains)