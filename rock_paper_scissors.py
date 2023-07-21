import os
import random
import time
from art import text2art


# The list of valid choices in the game: rock, paper, and scissors
choices = ["rock", "paper", "scissors"]

# ANSI escape code for setting the text color to bright cyan
cyan_color = "\033[1;36m"


def is_valid_response(response):
    """Check if the user's response is a valid choice."""
    return response in choices


def is_winning_response(response1, response2):
    """Check if response1 wins over response2."""
    return (
        (response1 == "rock" and response2 == "scissors")
        or (response1 == "paper" and response2 == "rock")
        or (response1 == "scissors" and response2 == "paper")
    )


def is_a_tie(response1, response2):
    """Check if response1 and response2 are the same, indicating a tie."""
    return response1 == response2


def clear_console():
    """Clear the console screen."""
    if os.name == "posix":  # Unix-based systems (Linux and macOS)
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


def game_message():
    """Display the game message in ASCII art."""
    ascii_art = text2art("ROCK   PAPER   SCISSORS")
    print(ascii_art)
    ascii_art = text2art("The Game", font="block", chr_ignore=True)
    print(ascii_art)


def print_welcome_message():
    """Print the welcome message and ASCII art for the game."""
    print(cyan_color)
    game_message()


def get_user_response():
    """Get the user's response and validate it until a valid response is provided."""
    while True:
        print("Type your choice: (ROCK, PAPER OR SCISSORS)")
        user_response = input("-> ").lower()
        if is_valid_response(user_response):
            return user_response
        print("Not a valid option. Expecting:", ", ".join(choices))


def get_computer_response():
    """Generate a random response for the computer."""
    print("Computer is thinking...")
    time.sleep(0.5)
    return random.choice(choices)


def display_results(user_response, computer_response):
    """Display the user's choice, the computer's choice, and the game result."""
    print("You choose:", user_response)
    print("Computer choose:", computer_response)
    print()

    if is_a_tie(user_response, computer_response):
        print("IT'S A TIE!!!")
    elif is_winning_response(user_response, computer_response):
        print(f"{user_response} beats {computer_response}")
        print("YOU WIN!!!")
        return "user"
    else:
        print(f"{computer_response} beats {user_response}")
        print("YOU LOSE!")
        return "computer"


def play_again():
    """Ask the user if they want to play again and return True if yes, False if no."""
    while True:
        print("Do you want to play again? (yes/no) ")
        play_again_response = input("-> ").lower()
        if play_again_response in ["yes", "no", "y", "n"]:
            return play_again_response == "yes" or play_again_response == "y"


def main():
    """Main function of the application"""
    clear_console()
    print_welcome_message()

    print("Please enter your name:")
    user_name = input("-> ").capitalize()
    print(f"\nHello {user_name}, let's play!\n")

    print("How many rounds?")
    game_rounds = int(input("-> "))

    user_points = 0
    computer_points = 0
    game_turns = 0

    while game_turns < game_rounds:
        user_response = get_user_response()
        computer_response = get_computer_response()

        winner = display_results(user_response, computer_response)
        if winner == "user":
            user_points += 1
        elif winner == "computer":
            computer_points += 1

        round_number = game_turns + 1
        print(f"Round : {round_number}")
        print(f"{user_name} Points: {user_points} | Computer Points: {computer_points}\n")
        game_turns += 1

    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("Final Results:")
    print(f"{user_name} Points: {user_points} | Computer Points: {computer_points}")

    if user_points > computer_points:
        ascii_winner = text2art(f"{user_name}")
        print(ascii_winner)
        print("\nCongratulations! You won!")
    elif user_points < computer_points:
        ascii_winner = text2art("Computer")
        print(ascii_winner)
        print("\nComputer wins! Better luck next time.")
    else:
        ascii_winner = text2art("Tie")
        print(ascii_winner)
        print("\nIt's a tie! Good game!")

    print("Have a good day!")


if __name__ == "__main__":
    main()
