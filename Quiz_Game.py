if __name__ == "__main__":
    print("Welcome to quiz game!")
    play = input("Do you want to play Quiz Game? ")
    if play.lower() != "yes":
        print("Fine! Don't play")
        quit()
    print("Okay! Let's Play")
    score = 0
    answer = input("Enter full form of cpu? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    answer = input("Enter extension of python file? ")
    if answer == ".py":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    answer = input("Enter extension of java file? ")
    if answer == ".java":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"Your final score is :- {round((score / 3) * 100, 2)}%")
    
