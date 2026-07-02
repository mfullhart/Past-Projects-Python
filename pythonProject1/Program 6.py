# Program to make change based on a given amount

# Main function
def main():

    # Variables
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    one = 1.00
    five = 5.00
    ten = 10.00
    twenty = 20.00
    fifty = 50.00
    one_hundred = 100.00

    # User defined variables
    sales_price = float(input("Enter the sales price: $"))
    amount_tendered = float(input("Enter the amount tendered: $"))

    # Calculate total change due & print
    total_change_due = amount_tendered - sales_price
    print("Your change is: $", total_change_due)
    print("You will receive:")

    # Calculate exact change due
    if total_change_due <= 0:
        print("No change due")

    # Calculate one hundred dollar bills
    if total_change_due // one_hundred:
        one_hundred_due = total_change_due // one_hundred
        print("One Hundred Dollar Bills: ", one_hundred_due)
        total_change_due -= one_hundred_due * one_hundred

    # Calculate fifty dollar bills
    if total_change_due // fifty:
        fifty_due = total_change_due // fifty
        print("Fifty Dollar Bills: ", fifty_due)
        total_change_due -= fifty_due * fifty

    # Calculate twenty dollar bills
    if total_change_due // twenty:
        twenty_due = total_change_due // twenty
        print("Twenty Dollar Bills: ", twenty_due)
        total_change_due -= twenty_due * twenty

    # Calculate ten dollar bills
    if total_change_due // ten:
        ten_due = total_change_due // ten
        print("Ten Dollar Bills: ", ten_due)
        total_change_due -= ten_due * ten

    # Calculate five dollar bills
    if total_change_due // five:
        five_due = total_change_due // five
        print("Five Dollar Bills: ", five_due)
        total_change_due -= five_due * five

    # Calculate one dollar bills
    if total_change_due // one:
        one_due = total_change_due // one
        print("One Dollar Bills: ", one_due)
        total_change_due -= one_due * one

    # Calculate quarters
    if total_change_due // quarter:
        quarter_due = total_change_due // quarter
        print("Quarters: ", quarter_due)
        total_change_due -= quarter_due * quarter

    # Calculate dimes
    if total_change_due // dime:
        dime_due = total_change_due // dime
        print("Dime: ", dime_due)
        total_change_due -= dime_due * dime

    # Calculate nickels
    if total_change_due // nickel:
        nickel_due = total_change_due // nickel
        print("Nickels: ", nickel_due)
        total_change_due -= nickel_due * nickel

    # Calculate pennies
    if total_change_due // penny:
        penny_due = total_change_due // penny
        print("Pennies: ", penny_due)
        total_change_due -= penny_due * penny


main()
