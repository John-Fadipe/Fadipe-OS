import random

class PIG:
    def __init__(self):
        self.total_score=0

    def roll(self):
        self.roll_dice=random.randint(1,6)
        return self.roll_dice

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
        self.max_score=50
        self.current_score=0

        while self.max_score<self.current_score:
            do_roll=input("Would you like to roll(Y)? ").upper()
            if do_roll!="Y":
                break
            else:
                rolled_value=self.roll()
                if rolled_value==1:
                    self.current_score=0
                    print(f"You rolled a {rolled_value}. Turn done!\n")
                    break

                else:
                    print(f"\nYou rolled a {rolled_value}")
                    self.current_score+=rolled_value

        self.total_score+=self.current_score

        print(f"Your total score is: {self.total_score}")
        
    def play_again(self):
        pass

if __name__=="__main__":
    print("**** Welcome to the PIG Game ****\n")
    pig_game=PIG()
    pig_game.play_game()
    pig_game.play_again()

    print("\n**** You exited the PIG Game ****")
