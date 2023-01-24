import random
import colorama

number_choice = random.randint(1, 100)
attempts = 0
is_Over = False
is_Passed = False
print("Welcome to 'Guess the Number' by Danny!\nYou have 5 attempts to guess the number(1-100)\
 and pass to the next level.\n"
      "Good luck!")


while True:
    # Repeatability after losing
    if is_Over:
        while True:
            restart = str(input(colorama.Fore.LIGHTWHITE_EX + "Play again?: (y / n): "))
            if restart == "y" or restart == "Y":
                attempts = 0
                break
            elif restart == "n" or restart == "N":
                print("Goodbye!")
                raise SystemExit
            else:
                print(colorama.Fore.RED + "Invalid option, please confirm your choice.")
                continue

    # Next level
    if is_Passed:
        print("Congratulations, you have reached the next, level!\n"
              "You have 5 attempts to guess the new number(1-200).\n"
              "Good luck!")
        number_choice = random.randint(1, 200)
        attempts = 0

    is_Over = False
    is_Passed = False

    # Game logic
    player_choice = input(colorama.Fore.LIGHTWHITE_EX + "Guess the number: ")

    if not player_choice.isnumeric():
        print(colorama.Fore.RED + f"That's not a number! Please input a number and try again.")
        continue

    if int(player_choice) == number_choice:
        print(colorama.Fore.LIGHTGREEN_EX + f"You got it! The correct number was: {number_choice}")
        is_Passed = True
        continue
    elif int(player_choice) > number_choice:
        print(colorama.Fore.RED + "Too high!")
        attempts += 1
    elif int(player_choice) < number_choice:
        print(colorama.Fore.RED + "Too low!")
        attempts += 1

    if attempts == 5:
        print(colorama.Fore.RED + f"Game over! 5 attempts reached.")
        is_Over = True
    else:
        print(colorama.Fore.YELLOW + f"-{5 - attempts} attempts left-")
