def is_valid_password_by_count(required_char, min_count, max_count, password):
    current_count = 0
    for char in password:
        if char == required_char:
            current_count += 1
        if current_count > max_count:
            return False
    return current_count >= min_count

def is_valid_password_by_position(required_char, first_position, second_position, password):
    count = 0
    password_len = len(password)
    if not first_position <= password_len and second_position <= password_len:
        return False
    if password[first_position - 1] == required_char:
        count += 1
    if password[second_position - 1] == required_char:
        count += 1
    return count == 1

with open('passwords.txt') as file:
    data = file.read()
content = [i for i in data.split('\n')]

valid_password_count_by_count = 0
valid_password_count_by_position = 0

for record in content:
    password_rule = [i for i in record.split(' ')]
    required_char = password_rule[1][:-1]
    min_count_or_position = int(password_rule[0].partition("-")[0])
    max_count_or_position = int(password_rule[0].partition("-")[2])
    password = password_rule[2]
    if(is_valid_password_by_count(required_char, min_count_or_position, max_count_or_position, password)):
        valid_password_count_by_count += 1
    if(is_valid_password_by_position(required_char, min_count_or_position, max_count_or_position, password)):
        valid_password_count_by_position += 1

print("part one", valid_password_count_by_count)
print("part two", valid_password_count_by_position)