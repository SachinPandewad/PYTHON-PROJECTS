                            #GAME RULES#
                    # rock vs paper, paper win..!
                  # paper vs scissor, scissor win..!
                    # scissor vs Rock, rock win..!


import random

while True:
    user_move = input("Select & Enter your choice from [rock, paper, scissor]: ")
    possible_move = ["rock", "paper", "scissor"]
    computer_move = random.choice(possible_move)
    print("Your Choice is ", user_move, "Computer Choice is", computer_move)

    if user_move == computer_move:
        print("Both Player Selected", {user_move}, "Tie in GAME..!" )
    elif user_move == "rock":
        if computer_move == "scissor":
            print("Rock smashes scissor. You Win The GAME..!")
        if computer_move == "paper":
            print("Paper covers rock. You Lose The GAME..!")

    elif user_move == "paper":
        if computer_move == "scissor":
            print("Scissor cuts paper . You Lose The GAME..!")
        if computer_move == "rock":
            print("Paper covers rock. You Win The GAME..!")

    elif user_move == "scissor":
        if computer_move == "rock":
            print("Rock smashes scissor. You Lose The GAME..!")
        if computer_move == "paper":
            print("Scissor cuts paper. You Win The GAME..!")

    play_again = input("Want to Play again? (y/n): ")
    if play_again.lower() != "y":
        break