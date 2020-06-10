#programmingProject_V1.8
#Cameron Galbraith

"""
Changelog
v1.8
Fix map borders
"""

#imports


#variables
question1 = 1 
question2 = 1
question3 = 1
question4 = 1
question5 = 1
score = 0

trash_collected = [] #Where trash you picked up gets stored

moveOffset = (0,0)
gMap = [
["X","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","["]
]

playerPos = (0,4) #position of the player
continueGame = True

#functions


# Set the graphics for a position on the board.
def setPos(pos,letter):
    global gMap
    gMap[4-pos[1]][pos[0]] = letter

# Check if a position is on the board. 
def isPosValid(pos):
    if pos[1] < 0 or pos[1] > 4 or pos[0] < 0 or pos[0] > 4: 
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
    global moveOffset
    displayMap()
    userInput = input("wasd to move \n>>>")
    if userInput.lower() == "w":        #W Moves player Up
        moveOffset = (0,1)   
    elif userInput.lower() == "a":      #A Moves player Left
        moveOffset = (-1,0)  
    elif userInput.lower() == "s":      #S Moves player Down
        moveOffset = (0,-1)
    elif userInput.lower() == "d":      #D Moves player Right
        moveOffset = (1,0)
    else:
        print("You didnt enter the right thing!")
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
        print("How long does a plastic bag live up to in years?") #Question for this rubbish
        userInput = input(">>>")
        if userInput.lower() == "1000": #The answer
            question1 = 1 + 1
            print("Correct") #Tells you that you got it right
            score = score + 1
            trash_collected.append("Plastic Bag")
            print("Number of pieces of trash is: %d"%score) # Tells you how many pieces of trash
                  
        else:
            question1 = 1 + 1
            print("Wrong Plastic bags can live up to 1000 years\nTry find some more trash you only need 3 pieces to complete your mission") #Tells player the answer if wrong

def foundPlastic_Container():
    question2 = 1
    while question2 == 1:
        global score
        print("You found a plastic container answer the question correct to pick up")
        print("Around how many years have plastic been around?") #Question for this rubbish
        userInput = input(">>>")
        if userInput.lower() == "100": #The answer
            question2 = 1 + 1
            print("Correct") #Tells you that you got it right
            score = score + 1
            trash_collected.append("Platic Container")
            print("Number of pieces of trash is: %d"%score)
        else:
            question2 = 1 + 1
            print("Wrong plastic bags have been around for roughly 100 years\nTry find some more trash you only need 3 pieces to complete your mission")     #Tells player the answer if wrong       
    
def foundPlastic_Bottle():
    question3 = 1
    while question3 == 1:
        global score
        print("You found a plastic bottle answer the question correct to pick up")
        print("On Average how long does someone use a plastic bag for in minutes?") #Question for this rubbish
        userInput = input(">>>")
        if userInput.lower() == "12":
            question3 = 1 + 1
            print("Correct")
            score = score + 1
            trash_collected.append("Plastic Bottle")
            print("Number of pieces of trash is: %d"%score)
        else:
            question3 = 1 + 1
            print("Wrong plastic bags are used on average of 12 minutes\nTry find some more trash you only need 3 pieces to complete your mission")            #Tells player the answer if wrong

def foundPile_Gladwrap():
    question4 = 1
    while question4 == 1:
        global score
        print("You found a pile of glad wrap answer the question correct to pick up")
        print("How many plastic bags roughtly does the average American take home each year?") #Question for this rubbish
        userInput = input(">>>")
        if userInput.lower() == "1500":
            question4 = 1 + 1
            print("Correct")
            score = score + 1
            trash_collected.append("Gladwrap")
            print("Number of pieces of trash is: %d"%score)
        else:
            question4 = 1 + 1
            print("Wrong The average American takes home roughtly 1500 plastic bags every year\nTry find some more trash you only need 3 pieces to complete your mission") #Tells player the answer if wrong
def foundMetal_Tin():
    question5 = 1
    while question5 == 1:
        global score
        print("You found a metal tin answer the question correct to pick up")
        print("Around what percent of plastic bags get returned for recycle?") #Question for this rubbish
        userInput = input(">>>")
        if userInput.lower() == "1": #Checks users answer matches the answer
            question5 = 1 + 1
            print("Correct") 
            score = score + 1 #Adds point to the score
            trash_collected.append("Metal Tin") #Adds the trash you picked up to a list
            print("Number of pieces of trash is: %d"%score) #Tells you how many things of trash you have picked up
        else:
            question5 = 1 + 1
            print("Wrong around 1% of plastic bags get returned for recycling \nTry find some more trash you only need 3 pieces to complete your mission")     #Tells player the answer if wrong
    
def endText(): #This prints when you win and says you win and prints what you picked up
    global score # Lets this fuction access the score
    global continueGame
    if score >= 3: #Checks if you picked up over 3 things of trash
        print("Congrats you by picking up rubbish helps just that little bit \nYou found %s"%trash_collected) #Text that plays when you  win
        continueGame = False #Ends game by stopping the main loop
         #Stops the game also
        
    else:
        print("You didnt collect at least 3 pieces of trash \nRestart the game and try again") #if you didnt get 3 you get told that that
        continueGame = False #Ends game by stopping the main loop
        #Stops the game also
    

def displayMap():
    print("\n".join([" ".join(line) for line in gMap]))

#main

print("Hello welcome to my trash game where your mission is to pick up as at least 3 pieces of trash to escape,\nOnce you have 3 or more you pieces of trash travel to the bottom right door to get out")

while continueGame == True:
    move()
    if playerPos == (3,4): #where trash is on map
        foundPlastic_Bag()
    if playerPos == (3,3):  #where trash is on map
        foundPlastic_Container()
    if playerPos == (2,1):      #where trash is on map
        foundPlastic_Bottle()
    if playerPos == (3,2):  #where trash is on map
        foundPile_Gladwrap()
    if playerPos == (1,1):   #where trash is on map
        foundMetal_Tin()  
    if playerPos == (4,0):   #where trash is on map
        endText()      
