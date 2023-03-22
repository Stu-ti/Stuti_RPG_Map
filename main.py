###############################################################################
#RPG_Map
#CS 30
#March 20, 2023
#Stuti Sapru
#Version 002
###############################################################################
'''
A simple game using a map

The user gets to choose between moving and not moving through a map of an 
house. If they choose not to move, the program stops running. This is
essentially a quit option. If the user wants to move, they can choose between
North, South,  East and West. The program keeps track of the location of the
user and prints it out for them everytime they're faced with the decision to 
move or not again.
'''

#this indicates the room the user is initially in on a horizontal plane
row = 3
#this variable indicates the room the user is initilly in on a vertical plane
column = 0
#this variable determines whether the code should continue forvever or break
#off
loop = True

#this is a map of the layout of the game
map = [['closet', 'office', 'washroom', 'sauna'],
       ['entrance', 'foyer', 'stairs', 'bedroom1'],
       ['bedroom', 'washroom1', 'bedroom2', 'theatre'],
       ['sunroom', 'kicthen', 'dining', 'gym']]


def move():
    """
    This function allows the user to choose whether they want to move or to
    quit the game. It continues forever until the user chooses to quit the
    game. If the user chooses to move, this function also allows them to
    choose the direction they want to move in.
    """
    #the variables we defined above are called in this function
    global row, column, loop

    #this allows the user to choose between moving or quitting
    walk = input("Do you want to move or not? Your options are Yes or No.")

    #if the user chooses to not move, the game stops
    if walk == "No":
        loop = False

    #if the user chooses to quit, the game stops
    elif walk == "Quit":
        loop = False

    #if the user chooses to move, the game proceeds
    elif walk == "Yes":
        #the user can move North, South, East or West of the default room
        print("\nGood choice! You can move North, South, East or West.")
        direction = input("Where would you like to go?")

        #the user chooses to move North and they move in a room in the row 
        #above
        if direction == "North":
            if row > 0:
                row -= 1

            elif row == 0:
                print("You're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move South and they move in a room in the row 
        #below
        elif direction == "South":
            if row < 3:
                row += 1

            elif row == 3:
                print("You're at the edge of the map. Please choose another "
                "direction")

        #the user chooses to move East and they move in a room in the 
        #column to the right
        elif direction == "East":
            if column < 3:
                column += 1

            elif column == 3:
                print("You're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move North and they move in a room in the
        #column to the left
        elif direction == "West":
            if column > 0:
                column -= 1

            elif column == 0:
                print("You're at the edge of the map. Please choose another "
                      "direction")

        #if the user chooses to quit the game, the game stops
        elif direction == "Quit":
            loop = False

        #the following statement prints if the user types an invalid input
        else:
            print("\nI  didn't understand that. Please try again.")

    #if the user chooses to quit, the game stops
    elif walk == "Quit":
        loop = False

    #the following statement prints if the user types an invalid input
    else:
        print("\nI didn't understand that. Please try again.")


#the initial instructions of the game are printed first and do not loop
#throughout
print("Please type all answers exactly as given in the question."
      "\nFor example, when asked if you want to go North or South, "
      "you would answer 'North' or 'South' only. \n\nHope you enjoy "
      "the game! To stop, type 'Quit'.")

#this allows the code to loop forver until the user decides to quit and it
#also prints the location of the user with every loop
while loop == True:
  print(f"\nYou are in room: {map[row][column]}")
  move()
