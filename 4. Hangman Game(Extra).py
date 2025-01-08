#Hangman Game
import random

words=("pyramid","lantern","thunder","journey","fortune","crystal","meadow","canyon","griffin","fiction")

hangman_art={0:("  ",
                "  ",
                "  "),
            1:(" o ",
               "   ",
               "   "),
            2:(" o ",
               " | ",
               "   "),
            3:(" o ",
               "/| ",
               "   "),
            4:(" o ",
               "/|\\",
               "   "),
            5:(" o ",
               "/|\\",
               "/  "),
            6:(" o ",
               "/|\\",
               "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
        
def display_hint(hint):
    print(" ".join(hint))
    
def display_answer(answer):
    print(" ".join(answer))
    
def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running:
        print("*************")
        display_man(wrong_guesses)
        print("*************")
        display_hint(hint)
        guess=input("Guess a letter from the hint: ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid guess!")
            continue
        if guess in guessed_letters:
            print(f"You already guessed {guess}")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for index in range(len(answer)):
                if answer[index]==guess:
                    hint[index]=guess
        else:
            wrong_guesses+=1
        if "_" not in hint:
            print("You Win!")
            print("*************")
            display_answer(answer)
            is_running=False
        elif wrong_guesses == len(hangman_art)-1:
            print("You Lose!")
            print("*************")
            display_answer(answer)
            is_running=False
            
    while True:
        play_again = input("Would you like to play again (Y/N): ").upper()
        if play_again == "Y":
            main()
            break
        elif play_again == "N":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

if __name__=="__main__":
    main()
