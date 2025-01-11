#Number Guessing Game
import random

class Number_Guessing_Game:
    def __init__(self):
        self.top_range=None
        self.answer=None
    
    def top_range(self):
        while True:
            top_range=input("Enter the top range number for your game: ")
            if top_range.isdigit():
                top_range=int(top_range)
                if top_range>0:
                    self.top_range=top_range
                    return
                else:
                    print("\nYou must enter a number greater than zero")
            else:
                print("\nYou can only enter numbers")
        
    def play_game(self):
        self.top_range_num=top_range()
        self.answer=random.randint(0,self.top_range_num)
        self.guess=0
        print("\nI have picked a random number, can you guess it?")
        
        while True:
            self.guess+=1
            guess_num=input("Enter your guess: ")
            if guess_num.isdigit():
                guess_num=int(guess_num)
                if guess_num==self.answer:
                    print("\nYou've guessed correct!")
                    break
                elif guess_num>self.top_range_num:
                    print("\nYour guess is out of range of guess")
                elif guess_num<self.answer:
                    print("\nYour guess is lower than the random number")
                elif guess_num>self.answer:
                    print("\nYour guess is higher than the random number")
            else:
                print("\nPlease enter a valid input")
        
        print("****************************")
        print(f"It took you {guess} attempts to guess correctly")
        print("****************************")
    
    def play_again(self):    
        while True:
            play_again=input("Would you like to play again (Y/N): ").upper()
            if play_again=="Y":
                self.play_game()
            elif play_again=="N":
                print("\nThank you for playing")
                break
            else:
                print("\nPlease enter Y or N, other inputs are invalid")
        
if __name__=="__main__":
    print("Welcome to the guessing game")
    print("****************************")
    print("Guess a number between 0 and a number of your choice")
    print()
    
    game=Number_Guessing_Game()
    game.play_game()
    game.play_again()
