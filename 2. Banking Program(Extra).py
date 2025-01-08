#banking program
def show_balance(balance):
    print(f"Your balance is ${balance:,.2f}")

def deposit():
    
    amount=float(input("Enter the deposit amount: "))
    
    if amount<0:
        print("Deposit must be greater than 0")
        return 0
    else:
        print(f"You deposited ${amount:,.2f}")
        return amount

def withdraw(balance):
    
    amount=float(input("Enter the withdraw amount: "))
    
    if amount>balance:
        print("Insufficient Funds!")
        return 0
    elif amount<0:
        print("You cannot withdraw a negative amount")
        return 0
    else:
        print(f"You withdrew ${amount:,.2f}")
        return amount
        
def main(): 

    balance=0
    is_running=True
    
    while is_running:
        print("Fadipe Bank Limited Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        
        choice=input("Enter your choice (1-4): ")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+=deposit()
        elif choice == "3":
            balance-=withdraw(balance)
        elif choice =="4":
            is_running = False
            print("Thank you for banking with us!")
        else:
            print("This is not a valid option")
            
if __name__=='__main__':
    main()
