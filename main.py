import random
import os
from words import word_list
from art import logo, stages


invalid = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", 
    "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", 
    "/", "?", "`", "~", "_",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]


while True:

    display = []
    guessed = []
    word_string = ""
    chosen_word = random.choice(word_list)
    for char in chosen_word:
        if char == ' ':
            display.append(' ')
        else:
            display.append('_')
    found_match = False
    end_game_win = False
    end_game_lose = False
    player_lives = 6

    print(f"{logo}\n")

    while True:
        guess = (input("Guess a letter: ")).lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            print(word_string)
            print(stages[player_lives])
            guessed_list = list(set(guessed))
            guessed_display = " ".join(guessed_list)
            print(f"Your guessed letters: {guessed_display.upper()}")
            continue
        if guess == ' ':
            print("Invalid input.")
            print(word_string)
            print(stages[player_lives])
            guessed_list = list(set(guessed))
            guessed_display = " ".join(guessed_list)
            print(f"Your guessed letters: {guessed_display.upper()}")
            continue
        if guess in invalid:
            print("Invalid input.")
            print(word_string)
            print(stages[player_lives])
            guessed_list = list(set(guessed))
            guessed_display = " ".join(guessed_list)
            print(f"Your guessed letters: {guessed_display.upper()}")
            continue
        found_match = False
        if guess in guessed:
            print(f"You've already guessed the letter {guess.upper()}.")
            print(word_string)
            print(stages[player_lives])
            guessed_list = list(set(guessed))
            guessed_display = " ".join(guessed_list)
            print(f"Your guessed letters: {guessed_display.upper()}")
            continue
        for i, char in enumerate(chosen_word):
            if char == guess:
                display[i] = char
                guessed.append(guess)
                found_match = True
        if found_match:
            print("Correct!")
        if not found_match:
            guessed.append(guess)
            player_lives -= 1
            if player_lives == 0:
                end_game_lose = True
            print(f"The letter {guess.upper()} is not in the word.")
        word_string = " ".join(display)
        print(word_string)
        print(stages[player_lives])
        guessed_list = list(set(guessed))
        guessed_display = " ".join(guessed_list)
        print(f"Your guessed letters: {guessed_display.upper()}")
        if list(chosen_word) == display:
            end_game_win = True
        if end_game_win:
            print("You guessed the word correctly!")
            while True:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again == "y":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                elif play_again == "n":
                    print("Thank you for playing!")
                    exit()
                else:
                    print("Invalid input.")
            break
        if end_game_lose:
            print(f"You lose!\nThe word was {chosen_word}")
            while True:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again == "y":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                elif play_again == "n":
                    print("Thank you for playing!")
                    exit()
                else:
                    print("Invalid input.")
            break