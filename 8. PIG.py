import random

class PIG:
    def __init__(self):
        self.total_score=0

    def roll(self):
        self.roll_dice=random.randint(1,6)
        print(f"\nYou rolled a {self.roll_dice}")

    def select_player(self):
        while True:
            player=input("Enter the number of players: ")
            if player.isdigit():
                player=int(player)
                if player>=2 and player<=4:
                    break
                elif player<2 or player>4:
                    print("\nNumber of players can only be 2-4")
                else:
                    print("\nEnter a valid input")

    def play_game(self):
        self.select_player()

        while True:
            current_score=0
            do_roll=input("Would you like to roll(Y)? ").upper()
            if do_roll!="Y":
                break
            else:
                self.roll()
                if self.roll()==1:
                    current_score=0
                    print(f"You rolled {self.roll()}. Turn done!\n")
                    break

                else:
                    current_score+=1
                

if __name__=="__main__":
    print("**** Welcome to the PIG Game ****\n")
    pig_game=PIG()
    pig_game.play_game()

    print("\n**** You exited the PIG Game ****")
