import random
"""
Program to play rock paper scissors
"""


def main():
    """Main function to calculate results and rerun program"""
    print("Rock, Paper, Scissors!")

    # Variables to hold results
    wins = 0
    loses = 0
    ties = 0

    # Determines if user wants program rerun
    result = play()

    # Calculate results as games are played
    if result == "You win":
        wins += 1
    elif result == "You lose":
        loses += 1
    else:
        ties += 1

    # Compile final results
    final_result = f'Human: {wins}\nComputer: {loses}\nTie: {ties}\nGoodbye!'
    response = input("Would you like to play again? (Y/N) ")

    # Print final results if game is ended
    if response != "Y":
        print(final_result)


def play():
    """Function to get player input and determine winner"""

    # Get player input for their move
    player_move = input("Select Rock, Paper, or Scissor and enter your answer: ")

    # If input is not in list, request they re-input
    while player_move not in ['Rock', 'Paper', 'Scissor']:
        player_move = input("Invalid input. Please select Rock, Paper, or Scissor: ")

    # Create computer options and randomize answer
    computer_list = ['Rock', 'Paper', 'Scissor']
    computer_answer = random.choice(computer_list)
    print("Computer plays", computer_answer)

    # Determine win, loss, or draw
    if player_move == computer_answer:
        result = "Draw"

    elif computer_answer == "Rock" and player_move == "Paper":
        result = "You win"

    elif computer_answer == "Paper" and player_move == "Scissor":
        result = "You win"

    elif computer_answer == "Scissors" and player_move == "Rock":
        result = "You win"

    else:
        result = "You lose"

    # Print result of individual rounds
    print(result)
    return result


main()
