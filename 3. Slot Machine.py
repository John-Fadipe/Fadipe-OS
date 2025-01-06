#Python Slot Machine
import random

def spin_row():
    symbols=["🍒"," 🍉","🍋","🔔","⭐"]
    return [random.choice(symbols) for _ in range(3)]   
#Alternatively to list comprehension
#    results=[]
#    for symbol in range(3):
#       results.append(random.choice(symbols))
#    return results

def print_row(row):
    print(" | ".join(row))
    
def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*2
        elif row[0]=="🍉":
            return bet*5
        elif row[0]=="🍋":
            return bet*10
        elif row[0]=="🔔":
            return bet*20
        elif row[0]=="⭐":
            return bet*50
    return 0
    
def main():
    balance=100
    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")
    
    while balance>0:
        bet=input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Enter a valid bet amount")
            continue
        bet=int(bet)
        if bet>balance:
            print("Insufficient Funds!")
            continue
        if bet<=0:
            print("Enter a bet amount greater than 0")
            continue
            
        balance-=bet
        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=get_payout(row, bet)
        balance+=payout
        
        if payout > 0:
            print(f"Congratulations! You won ${payout}")
        else:
            print("Better luck next time!")
        print(f"Your available bet is ${balance}")
        print("*************************")
        
        if balance == 0:
            print("You have no more funds to play.")
            break
        replay=input("Would you like to play again(Y/N): ").upper()
        if replay!="Y":
            break
            
    print("*************************")
    print(f"Thank you for playing. Your final balance is ${balance}")

if __name__=="__main__":
    main()