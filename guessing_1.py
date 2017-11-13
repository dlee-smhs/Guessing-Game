import random


def computer(upperLimit, guess):
    randNum = int(random.random() * upperLimit + 1)
    count = 0

    for i in range(upperLimit):
        count += 1
        guess = int(guess)

        if randNum > guess:
            print("Higher: ")
            guess = checklevel(1, upperLimit, "guess")
        elif randNum < guess:
            print("Lower: ")
            guess = checklevel(1, upperLimit, "guess")
        else:
            print("\nThat's it! That took you", count, "tries!")
            break

    return count

def guess(upperLimit):
    print("\nTry and guess the random number( 1 -", upperLimit, "): ")
    guess = checklevel(1, upperLimit, "guess")
    count = computer(upperLimit, guess)

    return count


# Checks if user inputs are out of range
def checklevel(low, high, choice):
    while True:
        try:
            level = int(input())
        except ValueError:
            if choice == "difficulty":
                print("You need to choose a level. Try again.")
            elif choice == "versus":
                print("You need to choose a type of game. Try again.")
            else:
                print("You need to enter a guess. Try again.")
            continue
        if level < low or level > high:
            print("That is out of range. Try again!")
            continue
        else:
            return level

def chooseLevel():
    print("\n1 - Easy(10)   2 - Medium(20)   3 - Hard(100)")
    print("Choose what level you would like to play: ")

    # Validates user input, returns user's choice
    return checklevel(1, 3, "difficulty")


def setUpperLimit(level):
    upperLimit = level * 10
    if level == 3:
        upperLimit = 100

    return upperLimit


def main():
    print("\n ::: Welcome to the Guessing Game! :::")

    guess(setUpperLimit(chooseLevel()))

main()