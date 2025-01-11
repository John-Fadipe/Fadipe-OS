#Password Manager
class PasswordManager:
    def __init__(self):
        self.master_pwd=None

    def master(self):
        pass
#        self.master_pwd=input("Enter your master password: ")

    def view_pass(self):
        pass

    def add_pass(self):
        pass
#       with open ("password.txt","a") as file:
#            file.write(f"{self.username} | {self.password}")

    def running(self):
#        self.username=input("Enter your usename: ")
#        self.password=input("Enter your password: ")

        self.selection=input("1. View\n2. Add\n3. Exit ")

        while True:
            if self.selection=="view":
                view_pass()
            elif self.selection=="add":
                add_pass()
            else:
                print("Invalid selection")

if __name__=="__main__":
    print("**** Welcome to your password manager ****\n")

    pwd=PasswordManager()
    pwd.running()