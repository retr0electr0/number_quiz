while True:
    number = 7

    user_input = input("Would you like to play? (Y/n): ").lower()

    if user_input == 'n':
        print("Quitting...")
        break

    if user_input == 'y':
        user_number = int(input("Guess the number: "))
        if user_number == number:
            print("You guessed right!")
            break
        elif abs(number - user_number) == 1:
            print("You were off by one")
        else:
            print("Sorry, it's wrong...")

    else:
        print("Please, type Y or n")