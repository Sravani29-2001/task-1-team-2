import random


Number = random.randint(1,99)
guess = None
count = 1
while guess!=Number:
  guess = int(input("Enter an integer between 1 and 99:"))
  if guess>Number:
    print("Too high! Try again!")
    count = count+1
  elif guess<Number:
    print("Too low! Try again")
    count = count+1
  elif guess==Number:
    print("Yep! you got it.")
   
print(f"It took you {count} guesses to get it right. ")
    