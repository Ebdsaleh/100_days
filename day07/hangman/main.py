# main.py
# Day 07 Project - hangman
import random
import os
import sys
import hangman_art
import hangman_words

stages = hangman_art.stages
logo = hangman_art.logo

words = hangman_words.word_list
display = []
used_letters = []
selected_word = random.choice(words)
words_solved = 0
end_game = False
lives = 6


def clear_screen():
    OS = sys.platform
    if OS == "linux" or OS == "linux2" or OS == "darwin":
        os.system('clear')
    else:
        os.system('cls')


def setup_display():
    # set up the display
    global display
    global selected_word
    global used_letters
    display = []
    used_letters = []
    clear_screen()
    for letter in selected_word:
        display.append('_')


def update_display(idx: int, val: str):
    display[idx] = val


def show_logo():
    print(f"{logo}")


def show_display():
    clear_screen()
    show_logo()
    print(f"\n\nUsed letters: {used_letters}\n\n")
    print(f"Solve: {display}")
    print(f"Words solved: {words_solved}")
    if lives < 6:
        print(f"{stages[lives]}")


def check_guess(g: str, word):
    safe = True
    used_letters.append(g)
    if g in word:
        safe = True
    else:
        safe = False

    for i in range(0, len(word)):
        if g == word[i]:
            update_display(i, word[i])
    if not safe:
        lose_a_life()


def should_end_game():
    global end_game
    global lives
    if lives < 1:
        end_game = True
    elif '_' in display:
        end_game = False
    else:
        end_game = True
    return end_game


def play_next_level():
    global selected_word
    global words
    global lives
    global end_game
    lives = 6
    selected_word = random.choice(words)
    end_game = False
    setup_display()
    show_display()
    game_loop()


def play_again():
    play_again = input("Would you like to play again? Y/N").lower()
    if play_again[0] == 'y':
        play_next_level()
    elif play_again[0] == "n":
        print("Goodbye.")
        exit()


def game_loop():
    global selected_word
    global lives
    global words_solved
    while not end_game:
        guess = input("Guess a letter: ").lower()
        check_guess(guess, selected_word)
        show_display()
        should_end_game()
    if lives > 0:
        print("You win!")
        words_solved += 1
        play_again()
    else:
        print(f"You lost! The word was: {selected_word}.")
        words_solved = 0
        play_again()


def lose_a_life():
    global lives
    lives -= 1


def game():
    play_next_level()


if __name__ == '__main__':
    game()
