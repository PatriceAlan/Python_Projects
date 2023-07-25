# Importing the necessary modules for the program
import random
from art import text2art

FRENCH_WORD_LIST: str = 'french_word_list.txt'


def game_message():
    """Display the game message in ASCII art."""
    ascii_art = text2art("SCRABBLE")
    print(ascii_art)
    ascii_art = text2art("Le Jeu", font="block", chr_ignore=True)
    print(ascii_art)


def show_words_scrabble():
    """Sort and return the allowed words in Scrabble from a word list file.

    Returns:
        dict: A dictionary containing the allowed words in Scrabble.
    """
    with open(FRENCH_WORD_LIST, "r") as file:
        allowed_words_in_scrabble = {}
        for line in file:
            word = line.strip()
            if len(word) < 9:
                allowed_words_in_scrabble[word] = True
    return allowed_words_in_scrabble


def scrabble_letters_generator():
    """Generate the number of occurrences of letters in Scrabble.

    Returns:
        str: A string containing all the letters in Scrabble.
    """
    letters_occurrences = {
        "A": 9, "B": 2, "C": 2, "D": 3, "E": 15, "F": 2, "G": 2, "H": 2,
        "I": 8, "J": 1, "K": 1, "L": 5, "M": 3, "N": 6, "O": 6, "P": 2,
        "Q": 1, "R": 6, "S": 6, "T": 6, "U": 6, "V": 2, "W": 1, "X": 1,
        "Y": 1, "Z": 1
    }
    scrabble_letters = ""
    for letter, letter_value in letters_occurrences.items():
        for _ in range(letter_value):
            scrabble_letters += letter
    return scrabble_letters


def play_game(player=None):
    """Start the game by asking the number of players, their usernames, number of drafts, and letter options.

    Args:
        player (str, optional): The username of the player. Defaults to None.

    Returns:
        tuple: A tuple containing the username, number of drafts, and letter option.
    """
    if player is None:
        print("Quel est votre nom: ")
        username = input("-> ")
    else:
        username = player

    while True:
        try:
            print(f"{username}, Combien de tirages (5 à 15):")
            number_of_drafts = int(input("-> "))
            if 5 <= number_of_drafts <= 15:
                break
            else:
                print("Le nombre de tirages doit être compris entre 5 et 15. Réessayez.")
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre entre 5 et 15.")

    while True:
        try:
            print("Tirage à chaque fois de 8 lettres (Y/N) ?: ")
            total_drafts = input("-> ").upper()
            if total_drafts == "Y" or total_drafts == "N":
                break
            else:
                print("Répondez par 'Y' pour oui ou 'N' pour non. Réessayez.")
        except ValueError:
            print("Entrée invalide. Veuillez saisir 'Y' pour oui ou 'N' pour non.")

    if total_drafts == "EXIT":
        print("You have exited the game.")
        return None

    return username, number_of_drafts, total_drafts


def calculate_points(player_word):
    """Calculate the number of points for a player's word.

    Args:
        player_word (str): The word submitted by the player.

    Returns:
        int: The number of points for the word.
    """
    points_per_letter = {
        "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
        "k": 10, "l": 1, "m": 2, "n": 1, "o": 1, "p": 3, "q": 8, "r": 1, "s": 1, "t": 1,
        "u": 1, "v": 4, "w": 10, "x": 10, "y": 10, "z": 10
    }
    score = 0
    for letter in player_word:
        score += points_per_letter.get(letter.lower(), 0)
    return score


def display_score(player, total_score):
    """Display the score of a player in ASCII art.

    Args:
        player (str): The name of the player.
        total_score (int): The total score of the player.
    """
    ascii_art = text2art(f"Score de {player}:")
    print(ascii_art)
    ascii_art = text2art(str(total_score), font="block", chr_ignore=True)
    print(ascii_art)


def main():
    """Main function of the program."""
    game_message()

    allowed_words_in_scrabble = show_words_scrabble()
    print("Dictionnaire des mots autorisés de 8 lettres max:", len(allowed_words_in_scrabble))

    scrabble_letters = scrabble_letters_generator()

    print("Combien de joueurs vont jouer ? (1 ou plus)")
    while True:
        try:
            num_players = int(input("-> "))
            if num_players >= 1:
                break
            else:
                print("Veuillez saisir un nombre supérieur ou égal à 1.")
        except ValueError:
            print("Entrée invalide. Veuillez saisir un nombre.")

    players = []
    for i in range(num_players):
        player = input(f"Nom du joueur {i + 1}: ")
        players.append(player)

    scores = {}

    for player in players:
        user_input = play_game(player)
        if user_input is None:
            return

        username, number_of_drafts, total_drafts = user_input

        total_score = 0
        score = 0

        if total_drafts == "Y":
            for _ in range(number_of_drafts):
                available_letters = list(scrabble_letters)
                drawn_letters = []

                for _ in range(8):
                    letter = random.choice(available_letters)
                    drawn_letters.append(letter)
                    available_letters.remove(letter)

                scrabble_letters = "".join(available_letters)
                print("Voici votre tirage: ", drawn_letters)
                print("Votre Mot SVP ? :")
                print("Vous pouvez quitter le jeu en insérant le mot: exit")
                player_word = input("-> ").upper()

                if player_word == "EXIT":
                    exit_message = text2art("Vous avez mis fin au jeu.")
                    print(exit_message)
                    break

                available_letters = list(drawn_letters)
                ok = True
                for letter in player_word:
                    if letter in available_letters:
                        available_letters.remove(letter)
                    else:
                        ok = False
                        break

                if not ok:
                    print("Mot proposé n'est pas possible par rapport au tirage")
                    score = 0
                else:
                    found = allowed_words_in_scrabble.get(player_word, False)
                    if not found:
                        print("Mot proposé n'est pas dans le dictionnaire des mots autorisés")
                        score = 0
                    else:
                        score = calculate_points(player_word)

                total_score += score
                print("Score pour ce mot: ", score)
                display_score(username, total_score)
        elif total_drafts == "N":
            available_letters = list(scrabble_letters)
            for _ in range(number_of_drafts):
                if len(available_letters) < 8:
                    break

                drawn_letters = []
                for _ in range(8):
                    letter = random.choice(available_letters)
                    drawn_letters.append(letter)
                    available_letters.remove(letter)

                print("Voici votre tirage: ", drawn_letters)
                print("Votre Mot SVP ? :")
                print("Vous pouvez quitter le jeu en insérant le mot: exit")
                player_word = input("-> ").upper()

                if player_word == "EXIT":
                    exit_message = text2art("Vous avez mis fin au jeu.")
                    print(exit_message)
                    break

                ok = True
                for letter in player_word:
                    if letter in drawn_letters:
                        drawn_letters.remove(letter)
                    else:
                        ok = False
                        break

                if not ok:
                    print("Mot proposé n'est pas possible par rapport au tirage")
                    score = 0
                else:
                    found = allowed_words_in_scrabble.get(player_word, False)
                    if not found:
                        print("Mot proposé n'est pas dans le dictionnaire des mots autorisés")
                        score = 0
                    else:
                        score = calculate_points(player_word)

                total_score += score
                print("Score pour ce mot: ", score)
                display_score(username, total_score)

        scores[username] = total_score

    winner = max(scores, key=scores.get)
    print(f"Le gagnant est {winner} avec un score de {scores[winner]} points !")


if __name__ == "__main__":
    main()
