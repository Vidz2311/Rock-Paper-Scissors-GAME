import random

def choice():
  player_choice=input("Enter your choice (Rock, Paper, Scissors):")
  computer_choice=["Rock", "Paper","Scissors"]
  dict={"player": player_choice, "computer":random.choice(computer_choice)}
  return dict

def winner(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player==computer:
    return "It's a TIE!"

  elif player=="Rock" and computer=="Paper" or player=="Scissors" and computer=="Rock" or player=="Paper" and computer=="Scissors":
    return "You LOSE"
  else:
    return "You WIN"
  
choices= choice()
result= winner(choices["player"], choices["computer"])
print(result)
  

