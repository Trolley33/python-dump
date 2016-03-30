import random

user_score = 0
comp_score = 0

answers = ['rock', 'paper', 'scissors']

while 1:
  print("You - {} {} - Computer".format(user_score, comp_score))
  ui = input("Rock, paper, or scissors: ").lower()
  # Input is a choice
  if ui in answers:
    comp = random.choice(answers)
    
    if ui == comp:
      print("It's a tie!")
      continue
      
    if ui == 'rock':
      if comp == 'paper':
        print("Paper covers rock!")
        comp_score += 1
      else:
        print("Rock crushes scissors!")
        user_score += 1
        
    elif ui == 'paper':
      if comp == 'rock':
        print("Paper covers rock!")
        user_score += 1
      else:
        print("Scissors cuts paper!")
        comp_score += 1
        
    #Skizzis
    else:
      if comp == 'rock':
        print("Rock crushes scissors!")
        comp_score += 1
      else:
        print("Scissors cuts paper!")
        user_score += 1
        