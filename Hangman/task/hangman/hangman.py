import random
from string import ascii_lowercase
from collections import namedtuple


words = ["python", "java", "kotlin", "javascript"]
NOT_IN_WORD = "That letter doesn't appear in the word"
ALREADY_GUESSED = "You've already guessed this letter"
LOST = "You lost!"
WON = "You guessed the word!\nYou survived!"
BAD_CHARACTER = "Please enter a lowercase English letter"
BAD_LENGTH = "You should input a single letter"
GuessResult = namedtuple("GameState", "guess_message game_message")


class HangmanGame:
    def __init__(self, word):
        self.solve_word = word
        self.guess_word = "-" * len(self.solve_word)
        self.guessed_letters = set()
        self.guesses_left = 8

    def take_a_guess(self, a_letter):
        guess_message = ""
        game_message = ""
        if len(a_letter) != 1:
            guess_message = BAD_LENGTH
        elif a_letter not in ascii_lowercase:
            guess_message = BAD_CHARACTER
        elif a_letter in self.guessed_letters:
            guess_message = ALREADY_GUESSED
        elif a_letter not in self.solve_word:
            guess_message = NOT_IN_WORD
            self.guesses_left -= 1
        else:
            guess_word_list = [
                letter if a_letter == letter else self.guess_word[i]
                for i, letter in enumerate(self.solve_word)
            ]
            self.guess_word = "".join(guess_word_list)
        self.guessed_letters.add(a_letter)
        if "-" not in self.guess_word:
            game_message = WON
        elif self.guesses_left < 1:
            game_message = LOST
        return GuessResult(guess_message, game_message)

    def play(self):
        print("H A N G M A N")
        print()
        game_over = False
        while not game_over:
            print(self.guess_word)
            letter = input("Input a letter: ")
            guess_result = self.take_a_guess(letter)
            if guess_result.guess_message:
                print(guess_result.guess_message)
            if guess_result.game_message:
                game_over = True
                print(guess_result.game_message)
                print()
            else:
                print()


def main():
    while True:
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == "play":
            game = HangmanGame(random.choice(words))
            game.play()
        elif command == "exit":
            break


if __name__ == "__main__":
    main()
