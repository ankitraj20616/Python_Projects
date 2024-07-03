from random import randint

class PIG_Game:
    def roll(self)->int:
        return randint(1, 6)

    def main(self)-> None:
        while True:
            players = input("Enter numbers of players (2-4): ")
            if players.isdigit():
                players = int(players)
                if players >= 2 and players <= 4:
                    break
                else:
                    print("Please enter numbers of players in valid range!")
            else:
                print("Please enter a digit!")
        
        max_score = 50
        players_score = [0 for _ in range(players)]
        while max(players_score) < 50:
            for player_idx in range(players):
                print(f"\nStarting turn of {player_idx + 1} player.\n")
                current_score = 0
                while True:
                    print(f"Your current score is {current_score}.")
                    status = input("Would you like to role again? (y for yes): ").lower()
                    if status != 'y':
                        break
                    value = self.roll()
                    if value == 1:
                        print("OOPS! You got 1 in this roll.")
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print(f"In this roll player {player_idx + 1} got {value} value.")
                players_score[player_idx] = current_score
                print(f"{player_idx} player your total score is {players_score[player_idx]}.")
        
        winner_score = max(players_score)
        winner_idx = players_score.index(winner_score)   

        print(f"Finally! {winner_idx} player wins with score {winner_score}.")

                    
            

if __name__ == "__main__":
    game = PIG_Game()
    game.main()