import random

class PIG:
    def __init__(self):
        self.max_score = 50
        self.player_scores = []

    def roll(self):
        return random.randint(1, 6)

    def select_player(self):        
        while True:
            player = input("\nEnter the number of players: ")
            if player.isdigit():
                player = int(player)
                if 2 <= player <= 4:
                    return player
                else:
                    print("\nNumber of players can only be 2-4")
            else:
                print("\nEnter a valid input")

    def play_game(self):
        num_players = self.select_player()
        self.player_scores = [0] * num_players

        while max(self.player_scores) < self.max_score:
            for player_idx in range(num_players):
                self.current_score = 0
                print(f"\nPlayer {player_idx+1}'s Turn (Current Score: {self.player_scores[player_idx]})")
                
                while True:
                    do_roll = input("\nWould you like to roll (Y)? ").upper()
                    if do_roll != "Y":
                        break
                    else:
                        rolled_value = self.roll()
                        print(f"\nYou rolled a {rolled_value}")

                        if rolled_value == 1:
                            self.current_score = 0
                            print("You rolled 1. Turn done!\n")
                            break
                        else:
                            self.current_score += rolled_value

                self.player_scores[player_idx] += self.current_score
                print(f"Player {player_idx+1} total score is: {self.player_scores[player_idx]}")

                if self.player_scores[player_idx] >= self.max_score:
                    print(f"\nPlayer {player_idx+1} wins with {self.player_scores[player_idx]} points!")
                    return

    def play_again(self):
        while True:
            play_again = input("\nWould you like to play again (Y/N)? ").upper()
            if play_again != "Y":
                print("\nYou're exiting the game...\n")
                break
            else:
                print("\nReloading the game...")
                self.play_game()

if __name__ == "__main__":
    print("**** Welcome to the PIG Game ****\n")
    pig_game = PIG()
    pig_game.play_game()
    pig_game.play_again()
    print("\n**** You exited the PIG Game ****")
