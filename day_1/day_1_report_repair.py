def two_sum(sum, choices):
    differences = set()
    for first_number in choices:
        second_number = sum - first_number
        if first_number in differences:
            return first_number, second_number
        differences.add(second_number)
    return False

def three_sum(sum, choices):
    choices.sort()
    choices_size = len(choices)
    for i in range(0, choices_size - 2):
        left_index = i + 1
        right_index = choices_size - 1
        while(left_index < right_index):
            first_number = choices[i]
            second_number = choices[left_index]
            third_number = choices[right_index]
            if(first_number + second_number + third_number == sum):
                return first_number, second_number, third_number
            if(sum - first_number < second_number + third_number):
                right_index -= 1
            else:
                left_index += 1  
    return False

with open('expense_report.txt') as file:
    data = file.read()
content = [int(i) for i in data.split()]

first, second = two_sum(2020, content)
print("part 1", first * second)

first, second, third = three_sum(2020, content)
print("part 2", first * second * third)
