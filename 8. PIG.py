import random

class PIG:
    def __init__(self):
        self.total_score=0

    def roll(self):
        self.roll_dice=random.randint(1,6)
        print(f"\nYou rolled a {roll_dice}\n")

    def play_game(self):
        while True:
            player=input("Enter the number of players: ")
            if player.isdigit():
                player=int(player)
                if player>=2 and player<=4:
                    break
                elif player<2 or player>4:
                    print("Number of players can only be 2-4")
                else:
                    print("Enter a valid input")

            
if __name__=="__main__":
    print("**** Welcome to the PIG Game ****\n")
    pig_game=PIG()
    pig_game.play_game()

    print("\n**** You exited the PIG Game ****")
