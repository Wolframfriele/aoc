# input tree_map.txt into list

tree_map_read = open('tree_map.txt', 'r')
tree_map = tree_map_read.read().splitlines()
tree_map_read.close()


def sledding(curve_variable, step, map):
    location = 0
    crash_counter = 0
    for i, row in enumerate(map):
        if i % step == 0:
            if row[(location%len(tree_map[0]))] == '#':
                crash_counter += 1
            # temp_row = row[:(location % len(tree_map[0]))] + 'X' + row[(location % len(tree_map[0]))+1:]
            # print(temp_row)
            location += curve_variable
        # else:
        #     print(row)

    return crash_counter


var1 = sledding(1, 1, tree_map)
var2 = sledding(3, 1, tree_map)
var3 = sledding(5, 1, tree_map)
var4 = sledding(7, 1, tree_map)
var5 = sledding(1, 2, tree_map)

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

print(var1*var2*var3*var4*var5)

# sledding(1, 2, tree_map)
