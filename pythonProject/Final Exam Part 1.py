import random

# TODO guess and main have more than 20 lines


def main():
    """
    function will ask user first how many decks they would like to play with(0,5).
    Then it will generate a card.  The user now has the option to either put a new card down and get a streak(15)
    or guess running and current total to keep score and add it to total.
    If the user guesses running total wrong, it will then tell the user that it was wrong and what the correct answer is
    The streak that the user had is now over.  The game will continue until the deck runs out or until the user exits.
    Once the game ends it saves the score to a .txt file, but only if it's higher than the previous score.
    This .txt file will be named highscore.txt and now represents highs score

    as a note:
    Think about turning these variables into one list for faster reading
    :return:
    """
    # Find hide score and display to user
    high_score = rs()
    # list to store cards that have been drawn
    random_card_list = []
    # list to store the value of the card for running count
    card_value_list = []
    # prompts user for how many decks they would like to play with, also converts cards
    # decks is [0] and cards is [1]
    decks_and_cards = decks_to_play_with()
    # find the amount of cards in amount of decks chosen
    cards = decks_and_cards[1]
    # streak always starts on 0
    streak = 0
    # menu option
    new_card = menu()
    # score in the beginning is always 0
    score = 0
    # game start
    while new_card != 3:
        # start of streak
        streak += 1
        # get random card that hasn't been drawn yet and display it to user, then discard
        random_card = rc(random_card_list, decks_and_cards[0])
        random_card_list.append(random_card)
        cards -= 1
        # was not working in while loop for some reason.  I put it here, still works
        if cards == 0:
            break
        # Check card value (+1, -1, 0) and add to list
        card_value = cv(random_card)
        card_value_list.append(card_value)
        # menu option: new card, guess, or exit
        new_card = menu()
        # if user hits a streak of 15 or wants to guess
        if streak == 15 or new_card == 2:
            score = guess(streak, card_value_list, score, cards)
            # because the user guessed, their streak is reset
            streak = 0
    ss(score, high_score)


def ss(score, high_score):
    """
    This function will read what the last highscore was, check to see if new score is more than highscore.
    if it is more than highscore, it will take score and write it to high_score.txt to save the user's data.
    if for some reason there is an error reading file or values, the function will not save data,
    and it will give the closing statement shutting the program down.
    :param score:
    :param high_score:
    :return:
    """
    # must be converted to string to write to program
    string_score = str(score)
    if score > high_score:
        try:
            # open file to write.
            with open('high_score.txt', 'w') as file:
                # if score is more than highscore, highscore will be replaced with score.
                file.write(string_score)
                print('Data saved')
                print(f'Your new highscore is {score}!')
        # if for some reason it cant find the file or gets value error for some reason.
        except FileNotFoundError and ValueError:
            print('Could not write to file, progress lost')
    # closing message
    print('Thankyou for playing the game!')


def rs():
    """
    This function is going to read a score from high_score.txt.  In the future it will change to .csv.
    upon reading score it will return that value.  If for some reason the file does not exist or there is a
    value error, the function will return 0.
    :return:
    """
    try:
        with open('high_score.txt', 'r') as file:
            high_score = int(file.readline())
    except FileNotFoundError and ValueError:
        high_score = 0
    print(f'Your highest score is: {high_score}')
    return high_score


def generate_threshold():
    """
    This function serves as a way to generate a threshold for int so that you can stop user error.
    For example, if I ask a user for an int input for the total or running count, and they guess a string or
    and outlandish number, they will then be prompted again.
    :return:
    """
    # im too lzy to do this by hand
    thresh_hold = []
    for i in range(-30, 30):
        thresh_hold.append(i)
    return thresh_hold


def menu():
    """
    This function validates the user input so that it doesn't break program.  It will then return the value of the card
    :return:
    """
    # options
    new_card_list = [1, 2, 3]
    new_card = int(input('New card(1) guess(2) exit(3)\nSelect (1,2,3): '))
    # validate input through list of options
    while new_card not in new_card_list:
        new_card = int(input('New card(1) guess(2) exit(3)\nSelect (1,2,3): '))
    return new_card


def decks_to_play_with():
    """
    This function serves as a way to make sure the user does not input something super wierd like strings or the wrong
    number.  it will then take that and turn it into cards for easier math and store both decks and cards to
    a list so that you can return that list.
    :return:
    """
    deck_list = [1, 2, 3, 4, 5]
    user_input = int(input('How many decks would you like to play with (1 to 5): '))
    while user_input not in deck_list:
        user_input = int(input('How many decks would you like to play with (1 to 5): '))
    cards = user_input * 52
    return_list = [user_input, cards]
    return return_list


def guess(streak, cvl, s, cards):
    """
    The user inputs their guess of the running count and true count, the function checks to see if it is correct.
    If false the user will lose 100 points per wrong guess and be told what the counts are.
    If they win, they get their streak to the second power.  This enables users to gamble.
    Also via math, the user is always going to generate a highscore.
    :param cvl:
    :param s:
    :param streak:
    :param cards:
    :return:
    """
    # if the user had a 15 streak of cards
    if streak == 15:
        print('You hit a streak of 15, time to guess the right amount')
    # calculate running count
    running_count = sum(cvl)
    # calculate total count
    decks_remaining = cards // 52
    true_count = running_count // decks_remaining
    # this function returns a list of ints for threshold  in while loop
    thresh_hold = generate_threshold()
    # question user running count
    rc_input = int(input('What is the running count?: '))
    # make sure it is a valid response
    while rc_input not in thresh_hold:
        rc_input = int(input('What is the running count?: '))
    # If user is wrong
    if rc_input != running_count:
        s -= 100
        print(f'You got the running count wrong, it was {running_count}')
    # if user is right
    if rc_input == running_count:
        s = (streak ^ 2) + s
        print('You got it right!')
    # question user true count
    tc_input = int(input(f'There are {decks_remaining} decks remaining, what is the true count?: '))
    # validate response
    while tc_input not in thresh_hold:
        tc_input = int(input(f'There are {decks_remaining} decks remaining, what is the true count?: '))
    if tc_input != true_count:
        s -= 100
        print(f'You got the true count wrong, it was {true_count}')
    if tc_input == true_count:
        s = (streak ^ 2) + s
        print('You got it right!')
    return s


def user_running_guess(running_c, s, streak):
    """
    The user inputs their guess of the running count, the function checks to see if it is correct.
    If false the user will lose 100 points and be told what the running count is.
    If they win, they get their streak to the second power.  This enables users to gamble
    :param running_c:
    :param s:
    :param streak:
    :return:
    """
    # question user
    rc_input = int(input('What is the running count?: '))
    # If user is wrong
    if rc_input != running_c:
        s -= 100
        print(f'You got the running count wrong, it was {running_c}')
    # if user is right
    if rc_input == running_c:
        s = (streak ^ 2) + s
        print('You got it right!')
    return s


def cv(random_card):
    """
    take the random card and find the value of it (+1, 0, -1).  Return value.
    :param random_card:
    :return:
    """
    # +1 value cards
    high = [2, 3, 4, 5, 6]
    card_var = 0
    if random_card in high:
        print('Card = +1')
        card_var = 1
    # -1 value cards
    low = [1, 10, 11, 12, 13]
    if random_card in low:
        print('Card = -1')
        card_var = -1
    # 0 value cards
    none = [7, 8, 9]
    if random_card in none:
        print('Card = 0')
        card_var = 0
    return card_var


def rc(rcl, d):
    """
    This function will generate a random card if called.  Then it will check to see if it has been drawn.
    Once it finds a card that has not been drawn, it will return that card.
    :param rcl:
    :param d:
    :return:
    """
    # create card
    random_card = random.randint(1, 13)
    # the amount of said cards in deck (ie there are 4 aces, 4 kings, 4 queens in one deck)
    amount_of_cards = d * 4
    # see if random_card value has been drawn too many times
    count_amount = rcl.count(random_card)
    # continue drawing cards until a card that is drawn is not at its limit
    while count_amount > amount_of_cards:
        random_card = random.randint(1, 13)
        amount_of_cards = d * 4
        count_amount = rcl.count(random_card)
    # Remove after publish, here for help
    print(random_card)
    return random_card


main()