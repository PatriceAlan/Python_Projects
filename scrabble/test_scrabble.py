from unittest.mock import patch
import pytest

from scrabble import *


@pytest.mark.parametrize("user_input", [
    ("John", "10", "Y"),
    ("Alice", "7", "N"),
    ("Martinez", "8", "N")
])
def test_play_game(user_input):
    with patch('builtins.input', side_effect=user_input):
        username, number_of_drafts, total_drafts = play_game()

    assert username == user_input[0]
    assert number_of_drafts == int(user_input[1])
    assert total_drafts == user_input[2]


@patch("builtins.open")
def test_show_words_scrabble(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.__iter__.return_value = [
        "apple\n",
        "banana\n",
        "orange\n",
        "mango\n",
        "kiwi\n"
    ]

    expected_result = {
        "apple": True,
        "banana": True,
        "orange": True,
        "mango": True,
        "kiwi": True
    }

    result = show_words_scrabble()
    assert result == expected_result
    mock_open.assert_called_once_with("french_word_list.txt", "r")


def test_scrabble_letters_generator():
    expected_result = "AAAAAAAAABBCCDDDEEEEEEEEEEEEEEEFFGGHHIIIIIIIIJKLLLLLMMMNNNNNNOOOOOOPPQRRRRRRSSSSSSTTTTTTUUUUUUVVWXYZ"
    result = scrabble_letters_generator()
    assert result == expected_result


def test_play_scrabble(monkeypatch):
    input_values = ["John", "10", "Y"]
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))

    expected_result = ("John", 10, "Y")
    result = play_game()

    assert result == expected_result


def test_calculate_points():
    # Test a word with all lowercase letters
    assert calculate_points("hello") == 8

    # Test a word with mixed case letters
    assert calculate_points("WORLD") == 15

    # Test an empty word
    assert calculate_points("") == 0

    # Test a word with letters not in the points dictionary
    assert calculate_points("xyz") == 30

    # Test a word with special characters
    assert calculate_points("!@#$%") == 0

    # Test a word with spaces
    assert calculate_points("hello world") == 23

    # Test a word with letters and numbers
    assert calculate_points("hello123") == 8

    # Test a word with non-ASCII characters
    assert calculate_points("café") == 8

    # Test a long word
    assert calculate_points("supercalifragilisticexpialidocious") == 58
