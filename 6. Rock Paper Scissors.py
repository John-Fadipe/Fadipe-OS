#Rock Paper Scissor Game

import random

class RockPaperScissors:
    def __init__(self):
        self.user_score=0
        self.computer_score=0
        self.options=("rock","paper","scissors")

    def play_game(self):
        self.session_user_score=0
        self.session_computer_score=0

        while True:
            user_input=input("Rock, Paper, Scissors or Q to quit: ").lower()

            if user_input=="q":
                print("\nYou have exited the game")
                break
            if user_input not in self.options:
                print("\nChoose Rock, Paper or Scissors to continue\n")
                continue

            computer_input=random.choice(self.options)
            
            print()
            print(f"You chose {user_input}")
            print(f"Computer chose {computer_input}")
            print()
            
            if user_input==computer_input:
                print("It's tie!")
            elif user_input=="rock" and computer_input=="scissors":
                self.session_user_score+=1
                print("You won!")
            elif user_input=="scissors" and computer_input=="paper":
                self.session_user_score+=1
                print("You won!")
            elif user_input=="paper" and computer_input=="rock":
                self.session_user_score+=1
                print("You won!")
            else:
                self.session_computer_score+=1
                print("You lose")

        print()
        print(f"You won {self.session_user_score} times")
        print(f"Computer won {self.session_computer_score} times")

        self.user_score += self.session_user_score
        self.computer_score += self.session_computer_score

    def play_again(self):
        while True:
            replay=input("\nWould you like to play again (Y/N)? ").lower()
    
            if replay=="y":
                print("\nWelcome back to the game\n")
                self.play_game()
                continue
            elif replay=="n":
                break
            else:
                print("\nEnter Y or N to continue")
                continue

if __name__=="__main__":
    print("****************************")
    print("Welcome to the Rock, Paper, Scissors game")
    print("****************************")

    game=RockPaperScissors()
    game.play_game()
    game.play_again()

    print(f"You won the game a total of {game.user_score} times")
    print(f"The computer won the game a total of {game.computer_score} times")
    
    print("****************************")
    print("Thank you for playing!")
