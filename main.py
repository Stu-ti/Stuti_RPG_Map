###############################################################################
#RPG_Map
#CS 30
#March 20, 2023
#Stuti Sapru
#Version 001
###############################################################################
'''
A simple game using a map

The user gets to choose between moving and not moving. If they choose not to
move and the program stops running. This is essentially a quit option. If the
user wants to move, they can choose between North, South, East and West. The
program keeps track of the location of the user and prints it out for them
everytime they're faced with the decision to move or not again.
'''

#this indicates the room the user is initially in on a horizontal plane
row = 3
#this indicated the room the user is initilly in on a vertical plane
column = 0
#this loop determines whether the code should continue forvever or break off
loop = True

#this is a map of the layout of the game
map = [['closet', 'office', 'washroom', 'sauna'],
       ['entrance', 'foyer', 'stairs', 'bedroom1'],
       ['bedroom', 'washroom1', 'bedroom2', 'theatre'],
       ['sunroom', 'kicthen', 'dining', 'gym']]


def move():
  global row, column, loop
  #this allows the user to choose between moving or quitting
  walk = input("Do you want to move or not? Your options are Yes or No.")

    #if the user chooses to not move, the game stops
    if walk == "No":
        loop = False

    #if the user chooses to move, the game proceeds
    elif walk == "Yes":
        #the user can move North, South, East or West of the default room
        print("Good choice! You can move North, South, East or West.")
        direction = input("Where would you like to go?")

        #the user moves North
        if direction == "North":
            if row > 0:
            row -= 1

        elif row == 0:
            print("You're at the edge of the map. Please choose another "
                  "direction")

        #the user moves South
        elif direction == "South":
            if row < 3:
            row += 1

        elif row == 3:
            print("You're at the edge of the map. Please choose another "
                  "direction")

        #the user moves East
        elif direction == "East":
            if column < 3:
            column += 1

        elif column == 3:
            print("You're at the edge of the map. Please choose another "
                  "direction")

       #the user moves West
        elif direction == "West":
            if column > 0:
            column -= 1

        elif column == 0:
            print("You're at the edge of the map. Please choose another "
                  "direction")

        #the user has chosen to quit the game
        elif direction == "Quit":
            loop = False

        #the user has an invalid input
       else:
          print("\nI didn't understand that. Please restart the game and try"
               " again.")

   #the user has chosen to quit the game
    elif walk == "Quit":
        loop = False

    #the user has an invalid input
    else:
        print("\nI didn't understand that. Please restart the game and try"
              " again.")


#the initial instructions of the game are printed first and do not loop
print("Please type all answers exactly as given in the question."
      "\nFor example, when asked if you want to go North or South, "
      "you would answer 'North' or 'South' only. \n\nHope you enjoy "
      "the game! To stop, type 'Quit'.")
#allows the code to loop forver until the user decides to quit
while loop == True:
  print(f"You are in room: {map[row][column]}")
  move()