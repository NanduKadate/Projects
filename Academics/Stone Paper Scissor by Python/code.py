import random

# Stone Paper Scissors
def gameWin(comp, you):

    # Check if user input is valid or not
    if you != 'c' and you != 'p' and you != 's' and you != 'C' and you != 'P' and you != 'S':
        print("Enter Valid Option from Stone (s), Paper(p) and Scissor(c)")
        return 'None'
    
    # If two values are equal, declare a tie!
    elif comp == you:
        return 'Same'

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'p':
            return 1
        elif you == 'c':
            return 0

    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you == 'c':
            return 1
        elif you == 's':
            return 0

    # Check for all possibilities when computer chose c
    elif comp == 'c':
        if you == 's':
            return 1
        elif you == 'p':
            return 0
        
    

print("Comp Turn: Stone(s) Paper(p) or Scissors(c)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'c'

you = input("Your Turn: Stone(s) Paper(p) or Scissors(c)?")
result = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if result == 'None':
    print("Please start again!")
if result == 'Same':
    print("The game is a tie!")
elif result == 1:
    print("You Win!")
elif result == 0:
    print("You Lose!")
