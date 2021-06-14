import random

while True:
    user_action=input("Enter a choice (rock, paper, sccissor):")
    possible_action=["rock", "paper", "scissors"]
    computer_action=random.choice(possible_action)
    print(f"\nYou Choose",user_action)
    print(f"\ncomputer Choose",computer_action)

    if user_action == computer_action:
        print(f"both player selected {user_action}. it is a tie")

    elif user_action=="rock":
        if computer_action =="scissors":
            print("Rock smashed scissors>> <<YOU WIN>>")
        else:
            print("paper cover rock>> <<YOU LOSE>>")

    elif user_action=="paper":
        if computer_action =="rock":
            print("paper cover rock>> <<YOU WIN>>")
        else:
            print("scissor cuts paper>> <<YOU LOSE>>")

    elif user_action=="scissor":
        if computer_action =="paper":
            print("scissor cut paper>> <<YOU WIN>>")
        else:
            print("Rock smashed scissors>> <<YOU LOSE>>")



    play_again = input("Play again? (y/n)")
    if play_again.lower() !="y":
        break
      

            

        

     
