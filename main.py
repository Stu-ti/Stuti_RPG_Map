###############################################################################
#RPG_Inventory
#CS 30
#March 29, 2023
#Stuti Sapru
#Version 003
###############################################################################
'''
A simple game using a map and items in the rooms of the map

The user gets to choose between moving and not moving through a map of an 
house. If they choose not to move, the program stops running. This is
essentially a quit option. If the user wants to move, they can choose between
North, South,  East and West. The program keeps track of the location of the
user and prints it out for them everytime they're faced with the decision to 
move or not again. In every room of the map, there is also an item. This item
is added to the inventory of the user by default. The same item cannot be added
to the user's inventory twice, even if the user goes to the same room more than
one time.
'''

#this indicates the room the user is initially in on a horizontal plane
row = 3
#this variable indicates the room the user is initilly in on a vertical plane
column = 0
#this variable determines whether the code should continue forvever or break
#off
loop = True
#this variable is an empty list that will hold the items collected in each room
inventory = []

#this is a map of the layout of the game
map = [['closet', 'office', 'washroom', 'sauna'],
       ['entrance', 'foyer', 'stairs', 'bedroom1'],
       ['bedroom', 'washroom1', 'bedroom2', 'theatre'],
       ['sunroom', 'kitchen', 'dining', 'gym']]

#this is a nested dictionary that contains all the rooms and their descriptions
map_rooms = {
    'closet': {'Description': 'The closet is filled with dirty mops'},
    'office': {'Description': 'There are papers on every corner of the room'},
    'washroom': {'Description': 'The washroom is slippery'},
    'sauna': {'Description': 'The steam is slipping out through the cracks of'
              ' the door'},
    'entrance': {'Description': 'The entrance is locked'},
    'foyer': {'Description': 'There is a large painting in the middle of the'
              ' foyer'},
    'stairs': {'Description': 'The stairs are long and winding'},
    'bedroom1': {'Description': 'The bedroom is table is filled with coffee'
                 ' mugs'},
    'bedroom': {'Description': 'The bedroom smells is filled with the smell of'
                ' jasmine'},
    'washroom1': {'Description': 'The washroom has a large bathtub in the'
                  'middle'},
    'bedroom2': {'Description': 'The bedroom floor is piled with clothes'},
    'theatre': {'Description': 'The theatre has a popcorn machine'},
    'sunroom': {'Description': 'The sunroom seems to be shining, with sunlight'
                ' spilling in'},
    'kitchen': {'Description': 'The kitchen smells like freshly baked bread'},
    'dining': {'Description': 'The dining room has old dark wood furniture'},
    'gym': {'Description': 'The gym as a variety of machines and weights'}
     }

#this is a nested dictionary that has all the rooms and the items in them
map_items = {
    'closet': {'Item': 'Bleach'},
    'office': {'Item': 'Pen'},
    'washroom': {'Item': 'Lotion'},
    'sauna': {'Item': 'Hot Rock'},
    'entrance': {'Item': 'Slippers'},
    'foyer': {'Item': 'Family Picture'},
    'stairs': {'Item': 'Mat'},
    'bedroom1': {'Item': 'Coffee Mug'},
    'bedroom': {'Item': 'Jasmine Flower'},
    'washroom1': {'Item': 'Toothbrush'},
    'bedroom2': {'Item': 'Book'},
    'theatre': {'Item': 'Popcorn'},
    'sunroom': {'Item': 'Key'},
    'kitchen': {'Item': 'Cupcake'},
    'dining': {'Item': 'Knife'},
    'gym': {'Item': 'Dumbell'}
    }


def get_items():
    """
    This is a funtion that allows the user to view what items they have in 
    their inventory. Additionally, every time the user reachs a certain room,
    the function adds the items of the corresponding room to the inventory. If
    the user reaches a certain room twice, the item of the corresponding room
    is not readded to the inventory.
    """
    #this line of code calls the variable we defined previously
    global inventory
    #this loop prints the item of the room the user went into
    for room in map_items:
        if room == map[row][column]:
            for item in map_items[room]:
                print(f"\nYou found {map_items[room][item]}")
                #this loop adds the item to the user's inventory. If the
                #inventory already has the item, the item is not readded.
                if map_items[room][item] in inventory:
                    print("You already have this in your inventory\n")
                else:
                    inventory.append(map_items[room][item])
    #this loop prints all the items of the inventory for the user. If the user 
    #has no items in their inventory, the loop prints the same to let the user 
    #know
    if len(inventory) != 0:
        for i in inventory:
            print(f"You have: - {i}")
    elif len(inventory) == 0:
        print("Your inventory is empty.\n")


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
    walk = input("\nDo you want to move or not? Your options are Yes or No.")

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
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move South and they move in a room in the row
        #below
        elif direction == "South":
            if row < 3:
                row += 1

            elif row == 3:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move East and they move in a room in the
        #column to the right
        elif direction == "East":
            if column < 3:
                column += 1

            elif column == 3:
                print("\nYou're at the edge of the map. Please choose another "
                      "direction")

        #the user chooses to move North and they move in a room in the
        #column to the left
        elif direction == "West":
            if column > 0:
                column -= 1

            elif column == 0:
                print("\nYou're at the edge of the map. Please choose another "
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
    #this statement prints what room the user is in
    print(f"\nYou are in room: {map[row][column]}")
    #this loop prints the description of the room the user is in
    for key in map_rooms:
        if key == map[row][column]:
            for des in map_rooms[key]:
              print(f"{map_rooms[key][des]}")
    get_items()
    move()
