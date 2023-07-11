import random
# Write your code here


def play_game(word_to_guess) -> bool:
    attempts: int = 0
    lst_hint = [*word_to_guess]
    lst_hint[:] = ["-" for _ in lst_hint[:]]
    won: bool = False
    wrong_input: bool = True
    list_of_guessed_letters = []
    while attempts < 8:
        wrong_input = True
        # print(word_to_guess)
        print()
        print(f"{''.join(lst_hint)}")
        print(list_of_guessed_letters)
        letter_guessed: str = input("Input a letter:")
        # check input
        while wrong_input:
            if len(letter_guessed) != 1:
                print("Please, input a single letter.")
                break
            elif letter_guessed in list_of_guessed_letters:
                print("You've already guessed this letter.")
                break
            elif (ord(letter_guessed) < ord('a')) or (ord(letter_guessed) > ord('z')):
                print("Please, enter a lowercase letter from the English alphabet.")
                break
            else:  # Input was correct
                wrong_input = False
                list_of_guessed_letters.append(letter_guessed)
                # check guessed letter in word
                if letter_guessed in lst_hint:
                    attempts += 1
                    print("No improvements.")
                elif letter_guessed in word_to_guess:
                    for pos, char in enumerate(lst_hint):
                        if char != '-':
                            pass
                        elif letter_guessed == word_to_guess[pos]:
                            lst_hint[pos] = letter_guessed
                else:
                    attempts += 1
                    print("That letter doesn't appear in the word.")

        if "-" not in lst_hint:
            won = True
            break
    return won


if __name__ == "__main__":
    print("H A N G M A N")
    list_of_words = ["python", "java", "swift", "javascript"]
    count_win = 0
    count_lose = 0
    not_exit = True
    while not_exit:
        what_to_do = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if what_to_do == "results":
            print(f"You won: {count_win} times")
            print(f"You lost: {count_lose} times")
        elif what_to_do == "play":
            word_to_guess = random.choice(list_of_words)
            survived = play_game(word_to_guess)
            if survived:
                print()
                print(f"You guessed the word {word_to_guess}!")
                print("You survived!")
                count_win += 1
            else:
                print()
                print("You lost!")
                count_lose += 1
        elif what_to_do == "exit":
            not_exit = False
        else:
            continue
