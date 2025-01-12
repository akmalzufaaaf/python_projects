import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to RPS 9000!")

        self.moves: dict = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self.valid_move: list[str] = list(self.moves.keys())
        self.points: dict = {'user': 0, 'ai' : 0}
        
    def play_game(self):
        user_move: str = input("Rock, paper, or scissors? >> ").lower()

        if user_move.lower() == "exit":
            print("Thanks for playing!")
            sys.exit()
        
        if user_move not in self.valid_move:
            print("Invalid move...")
            self.play_game()
            
        ai_move: str = random.choice(self.valid_move)
        
        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)
    
    def display_move(self, user_move: str, ai_move: str):
        print("------")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print("------")
    
    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It\'s a tie!")
            print("------")
            print(f"You : AI")
            print(f"{self.points['user']} : {self.points['ai']}")
            print("------")
        elif user_move == 'rock' and ai_move == 'scissors':
            print("You win!")
            self.point('user')
        elif user_move == 'paper' and ai_move == 'rock':
            print("You win!") 
            self.point('user')
        elif user_move == 'scissors' and ai_move == 'paper':
            print("You win!") 
            self.point('user')
        else:
            print("You lose")
            print("AI win...")
            self.point('ai')
    
    def point(self, winner: str):
        self.points[winner] += 1
        print(f"{self.points['user']} : {self.points['ai']}")
        print("------")
        
if __name__ == '__main__':
    rps = RPS()
    while True:
        rps.play_game()

        