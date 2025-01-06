#Python Quiz Game
print("*************************")
print("Welcome to a Computer Quiz Game")
print("*************************")

def questions():

    score=0
    question_1 = input("1. What does CPU stand for? ").lower()
    if question_1 == "central processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        
    print("*************************")
    question_2 = input("2. What does GPU stand for?").lower()
    if question_2 == "graphics processing unit":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

    print("*************************")
    question_3 = input("3. What does UPS stand for?").lower()
    if question_3 == " uninterruptible power supply":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        
    print("*************************")
    question_4 = input("4. What does RAM stand for?").lower()
    if question_4 == "random access memory":
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")

    print("*************************")
    print(f"You scored: {score}")
    print()
    print("Thank you for playing!")

def main():

    is_running=True
    
    while is_running:
        prompt_1=input("Would you like to play a game(Y/N): ").upper()
        if prompt_1 == "N":
            print("\nThank you, maybe next time!")
            is_running=False
        elif prompt_1 == "Y":
            print("\nWelcome to the game!")
            questions()
            
            replay=input("Would you like to play a game(Y/N): ").upper()
            if replay == "N":
                print("\nThank you, existing the game")
                is_running=False
            elif replay == "Y":
                print("\nRestarting the game...\n")
            else:
                print("\nPlease enter a valid Y or N\n")
            
        else:
            print("\nPlease enter a valid Y or N")

if __name__=="__main__":
    main()