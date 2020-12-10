def count_trees(locations, right_increment, down_increment):
    tree_count = 0
    cur_right = right_increment
    cur_down = down_increment
    while cur_down in locations:
        if len(locations[cur_down]) < cur_right + 1:
            cur_right = cur_right % len(locations[cur_down])
        if locations[cur_down][cur_right] == '#':
            tree_count += 1
        cur_right += right_increment
        cur_down += down_increment
    return tree_count

with open('map_input.txt') as file:
    data = file.read()
content = [list(i) for i in data.split()]
locations = { i : content[i] for i in range(0, len(content)) }

print("part 1", count_trees(locations, 3, 1))
print("part 2", count_trees(locations, 1, 1) * count_trees(locations, 3, 1) * count_trees(locations, 5, 1) * count_trees(locations, 7, 1) * count_trees(locations, 1, 2))
