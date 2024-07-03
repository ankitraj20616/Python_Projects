import random
import time

class timedMathChallenges:
    def expression_generator(self):
        min_operand = 3
        max_operand = 12
        operator = ['+', '-', '*', '//']

        expression = str(random.randint(min_operand, max_operand))+str(random.choice(operator))+str(random.randint(min_operand, max_operand))

        answer = eval(expression)

        return expression, answer

    def main(self)-> None:
        
        while True:
            problem = input("Enter numbers of problems you want to solve:- ")
            if problem.isdigit():
                problem = int(problem)
                break
            else:
                print("Please enter integer value!")
                continue

        input("Enter any key to start challenge: ")
        print("-----------------------------------")
        start_time = time.time()
        for i in range(problem):
            exp, ans = self.expression_generator()
            while True:
                user_ans = input(f"Enter solution for {exp}: ")
                if user_ans == str(ans):
                    break
        end_time = time.time()
        print("------------------------------------")
        print(f"You solved {problem} problems in {round(end_time - start_time, 2)} seconds!")

        


if __name__ == "__main__":
    maths = timedMathChallenges()
    maths.main()