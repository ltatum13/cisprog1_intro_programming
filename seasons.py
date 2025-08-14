input_month = input()
input_day = int(input())

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February', 'March']

## invalid
if input_month not in spring:
    if input_month not in summer:
        if input_month not in autumn:
            if input_month not in winter:
                print('Invalid')

if input_day <= 0 or input_month == 'February' and input_day >= 30:
    print('Invalid')

## spring
if input_month in spring:
    if input_month == 'March' and 20 <= input_day <= 31:
        print('Spring')
    if input_month == 'June' and 1 <= input_day <= 20:
        print('Spring')
    if input_month != 'March' and input_month != 'June':
        print('Spring')

## summer
if input_month in summer:
    if input_month == 'June' and 21 <= input_day <= 30:
        print('Summer')
    elif input_month == 'September' and 1 <= input_day <= 21:
        print('Summer')
    elif input_month != 'September' and input_month != 'June':
        print('Summer')

## autumn
if input_month in autumn:
    if input_month == 'September' and input_day >= 22:
        if input_month == 'September' and input_day > 30:
            print('Invalid')
        else:
            print('Autumn')
    elif input_month == 'December' and 1 <= input_day <= 20:
        print('Autumn')
    elif input_month != 'September' and input_month != 'December':
        print('Autumn')

## winter
if input_month in winter:
    if input_month == 'December' and input_day >= 21:
        print('Winter')
    elif input_month == 'March' and 1 <= input_day <= 19:
        print('Winter')
    elif input_month == 'February' and 1 <= input_day <= 29:
        print('Winter')
    elif input_month == 'January' and 1 <= input_day <= 31:
        print('Winter')