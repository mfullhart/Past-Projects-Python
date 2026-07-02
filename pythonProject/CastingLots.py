# Program to play casting of lots

# Imports random number generator
import random


def load_talents():
    """ Function to load talents from file"""
    try:
        with open("talents.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 100  # Starting amount if file doesn't exist


def save_talents(talents):
    """ Function to save talents to file"""
    with open("talents.txt", "w") as file:
        file.write(str(talents))


def field_bet(talents, bet_amount):
    """ Field bet logic"""
    # Generate random number
    result = random.randint(0, 12)
    print("The LOTS CAST is: ", result)

    # Results if won
    if result in (2, 12):
        print("You have won double your bet.")
        total_talents = talents + bet_amount * 2
        print("You now have ", total_talents)
        return total_talents

    # Results if won
    elif result in (3, 4, 9, 10, 11):
        print("You have won your bet.")
        total_talents = talents + bet_amount
        print("You now have ", total_talents)
        return total_talents

    # Results if lost
    else:
        print("You have lost your bet.")
        total_talents = talents - bet_amount
        print("You now have ", total_talents)
        return total_talents


def pass_bet(talents, bet_amount):
    """Pass bet logic"""
    # Generate random number
    result = random.randint(0, 12)
    print("The LOTS CAST is: ", result)

    # Results if won
    if result in (7, 11):
        print("You have won your bet.")
        total_talents = talents + bet_amount
        print("You now have ", total_talents)
        return total_talents

    # Results if lost
    elif result in (2, 12):
        print("You have lost your bet.")
        total_talents = talents - bet_amount
        print("You now have ", total_talents)
        return total_talents

    else:
        point = result
        while True:
            new_result = random.randint(0, 12)

            # Results if lost
            if new_result == 7:
                print("You have lost your bet.")
                total_talents = talents - bet_amount
                print("You now have ", total_talents)
                return total_talents

            # Results if won
            elif new_result == point:
                print("You have won your bet.")
                total_talents = talents + bet_amount
                print("You now have ", total_talents)
                return total_talents


def play_game():
    """Main game loop"""
    talents = load_talents()
    print(f"Welcome! You have {talents} talents.")

    # Main menu prompt
    while True:
        print("\nMenu:")
        print("1 - Field Bet")
        print("2 - Pass Bet")
        print("3 - Quit")

        choice = input("Enter your choice: ")

        # Choice is Field Bet
        if choice == '1':
            bet_amount = int(input("Enter the amount of talents you wish to wager: "))
            if bet_amount > talents:
                print("You don't have enough talents.")
                continue
            talents = field_bet(talents, bet_amount)

        # Choice is Pass Bet
        elif choice == '2':
            bet_amount = int(input("Enter the amount of talents you wish to wager: "))
            if bet_amount > talents:
                print("You don't have enough talents.")
                continue
            talents = pass_bet(talents, bet_amount)

        # Choice is Quit
        elif choice == '3':
            save_talents(100)
            print(f"Your talents have been reset to 100. See you next time!")
            break
        else:
            print("Invalid choice. Please choose again.")

        # Ran out of talents
        if talents <= 0:
            print("You have run out of talents. Start with 100 talents next time.")
            save_talents(100)
            break


# Run the game
play_game()
