import time
import logging
from colorama import Fore, Style
def quit():
    print(Fore.LIGHTGREEN_EX + f"GoodBye!!" + Style.RESET_ALL)
    time.sleep(0.6)
    return 0
def register(username,password):
    status = 0
    try:
        with open("username.txt", "r") as file:
            
            for line in file:
                clear_line = line.strip()
                if f"{username}" == clear_line:
                    status = 1
            if status == 1:
                print(Fore.RED + f"{username} already exist" + Style.RESET_ALL)
            elif status == 0:
                with open("username.txt", "a") as file:
                    file.write(username)
                    file.write("\n")
                    file.close()
                with open("password.txt", "a") as file:
                    file.write(f"{username}:{password}")
                    file.write("\n")
                    print(Fore.GREEN + f"{username} successfully registered" + Style.RESET_ALL)
                    file.close()
    except FileNotFoundError:
        open("username.txt", "x")
        open("password.txt", "x")
        time.sleep(0.5)
        print("File created successfully")
    except:
        print("Error")
def login(username,password):
    status = 0

    try:
        with open("username.txt", "r") as file:
           
            for line in file:
                clear_line = line.strip()
                if f"{username}" == clear_line:
                    status = 1

            if status == 1:
                with open("password.txt", "r") as file:
                    pass_status = 0
                    for line in file:
                        clear_pass_line = line.strip()
                        if f"{username}:{password}" == clear_pass_line:
                            pass_status = 1
                    if pass_status == 1:
                        print(Fore.GREEN + f"{username} has been successfully logged in\n=======WELCOME============\n" + Style.RESET_ALL)
                    elif pass_status == 0:
                       print(Fore.RED + "Incorrect Password" + Style.RESET_ALL) 

            elif status == 0:
                print(Fore.RED + f"{username} not found" + Style.RESET_ALL)
                


    except FileNotFoundError:
        open("cred.txt", "x")
        time.sleep(0.5)
        print("File created successfully")
    except:
        logging.exception(Fore.RED + "ERRR" + Style.RESET_ALL)

print("========logging and Register System==========\n1.Logging\n2.Register\n3.Quit")


try:
    user_input = int(input("Enter your Choice(1,2,3): "))
    if user_input >=4 or user_input <= 0:
        print("Error")
        time.sleep(0.5)
    elif user_input == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        login(username,password)
    elif user_input == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register(username,password)
    elif user_input == 3:
        quit()
    else:
        print("Error")
except ValueError:
    print("Please choose between 1 or 2")
        
        

