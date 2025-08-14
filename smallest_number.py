integer1 = int(input())
integer2 = int(input())
integer3 = int(input())

if integer1 <= integer2:
    lowest_num = integer1
elif integer2 <= integer1:
    lowest_num = integer2

if lowest_num <= integer3:
    lowest_num = lowest_num
elif lowest_num >= integer3:
    lowest_num = integer3

print(lowest_num)