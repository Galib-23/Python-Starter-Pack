secret_number = 4

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!!")
        break
else: ######  SO, Like if , while can also have else. if while looped through whole time and condition reached then goes to else block #####
    print("Sorry! You lose.")