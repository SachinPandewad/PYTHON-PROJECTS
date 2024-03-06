while True:
    name = input("Type Your Name: ")
    print("Welcome", name, "to this adventure!")

    answer = input("You are on dirt road, it has come to an end. You can left or right. Which way you like to go?").lower()

    if answer == "left":
        answer = input("You come to river, you can walk arround it or swim across? Type walk to walk around and swim to swim accross: ")
        
        if answer == "swim":
            print(name, ", You swim across and were eaten by an aaligator.")
        elif answer == "walk":
            print(name, ", You walked for many miles, ran out of water and you lost the game.")
        else:
            print(name, ', Not a valid option. You Lose.')
    elif answer == 'right':
        answer = input("You come to bridge, it looks weak, do you want to cross it or head back (cross/back)? ")
        
        if answer == "cross":
            answer = input("You cross the bridge and meet a stranger. do you talk to them (yes/no)?")
            
            if answer == "yes" or answer == "y":
                print(name, ", You talk to the stranger and they give you GOLD. You WIN!")
                
            elif answer == "no" or answer == "n":
                print(name,", You ignore the stranger and they are offended. You Lose!")
        elif answer == "back":
            print(name, ", You go back and lose.")
        else:
            print(name, ', Not a valid option. You Lose.')
        
    else:
        print(name, ", Not a valid option. You Lose.")
        
        
    enter_again = input("Want to play again? (y/n): ")
    if enter_again.lower() != "y":
        break