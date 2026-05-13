import random 

jackpot = random.randint(1, 100)
guess = int(input("Guess the jackpot number between 1 and 100: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess the jackpot number between 1 and 100: "))
    counter += 1

print("Congratulations! You've guessed the jackpot number:", jackpot)
print("Number of guesses:", counter)
