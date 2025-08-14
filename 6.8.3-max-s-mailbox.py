num_rows = int(input())
num_columns = int(input())

letter1 = 'A'

for i in range(1, num_rows + 1):
    for j in range(num_columns):
        print(f'{i}{letter1}', end=' ')
        letter1 = chr(ord(letter1) + 1)
    letter1 = 'A'
    print('')