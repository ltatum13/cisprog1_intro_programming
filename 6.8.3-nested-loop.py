loop_val = int(input())
i = 0

for i in range(1, loop_val + 1):
    print(i, end='')
    for i in range(i):
        print('$', end='')
    print()