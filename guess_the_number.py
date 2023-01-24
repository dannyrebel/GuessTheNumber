import random
import colorama

number_choice = random.randint(1, 100)
attempts = 0
# Game logic

while True:
    player_choice = input(colorama.Fore.LIGHTWHITE_EX + "Guess the number!: ")

    if not player_choice.isnumeric():
        print(colorama.Fore.RED + f"That's not a number! Please input a number and try again.")
        continue

    if int(player_choice) == number_choice:
        print(colorama.Fore.LIGHTGREEN_EX + f"You got it! The correct number was: {number_choice}")
    elif int(player_choice) > number_choice:
        print(colorama.Fore.RED + "Too high!")
        attempts += 1
    elif int(player_choice) < number_choice:
        print(colorama.Fore.RED + "Too low!")
        attempts += 1

    if attempts == 4:
        print(colorama.Fore.RED + f"Game over! 4 attempts reached.")
        break
    else:
        print(colorama.Fore.YELLOW + f"-{4 - attempts} attempts left-")
