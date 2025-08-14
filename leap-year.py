input_year = int(input())

if (input_year % 4 == 0) and (input_year % 100 != 0) and (input_year % 400 == 0):
    print(str(input_year) + ' - not a leap year')
elif (input_year % 8 == 0):
    print(str(input_year) + ' - leap year')
else:
    print(str(input_year) + ' - not a leap year')