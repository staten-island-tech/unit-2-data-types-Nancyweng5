#use modeulo to check remainder for 1 factor 
#use a loop to chekc all otential factors range (2,15)
#conditional statement if factor do something
#print the list

isRich = True
is21 = True

def canGamble(isRich, is21) : 
    if isRich == True and is21 == True:
        print("Let it rids!")
    elif isRich == False and is21 == True:
        print("You are too poor, get out")
    elif isRich == False or is21 == False:
        print("you cannot play")