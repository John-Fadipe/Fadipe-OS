import random

class PIG:
    def __init__(self):
        self.total_score=0

    def roll(self):
        roll_dice=random.randint(1,6)

    def play_game(self):
        pass

if __name__=="__main__":
    print("**** Welcome to the PIG Game ****\n")
    pig_game=PIG()
    pig_game.play_game()

    print("**** You exited the PIG Game ****\n")
