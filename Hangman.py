# hangman
import random
from words import words_list


def get_word():  # defining a function that  choose randomly a word from the list of words in words.py
    word = random.choice(words_list)
    return word.upper()


def play(word):  # defining a function to play the game hangman and which takes the word chosen in parameter
    word_completion = "_" * len(word)  # defining a string which only contains underscores corresponding to the number
    # of letters of the word chosen randomly by the computer
    guessed = False  # boolean variable corresponding to the fact if a word has been guessed or not
    guessed_letters = []  # defining a list that holds the letters the user guessed
    guessed_words = []  # defining a list that holds the words the user guessed
    tries = 6  # number of tries corresponding to the number of bones left on the hangman before the user loses counting
    # the head, the body , both legs and both arms
    print("\n")
    print("--------------------------------------------------------------------------------- LET'S PLAY HANGMAN "
          "!!!---------------------------------------------------------------------------------------------------")
    print("\n")  # printing a new empty line
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():  # isalpha() returns True if the characters are alphabet letters (a-z)
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)  # Add the letters guessed in the previous guessed letters
            else:
                print("Well done,", guess, "is in the word !")
                guessed_letters.append(guess)
                # updating the variable word completion to reveal to the user all occurrences of a guess
                words_as_list = list(word_completion)  # creating a list of word_completion in order to index into it
                # finding all the occurrences when a guess appears in a word
                indices = [i for i, letter in enumerate(word) if letter == guess]  # creating an enumeration to find
                # both the index i and letter at the index for each iteration we'll append i to the list if the
                # corresponding letter == guess
                for index in indices:  # using a for loop over indices to replace each underscores at index with guess
                    words_as_list[index] = guess
                word_completion = "".join(words_as_list)  # updating word_completion with the new changes by calling
                # empty string.join on words as list to convert it back to a string
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):  # defining a function that returns a list of the hangman state :
    # [ full; without 1 leg; without 2 legs; without 2 legs and 1 arm; without 2 legs and 2 arms;
    # without 2 legs, 2 arms and the torso; empty ]
    stages = [  # final state: head, torso, both arms, and both legs
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                  -
                  """,
        # head, torso, both arms, one leg
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                  """,
        # head, torso, both arms
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -
                  """,
        # head, torso, one arm
        """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                  """,
        # head, torso
        """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                  """,
        # head
        """
                    --------
                    |      |
                    |      O
                    |     
                    |      
                    |     
                    -
                  """,
        # initial state
        """
                    --------
                    |      |
                    |      
                    |     
                    |      
                    |     
                    -
                  """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while True:
        user = input("Play Again? (YES/NO):  ").upper()
        if user == "YES":
            word = get_word()
            play(word)
        elif user == "NO":
            print("OK,Thanks and Goodbye")
            break


if __name__ == "__main__":
    main()
