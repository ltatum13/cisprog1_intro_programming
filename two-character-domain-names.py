'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
num_val = 1

while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print(f'{letter1}{letter2}.com')
        letter2 = chr(ord(letter2) + 1)
    while num_val <= 9:
        print(f'{letter1}{num_val}.com')
        num_val = num_val + 1
    letter1 = chr(ord(letter1) + 1)
