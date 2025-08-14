user_input = input()
num_list = list(map(int, user_input.split()))
num_list.sort()
elements_in_list = 0

for i in num_list:
    elements_in_list += 1

if elements_in_list > 9:
    print('Too many inputs')
else:
    median = elements_in_list // 2
    middle_num = num_list[median]

print(f'Middle item: {middle_num}')