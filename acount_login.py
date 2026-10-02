
def create_account():
    Uname = input("please enter a Username:  ")
    Pword = input("Please enter a Password:  ")
    print("Thank you for creating a account")
    enter_account(Uname, Pword)
        
def enter_account(Uname, Pword):
    while True:
        TUname = input("please enter your username  ")
        TPword = input("please enter your password  ")
        if TUname == Uname and TPword == Pword:
            print("Welcome to our account")
            with open("account.py", "r") as f:
                exec(f.read())
            break
        else:
            print("Try again")

                


login = input("do you have an account with us already? Y/N  ").upper()
while True:
    if login == "Y":
        enter_account()
        break
    elif login == "N":
        create_account()
        break
    else:
        print("try again")
        
                
                
            
        
        
