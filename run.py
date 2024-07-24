from colorama import Fore, Back, Style  # import colors sheme

def main():
    """
    Main function that starts the test/risk calculator
    """

print(Fore.YELLOW + "\nWelcome to our program that helps to find out your risk of type 2 diabetes in the next 10 years.")
print("To calculate your risk we will ask you for some data related to your health.") 
print("This program doesn't save or transfer any data you provided so anyone cannot identify you.\n" + Style.RESET_ALL)

print("When you pass through our test you'll find out that potential risk level for developing diabetes in the next 10 years of life is (depending on points earned):\n")
    
print(Fore.GREEN + "Less than 7 points" + Style.RESET_ALL + ": Low risk")
print(Fore.YELLOW + "7 - 11 points" + Style.RESET_ALL + ": Slight risk")
print(Fore.CYAN + "12 - 14 points" + Style.RESET_ALL + ": Average risk")
print(Fore.MAGENTA + "15 - 20 points" + Style.RESET_ALL + ": High risk")
print(Fore.RED + "More than 20 points" + Style.RESET_ALL + ": Very high risk\n")
    
while True:
    try:
        start = input("Let's get started? (Y/N): \n").upper()
        if start == "Y":
            main()
            print("Start")
            break
        elif start == "N":
            print("No Start")
            break
        else:
            raise ValueError(Fore.RED + ("Please choose Y or N!"))
    except ValueError as e_rr:
            print(f"Invalid input: {e_rr}")