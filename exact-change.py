change_amount = int(input())

if change_amount == 0:
    print('No change')
else:
    ## dollars
    dollars = change_amount // 100
    if dollars == 1:
        print(str(dollars) + ' Dollar')
        change_amount = change_amount - (dollars * 100)
    elif dollars > 1:
        print(str(dollars) + ' Dollars')
        change_amount = change_amount - (dollars * 100)
    
    ## quarters
    quarters = change_amount // 25
    if quarters == 1:
        print(str(quarters) + ' Quarter')
        change_amount = change_amount - (quarters * 25)
    elif quarters > 1:
        print(str(quarters) + ' Quarters')
        change_amount = change_amount - (quarters * 25)
    
    ## dimes
    dimes = change_amount // 10
    if dimes == 1:
        print(str(dimes) + ' Dime')
        change_amount = change_amount - (dimes * 10)
    elif dimes > 1:
        print(str(dimes) + ' Dimes')
        change_amount = change_amount - (dimes * 10)
    
    ## nickels
    nickels =  change_amount // 5
    if nickels == 1:
        print(str(nickels) + ' Nickel')
        change_amount = change_amount - (nickels * 5)
    elif nickels > 1:
        print(str(nickels) + ' Nickels')
        change_amount = change_amount - (nickels * 5)
    
    ## pennies
    pennies = change_amount // 1
    if pennies == 1:
        print(str(pennies) + ' Penny')
        change_amount = change_amount - (pennies * 1)
    elif pennies > 1:
        print(str(pennies) + ' Pennies')
        change_amount = change_amount - (pennies * 1)