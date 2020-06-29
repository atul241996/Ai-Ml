secret_no = 9
chances = 3
guess_count = 0
while guess_count < chances:
    guess = input("Provide input > ")
    guess = int(guess)
    if guess == secret_no:
        print("You Win")
        break
    else:
        guess_count += 1
print("Game over!!")