from colorama import Fore, Back, Style   # import colors sheme
from simple_term_menu import TerminalMenu  # import Simple Terminal Menu
import sys  # import sys library for correct exit from program
from os import system  # import system functions for cleaning terminal


def main():
    """
    Main function that starts the test/risk calculator
    """
    introduction()
    menu_start()
    gender_menu()
    print("To be continued...")
    # gender = get_gender()
    # weight = get_weight()
    # sport = get_sport()


def introduction():
    """Introduction function"""
    print(f"""{Fore.YELLOW}
          Welcome to our program that helps to find out your risk of 
                    type 2 diabetes in the next 10 years""")
    print(f"""
  To calculate your risk we will ask you for some data related to your health.
  This program doesn't save or transfer any data you provided so anyone cannot 
  identify you. You are in safe place.{Style.RESET_ALL}""")
    print(f"""
  When you pass through our test you'll find out that potential risk level for 
  developing diabetes in the next 10 years of life depending on points earned:
    """)    
    print(Fore.GREEN + "Less than 7 points" + Style.RESET_ALL + ":  Low risk")
    print(Fore.YELLOW + "7 - 11 points" + Style.RESET_ALL + ":       Slight risk")
    print(Fore.CYAN + "12 - 14 points" + Style.RESET_ALL + ":      Average risk")
    print(Fore.MAGENTA + "15 - 20 points" + Style.RESET_ALL + ":      High risk")
    print(Fore.RED + "More than 20 points" + Style.RESET_ALL + ": Very high risk\n")


def menu_start():
    while True:
        try:
            start = input("Let's get started? " + Fore.BLUE + "(Y/N): " +
                    Style.RESET_ALL).upper()
            if start == "Y":
                system("clear")
                break
            elif start == "N":
                print("")
                sys.exit("Thank you for attention. Goodbye!")
            else:
                raise ValueError(Fore.RED + ("Please choose Y or N") +
                    Style.RESET_ALL)
        except ValueError as err:
            print(f"Invalid input: {err}")


def gender_menu():
    options = ["Male", "Female"]
    terminal_menu = TerminalMenu(options, title="Choose your gender")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")


main()