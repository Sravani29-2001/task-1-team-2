import random
game = ["Rock","Paper","Scissors"]
choice = random.choice(game)
opponent = None

count=0
point=0

while True:
  print("Let's Play Rock | Paper | Scissors")
  
  for i in range(1,6):
    print(f"Round {i}")
    opponent = input("Rock?? , Paper?? , Scissors??")
    if opponent== "Rock" and choice== "Rock":
      count=0
      point=0
    elif opponent== "Paper" and choice== "Paper":
      count=0
      point=0
    elif opponent== "Scissors" and choice== "Scissors":
      count=0
      point=0
    elif opponent== "Rock" and choice== "Paper":
      count=count+1
      point=0
    elif opponent== "Paper" and choice== "Scissors":
      count=count+1
      point=0
    elif opponent== "Scissors" and choice== "Rock":
      count=count+1
      point=0
    elif opponent== "Paper" and choice== "Rock":
      count=0
      point=point+1
    elif opponent== "Scissors" and choice== "Paper":
      count=0
      point=point+1
    elif opponent== "Rock" and choice== "Scissors":
      count=0
      point=point+1
  if count>point:
    print("Computer won!Better luck next time!")
  else:
    print("Yayyy! you won!!!")
  again = input("Wanna play again? (yay/nay)?")
  if again=="yay":
    continue
  else:
     break
  


