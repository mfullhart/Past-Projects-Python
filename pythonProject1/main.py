
def main():
    sales_price = float(input("Enter the sales price:"))
    amount_tendered = float(input("Enter the amount tendered:"))

    # Calculate total change due
    total_change = amount_tendered - sales_price
    print(total_change)

    if total_change <= 0:
        print('No change')
    else:
        dollar = total_change // 100
        if dollar == 1:
            print(dollar, 'Dollar')
            total_change = total_change - (dollar * 100)
        elif dollar <= 0:
            print(end='')
        else:
            print(dollar, 'Dollars')
            total_change = total_change - (dollar * 100)
        quarter = total_change // 25
        if quarter == 1:
            print(quarter, 'Quarter')
            total_change = total_change - (quarter * 25)
        elif quarter <= 0:
            print(end='')
        else:
            print(quarter, 'Quarters')
            total_change = total_change - (quarter * 25)
        dime = total_change // 10
        if dime == 1:
            print(dime, 'Dime')
            total_change = total_change - (dime * 10)
        elif dime <= 0:
            print(end='')
        else:
            print(dime, 'Dimes')
            total_change = total_change - (dime * 10)
        nickel = total_change // 5
        if nickel == 1:
            print(nickel, 'Nickel')
            total_change = total_change - (nickel * 5)
        elif nickel <= 0:
            print(end='')
        else:
            print(nickel, 'Nickels')
            total_change = total_change - (nickel * 5)
        penny = total_change // 1
        if penny == 1:
            print(penny, 'Penny')
            total_change = total_change - (penny * 1)
        elif penny <= 0:
            print(end='')
        else:
            print(penny, 'Pennies')
            total_change = total_change - (penny * 1)


main()
