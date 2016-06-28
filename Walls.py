'''Walls - This program provides a boxed in area for a character to move around in
It could be utilized in games, "choose your path" stories", or simulations where a walled in area is needed.'''


vertical = 0                #starting point North/South
horizontal = 0              #starting point #East/West

def run():                  #Initial function asking the user what they intend to do.
    print('Do you wish to move your character? You are currently located at location : [%d, %d]' %(horizontal, vertical))           #Asks if the user wishes to move and prints out their current location
    print('Press 1 if yes. Press 2 if no.')                                     #Asks the user to type '1' or '2' based on their choice.
    decision = input()                                                          #User Input
    try:
        decision_check = int(decision)                                          #Checks to make sure that the user input an integer.
    except ValueError:
        print('Sorry, you must choose 1 or 2.')                                 #Reminds the user of their options if they type a string or float
        run()                                                                   #Re-runs the function
    while decision_check < 1 or decision_check > 2:                             #While user input is an integer that is less than 1 or greater 2
        print('Sorry, you must choose 1 or 2.')                                 #Reminds user of their options if number is outside of the range that is accepted (1 or 2)
        run()                                                                   #Re-run function
    else:
        if decision_check == 1:                                                 #1 is entered as user input
            movement()                                                          #Movement function is run
        elif decision_check == 2:                                               #2 is entered as user input
            print('You have stopped moving. Ending Program.')
            exit()                                                              #Per user's choice, program is ended



def movement():                                             #Function that will ask which direction user wants to travel and shows them their location
    global vertical                                         #Declaring global variable from outside function
    global horizontal                                       #Declaring global variable from outside function
    print('What direction would you like to move?')
    print('Press 1 to move North. Press 2 to move East. Press 3 to move South. Press 4 to move West. Press 5 to stop movement')
    direction = input()                                     #User Input
    try:
        direction_check = int(direction)                    #Checks to make sure that the user input an integer.
    except ValueError:
        print('Sorry, you must enter 1, 2, 3, 4, or 5.')    #Reminds the user of their options if they type a string or float
        movement()                                          #Re-runs function
    while direction_check < 1 or direction_check > 5:       #While user input is integer, but outside of the acceptable range
        print('Sorry, you must enter 1, 2, 3, 4, or 5.')    #Reminder of what numbers are acceptable inputs
        movement()                                          #Re-run function
    else:
        if direction_check == 1:                            #User input = 1
            if vertical < 1:                                #Setting a limit for how far a user can move North.
                vertical += 1                               #Up increment the vertical value, if the user is not already at the limit established
                print('You have moved North. You are now at location : [%d, %d]' %(horizontal, vertical))   #Tells the user their new location
                movement()                                  #Re-run movement function
            else:                                           #If user is at the Northern limit
                print('You cannot go any further North. You are already located at location : [%d, %d]' %(horizontal, vertical))    #Tells user they can't go any further North and reminds them of their location
                movement()                                  #Re-run movement function
        elif direction_check == 2:                          #Repeat for user input = 2 (East)
            if horizontal < 1:
                horizontal += 1
                print('You have moved East. You are now at location : [%d, %d]' %(horizontal, vertical))
                movement()
            else:
                print('You cannot go any further East. You are already located at location : [%d, %d]' %(horizontal, vertical))
                movement()
        elif direction_check == 3:                          #Repeat for user input = 3 (South)
            if vertical > -1:
                vertical -= 1
                print('You have moved South. You are now at location : [%d, %d]' %(horizontal, vertical))
                movement()
            else:
                print('You cannot go any further South. You are already located at location : [%d, %d]' %(horizontal, vertical))
                movement()
        elif direction_check == 4:                          #Repeat for user input = 4 (West)
            if horizontal > -1:
                horizontal -= 1
                print('You have moved West. You are now at location : [%d, %d]' %(horizontal, vertical))
                movement()
            else:
                print('You cannot go any further West. You are already located at location : [%d, %d]' %(horizontal, vertical))
                movement()
        elif direction_check == 5:                              #User input = 5
            print('You have stopped moving. Ending Program.')   #Tells user they have chosen to stop moving and end program
            exit()                                              #End program

run()
