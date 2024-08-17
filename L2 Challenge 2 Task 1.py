import random
count = 1


def random_number():
    return random.randint(0, 100)


def guessing_game():
    global count
    secret_number = random_number()

    while True:
        number = int(input("What's your guess? "))

        if number > secret_number:
            print("Your guess was too large. Try again")
            count += 1
        elif number < secret_number:
            print("Your guess was too small. Try again")
            count += 1
        else:
            print(f"You Won! It took you {
                  count} tries to guess the correct number")
            break


if __name__ == "__main__":
    print(
        "Welcome to the number guessing game! The secret number is between 0 and 100.")
    guessing_game()
