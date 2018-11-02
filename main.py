import random as ran

#This function will convert the random integer value to r, p, s.
def convertor(input1):
    test = 'rps'
    return test[input1]

#This function will evaluate the winner based on the conditions.
def printWinner(a,b):
    if (player==comp):
        print("DRAW")
    #For Rock Case
    elif(player=='r' and comp=='p'):
        print("Computer Wins")
    elif(player=='r' and comp=='s'):
        print("Player Wins")
    #For Paper Case
    elif(player=='p' and comp=='r'):
        print("Player Wins")
    elif(player=='p' and comp=='s'):
        print("Computer Wins")
    #For Scissors Case
    elif(player=='s' and comp=='r'):
        print("Computer Wins")
    elif(player=='s' and comp=='p'):
        print("Player Wins")
    return

#This function will show some graphical content on screen during run time
def toAsciiChar(a):
    if(a=='p'):
        return "|"
    if(a=='r'):
        return "O"
    if(a=='s'):
        return "8<"

player = input("Rock(r) , Paper (p) or Scissors (s) ")
# lower func is called as someone can enter a uppercase input
player.lower()
comp = ran.randint(0,2)  #comp means computer
comp = convertor(comp)
print(toAsciiChar(player)," VS ",toAsciiChar(comp))
printWinner(player,comp)
#loop the code in the event of a tie to allow the player to play again
while player == comp:
    print("Try Again.")
    player = input("Rock(r) , Paper (p) or Scissors (s) ")
    print(toAsciiChar(player), " VS ", toAsciiChar(comp))
    printWinner(player, comp)
