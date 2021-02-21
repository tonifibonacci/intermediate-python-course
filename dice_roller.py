import random
 

def main():
  dice_rolls=2
  dice_sum=0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dice_sum=dice_sum + roll
    if roll == 1: 
      print('bad luck, you rolled a', roll)
    elif roll == 6:
      print('nice one , you rolled a', roll)
    else:
      print('you roll', roll )

    
  print('the sum of them is', dice_sum)
    



if __name__== "__main__":
  main()










