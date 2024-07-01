import random
if __name__ == "__main__":
    user_run = 0
    comp_run = 0
    while True:
        user_choice = input("Enter your choice Rock, Paper, Scissor or q for quit: ").lower()
        if user_choice == "q":
            break
        if user_choice not in ["rock", "paper", "scissor"]:
            print("Input valid option!")
            continue
        else:
            comp_choice = random.choice(["rock", "paper", "scissor"])
            if user_choice == "rock" and comp_choice == "paper":
                print("Computer win in this turn!")
                comp_run += 1
            elif user_choice == "rock" and comp_choice == "scissor":
                print("User win in this turn!")
                user_run += 1
            elif user_choice == "paper" and comp_choice == "rock":
                print("User win in this turn!")
                user_run += 1
            elif user_choice == "paper" and comp_choice == "scissor":
                print("Computer win in this turn!")
                comp_run += 1
            elif user_choice == "scissor" and comp_choice == "rock":
                print("Computer win in this turn!")
                comp_choice += 1
            elif user_choice == "scissor" and comp_choice == "paper":
                print("User win in this turn!")
                user_run += 1
            else:
                print("Match tie in this turn!")
    if user_run >= comp_run:
        print(f"User win:- user runs: {user_run} and computer runs: {comp_run}")
    else:
        print(f"Computer win:- user runs: {user_run} and computer runs: {comp_run}")

