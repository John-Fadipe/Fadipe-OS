# Password Manager
import os

class PasswordManager:
    def __init__(self):
        self.file_path = "Linked File/password.txt"
        self.master_pwd = None
        self.credentials = {}

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                if lines:
                    self.master_pwd = lines[0].strip().split(": ")[1]
                    for line in lines[1:]:
                        username, password = line.strip().split(" | ")
                        self.credentials[username] = password

    def master_password(self):
        if self.master_pwd is None:
            master_pwd = input("\nSet your master password: ")
            self.master_pwd = master_pwd
            with open(self.file_path, "w") as file:
                file.write(f"master password: {self.master_pwd}\n")
            print("\nMaster password was successfully created")
        else:
            print("\nMaster password already exists")
    
    def validate_master_password(self):
        entered_pwd = input("Enter your master password to proceed: ")
        return entered_pwd == self.master_pwd

    def add_password(self):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        self.credentials[username] = password
        
        with open(self.file_path, "a") as file:
            file.write(f"{username} | {password}\n")
        print("\nPassword was successfully added\n") 

    def view_password(self):
        if not self.validate_master_password():
            print("\nWrong master password, access denied")
            return
        print("\nFind your saved passwords below:")
        for username, password in self.credentials.items():
            print(f"Username: {username}, Password: {password}")
                
    def run(self):
        while True:
            print("\nSelect your options (1, 2, 3, or 4):\n")
            print("1. Set the master password (First set-up)")
            print("2. Add a new password")
            print("3. View existing passwords")
            print("4. Exit\n")

            selection = input("Enter your option: ").strip()
            if selection.isdigit():
                selection = int(selection)
            
            if selection == 1:
                print("\nSetting master password...\n")
                self.master_password()
            elif selection == 2:
                if self.master_pwd is None:
                    print("\nYou need to set a master password first")
                else:
                    print("\nAdding a new password...\n")
                    self.add_password()
            elif selection == 3:
                if self.master_pwd is None:
                    print("\nYou need to set a master password first")
                else:
                    print("\nViewing existing passwords...\n")
                    self.view_password()
            elif selection == 4:
                print("\nExiting the password manager...\n")
                break
            else:
                print("\nInvalid option\n")
                continue

if __name__ == "__main__":
    print("**** Welcome to your password manager ****\n")

    pwd = PasswordManager()
    pwd.run()

    print("\n**** You exited the password manager ****")
