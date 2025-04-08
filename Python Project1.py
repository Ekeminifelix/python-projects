name = input ("Please enter your name: ")
print ("Haloo", name, "welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
if should_we_play == "yes" or should_we_play == 'y':
    print("We are going to play!")
    weapon = input("choice of weapon (sword, axa, GPMG, javalin) ").lower()
    
    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction =="left":
        print("You went to the wrong direction and you fall off the cliff. GAME OVER!! ")
    elif direction == "right":
        choice = input ("Okay, you now on the bridge, do you want to swim or cross the bridge? (swim/cross) ").lower()
        if choice == "swim" and weapon == "sword":
            print("you've just killed an alligator. BRAVO ")
        #elif choice == "swim" and weapon == "axe" or 'GPMG' or 'Javaline':
            #print("sorry, you were eaten by the aligator.. Better luck next time")
        if choice == cross:
            pick = input ("Okay, you are close uncovering the treasure. Do you want to run or drive? (run/drive) ").lower()
            if pick == run:
                print("sorry, your energy is low and you have been eliminated. Better luck next time ")
            elif pick == drive:
                print("You have found the hidden treasure. CONGRATULATIONS")
                
    
    else:
        print("sorry!! this is an invalid reply")

else:
    print("So sad we will not be playing")




