from colorama import Fore,Style
def add(a,b):
    sum = a + b
    print(Fore.GREEN + f"Your sum is {sum}" + Style.RESET_ALL)
    

a = int(input("Enter your first number: "))
b = int(input("Enter your Second number: "))
add(a,b)

