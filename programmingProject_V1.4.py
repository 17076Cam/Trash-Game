#programmingProject_V1.0
#Cameron Galbraith

"""
Changelog
v1.4
Add questions
"""

#imports
import random


#variables
question1 = 1 
question2 = 1
question3 = 1
question4 = 1
question5 = 1
score = 0

trash = ["Plastic Bag","Plastic Container","Plastic Bottle","Pile of Glad wrap","Metal Tin"] #Trash you can pick up

gMap = [
["X","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","["]
]

playerPos = (0,3) #position of the player

#functions

# Set the graphics for a position on the board.
def setPos(pos,letter):
    global gMap
    gMap[3-pos[1]][pos[0]] = letter

# Check if a position is on the board. 
def isPosValid(pos):
    if pos[0] < 0 or pos[0] > 4 or pos[0] < 0 or pos[1] > 4: 
        return False
    return True

# Returns FALSE if the player tried to move off the board
def movePlayer(moveOffset):
    global playerPos
    # Move pos
    newPos = (playerPos[0]+moveOffset[0],playerPos[1]+moveOffset[1])
    # Check if moved off the board
    if not isPosValid(newPos):
        return False
    # Update board
    setPos(playerPos,"O")
    setPos(newPos,"X")
    playerPos = newPos
    return True

#Movement controls
def move():
    displayMap()
    print("wasd to move")
    userInput = input(">>> ")

    if userInput.lower() == "w":
        moveOffset = (0,1)   
    elif userInput.lower() == "a":
        moveOffset = (-1,0)  
    elif userInput.lower() == "s":
        moveOffset = (0,-1)
    elif userInput.lower() == "d":
        moveOffset = (1,0)
    else:
        print("You not enter right thing!")
        return
    # If the player tried to move to an invalid location
    if not movePlayer(moveOffset):
        print("You can't move there.")
        return
    #Runs when player finds trash on the map
def foundPlastic_Bag():
    question1 = 1
    while question1 == 1:
        global score
        print("You found a plastic bag answer the question correct to pick up")
        print("How long does a plastic bag live up to in years?")
        userInput = input(">>>")
        if userInput.lower() == "1000":
            question1 = 1 + 1
            print("Correct")
            score = score + 1
            print("Number of pieces of trash is: %d"%score)
                  
        else:
            question1 = 1 + 1
            print("Wrong Plastic bags can live up to 1000 years\nTry find some more trash you only need 3 pieces to complete your mission")

def foundPlastic_Container():
    question2 = 1
    while question2 == 1:
        global score
        print("You found a plastic container answer the question correct to pick up")
        print("Around how many years have plastic been around?")
        userInput = input(">>>")
        if userInput.lower() == "100":
            question2 = 1 + 1
            print("Correct")
            score = score + 1
            print("Number of pieces of trash is: %d"%score)
        else:
            question2 = 1 + 1
            print("Wrong plastic bags have been around for roughly 100 years\nTry find some more trash you only need 3 pieces to complete your mission")            
    
def foundPlastic_Bottle():
    question3 = 1
    while question3 == 1:
        global score
        print("You found a plastic bottle answer the question correct to pick up")
        print("On Average how long does someone use a plastic bag for in minutes?")
        userInput = input(">>>")
        if userInput.lower() == "12":
            question3 = 1 + 1
            print("Correct")
            score = score + 1
            print("Number of pieces of trash is: %d"%score)
        else:
            question3 = 1 + 1
            print("Wrong plastic bags are used on average of 12 minutes\nTry find some more trash you only need 3 pieces to complete your mission")            

def foundPile_Gladwrap():
    question4 = 1
    while question4 == 1:
        global score
        print("You found a pile of glad wrap answer the question correct to pick up")
        print("How many plastic bags roughtly does the average American take home each year?")
        userInput = input(">>>")
        if userInput.lower() == "1500":
            question4 = 1 + 1
            print("Correct")
            score = score + 1
            print("Number of pieces of trash is: %d"%score)
        else:
            question4 = 1 + 1
            print("Wrong The average American takes home roughtly 1500 plastic bags every year\nTry find some more trash you only need 3 pieces to complete your mission")
def foundMetal_Tin():
    question5 = 1
    while question5 == 1:
        global score
        print("You found a metal tin answer the question correct to pick up")
        print("Around what percent of plastic bags get returned for recycle?")
        userInput = input(">>>")
        if userInput.lower() == "1":
            question5 = 1 + 1
            print("Correct")
            score = score + 1
            print("Number of pieces of trash is: %d"%score)
        else:
            question5 = 1 + 1
            print("Wrong around 1% of plastic bags get returned for recycling \nTry find some more trash you only need 3 pieces to complete your mission")    
    
    
    

def displayMap():
    print("\n".join([" ".join(line) for line in gMap]))


while True:
    print("What would you like to do? (m)ove,")
    userInput = input(">>>")
    if userInput.lower() == "m":
        move()
    if playerPos == (3,3):
        foundPlastic_Bag()
    if playerPos == (3,0):
        foundPlastic_Container()
    if playerPos == (4,1):
        foundPlastic_Bottle()
    if playerPos == (2,2):
        foundPile_Gladwrap()
    if playerPos == (1,2):
        foundMetal_Tin()            