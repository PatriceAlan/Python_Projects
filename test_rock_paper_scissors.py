import pytest
import random
import ansi2html
from rock_paper_scissors import *


# Test for is_valid_response function
@pytest.mark.parametrize("user_response", ["rock", "paper", "scissors"])
def test_is_valid_response(user_response):
    assert is_valid_response(user_response)  # Check if the response is a valid choice
    assert user_response in choices  # Check if the response is in the choices list


# Test for is_winning_response function
def test_is_winning_response():
    response2 = "scissors"
    response1 = "rock"
    assert is_winning_response(response1, response2)  # Check if response1 wins over response2


# Test for is_a_tie function
def test_is_a_tie():
    response1 = "scissors"
    response2 = "paper"
    expected_result = False
    result = is_a_tie(response1, response2)  # Check if response1 and response2 are not the same (not a tie)
    assert result == expected_result


# Test for clear_console function
def test_clear_console():
    clear_console()  # Check if the function executes without any errors


# Test for game_message function
def test_game_message():
    input_result = text2art("ROCK PAPER SCISSORS")
    expected_result = text2art("ROCK PAPER SCISSORS")  # Expected ASCII art for the game message
    assert input_result == expected_result  # Check if the actual output matches the expected output


# Test for print_welcome_message function
def test_print_welcome_message():
    out = cyan_color + text2art("ROCK   PAPER   SCISSORS") + cyan_color + text2art("The Game", font="block",
                                                                                   chr_ignore=True)

    # Expected output: The welcome message printed in bright cyan color
    expected_output = print_welcome_message()

    # Check if the actual printed output matches the expected output
    assert out != expected_output


# Test for get_user_response function
@pytest.mark.parametrize("user_response", ["rock", "paper", "scissors"])
def test_get_user_response(user_response):
    is_valid_response(user_response)
    assert user_response in choices


# Test for get_computer_response function
def test_computer_response():
    assert get_computer_response()


# Test for the display_results function
@pytest.mark.parametrize("user_response, computer_response",
                         [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")])
def test_display_results(user_response, computer_response):
    result = display_results(user_response, computer_response)
    assert result == "user"  # Since the provided inputs result in the user winning in each case


# Test for the play_again function
def test_play_again(monkeypatch):
    # Simulate user input of "yes" (or "y")
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    expected_output = play_again()
    assert expected_output == True

    # Simulate user input of "no" (or "n")
    monkeypatch.setattr('builtins.input', lambda _: "no")
    expected_output = play_again()
    assert expected_output == False



