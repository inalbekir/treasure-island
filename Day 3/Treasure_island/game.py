print("Welcome to the Treasure Island.")

left_right = input("Your mission is to find the treasure. Do you want to go left or right?")
if left_right == "left":
    print("You come to a lake. There is island of the middle of the lake.")
    wait_swim = input("Type 'wait' to wait for boat or type 'swim' to swim across the lake.")
    if wait_swim == "wait":
        print("You arrive at the harvard unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        colour = input("Which color do you choose?")
        if colour == "blue":
            print("You enter in a room of beast. Game Over!")
        elif colour == 'yellow':
            print("You enter in a room of wolves. Game Over!")
        else:
            print("Congratulations! You escaped!")
    else:
        print("Game Over!")
else:
    print("Game Over!")