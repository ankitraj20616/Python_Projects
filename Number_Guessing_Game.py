from random import randint
if __name__ == "__main__":
    top_of_range = input("Enter a number(max range of guess) :- ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Input number greater then 0 next time")
            quit()
    else:
        print("Input a digit next time")
        quit()
    
    random_num = randint(0, top_of_range)
    count = 0
    while True:
        your_guess = input("Enter your guess number:- ")
        count += 1
        if your_guess.isdigit():
            your_guess = int(your_guess)
            if your_guess < 0:
                print("Guess number greater then or equal to 0 next time")
                continue
            if your_guess == random_num:
                print("You guessed corretly!")
                print(f"You guessed correctly in {count}'th times!")
                break
            elif your_guess < random_num:
                print("Guess some larger value")
            else:
                print("Guess some smaller value")
        else:
            print("Guess a digit next time")