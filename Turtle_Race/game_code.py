import turtle 
import time
import random

class Game:
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 500, 500
        self.COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

    def init_turtle(self)->None:
        screen = turtle.Screen()
        screen.setup(self.WIDTH, self.HEIGHT)
        screen.title("Turtle Race")

    def get_number_of_racers(self)->int:
        racers = 0
        while True:
            racers = input("Enter number of racers between (2 - 10):- ")
            if racers.isdigit():
                racers = int(racers)
                if 2 <= racers <= 10 :
                    break
                else:
                    print("Please Enter number between 2 to 10.")
            else:
                print("Please Enter a number!")
        return racers
    
    def create_turtle(self, colors):
        turtles = []
        spacing = self.WIDTH // (len(colors)+1)
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-self.WIDTH//2 + (i + 1) * spacing, -self.HEIGHT//2 + 20)
            racer.pendown()
            turtles.append(racer)
        
        return turtles
   
    def race(self, colors):
        turtles = self.create_turtle(colors)

        while True:
            for racer in turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= self.HEIGHT//2 - 10:
                    time.sleep(1)
                    return colors[turtles.index(racer)]

    def main(self)->None:
        num_of_racer = self.get_number_of_racers()
        self.init_turtle()

        random.shuffle(self.COLORS)
        colors = self.COLORS[:num_of_racer]

        winner = self.race(colors)
        print(f"Our winner is {winner} turtle.")





        # racer = turtle.Turtle()
        # racer.speed(1)
        # racer.penup()
        # racer.shape('turtle')
        # racer.color('red')
        # racer.forward(100)
        # racer.left(60)
        # racer.pendown()
        # racer.right(90)
        # racer.backward(90)
        
        # time.sleep(5)
        

        

        

if __name__ == "__main__":
    game = Game()
    game.main()

    
    
    