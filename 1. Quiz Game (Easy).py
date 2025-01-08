#Python Quiz Game

class Quiz_Game:
    def __init__(self):
        self.score=0
        
    def questions(self):
        self.score=0
        self.question_1 = input("1. What does CPU stand for? ").lower()
        if self.question_1 == "central processing unit":
            print("Correct!")
            self.score+=1
        else:
            print("Incorrect!")
            
        print("*************************")
        self.question_2 = input("2. What does GPU stand for?").lower()
        if self.question_2 == "graphics processing unit":
            print("Correct!")
            self.score+=1
        else:
            print("Incorrect!")
    
        print("*************************")
        self.question_3 = input("3. What does UPS stand for?").lower()
        if self.question_3 == "uninterruptible power supply":
            print("Correct!")
            self.score+=1
        else:
            print("Incorrect!")
            
        print("*************************")
        self.question_4 = input("4. What does RAM stand for?").lower()
        if self.question_4 == "random access memory":
            print("Correct!")
            self.score+=1
        else:
            print("Incorrect!")
    
        print("*************************")
        print(f"You scored: {self.score}")
        print()
        print("Thank you for playing!")
    
    def play_game(self): 
        self.is_running=True
        while self.is_running:
            play=input("Would you like to play a game(Y/N): ").upper()
            if play == "N":
                print("\nThank you, maybe next time!")
                self.is_running=False
            elif play == "Y":
                print("\nWelcome to the game!")
                self.questions()

                while True:
                    replay=input("Would you like to play again(Y/N): ").upper()
                    if replay == "N":
                        print("\nThank you, exiting the game")
                        self.is_running=False
                        break
                    elif replay == "Y":
                        print("\nRestarting the game...\n")
                        self.questions()
                    else:
                        print("\nPlease enter Y or N\n")
            
            else:
                print("\nPlease enter Y or N")

if __name__=="__main__":
    print("*************************")
    print("Welcome to a Computer Quiz Game")
    print("*************************")

    game=Quiz_Game()
    game.play_game()
