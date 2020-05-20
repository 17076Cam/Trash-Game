#programmingProject_V1.0
#Cameron Galbraith

"""
Changelog
v1.3
Add trash and questions
"""

#imports
import random



#variables

trash = ["Plastic Bag","Plastic Container","Plastic Bottle","Pile of Glad wrap","Metal Tin"] #Trash you can pick up

gMap = [
["X","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"],
["O","O","O","O","O"]
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
def foundTrash():
   print("Works")
   
   
def displayMap():
   print("\n".join([" ".join(line) for line in gMap]))
   

while True:
   print("What would you like to do? (m)ove")
   userInput = input(">>>")
   if userInput.lower() == "m":
      move()
   if playerPos == (3,3):
      foundTrash()
   if playerPos == (3,0):
      foundTrash()
   if playerPos == (4,1):
      foundTrash()
   if playerPos == (2,2):
      foundTrash()
   if playerPos == (1,2):
      foundTrash()            