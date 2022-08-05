import random
number = random.randint(1,9)
#number = 5
chance = 0
guess = int(input("Guess a number between 1 and 9: "))
chance = chance + 1

while chance < 5:
  chance = chance + 1

  if number == guess:
    print("YOU GOT IT! WELL DONE!!!")
    break
  elif number > guess:
    guess = int(input("Guess is too low! Guess again... "))
  elif number < guess:
    guess = int(input("Guess is too high! Guess again... "))

  if not chance < 5:
    print("YOU LOSE!! The number was", number)

