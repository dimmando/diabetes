from colorama import Fore, Back, Style  # import colors sheme
from simple_term_menu import TerminalMenu  # import Simple Terminal Menu
import sys  # import sys library for correct exit from program
from os import system  # import system functions for cleaning terminal


def main():
    """
    Main function that starts the test/risk calculator
    """
    introduction()
    menu_start()
    age = get_age()
    gender = get_gender()
    if gender == "Male":
        waist = get_waist_male()
    else:
        waist = get_waist_female()
    print(waist)

    print("To be continued...")
    # gender = get_gender()
    # weight = get_weight()
    # sport = get_sport()


def introduction():
    """Introduction function"""
    print(
        f"""{Fore.YELLOW}
          Welcome to our program that helps to find out your risk of 
                    type 2 diabetes in the next 10 years"""
    )
    print(
        f"""
  To calculate your risk we will ask you for some data related to your health.
  This program doesn't save or transfer any data you provided so anyone cannot 
  identify you. You are in safe place.{Style.RESET_ALL}"""
    )
    print(
        f"""
  When you pass through our test you'll find out that potential risk level for 
  developing diabetes in the next 10 years of life depending on points earned:
    """
    )
    print(Fore.GREEN + "Less than 7 points" + Style.RESET_ALL + ":  Low risk")
    print(
        Fore.YELLOW + "7 - 11 points" + Style.RESET_ALL + ":       Slight risk"
    )
    print(
        Fore.CYAN + "12 - 14 points" + Style.RESET_ALL + ":      Average risk"
    )
    print(
        Fore.MAGENTA + "15 - 20 points" + Style.RESET_ALL + ":      High risk"
    )
    print(
        Fore.RED
        + "More than 20 points"
        + Style.RESET_ALL
        + ": Very high risk\n"
    )


def menu_start():
    while True:
        try:
            start = input(
                "Let's get started? " + Fore.BLUE + "(Y/N): " + Style.RESET_ALL
            ).upper()
            if start == "Y":
                system("clear")
                break
            elif start == "N":
                print("")
                sys.exit("Thank you for attention. Goodbye!")
            else:
                raise ValueError(
                    Fore.RED + ("Please choose Y or N") + Style.RESET_ALL
                )
        except ValueError as err:
            print(f"Invalid input: {err}")


def get_age():
    options = ["Under 45 years old", "45 - 54 years old", "55 - 64 years old",
    "Over 65 years old"]
    terminal_menu = TerminalMenu(options, title="How old are you?")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected your age: {Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}")
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 2
    elif menu_entry_index == 2:
        points = 3
    elif menu_entry_index == 3:
        points = 4
    
    print(points)

    return points


def get_gender():
    options = ["Male", "Female"]
    terminal_menu = TerminalMenu(options, title="Choose your gender:")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected your gender: {Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}")
    print("")

    if menu_entry_index == 0:
        return "Male"
    else:
        return "Female"


def get_waist_male():
    options = ["Less than 94 cm", "94 - 102 cm", "More than 102 cm"]
    terminal_menu = TerminalMenu(options, title="What is your waist measurement?\n(Hint: measure between your bottom rib and the top of your hip bone)")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected your waist: {Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}")
    print("")
    
    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 3
    elif menu_entry_index == 2:
        points = 4
        
    print(points)

    return points


def get_waist_female():
    options = ["Less than 80 cm", "80 - 88 cm", "More than 88 cm"]
    terminal_menu = TerminalMenu(options, title="What is your waist measurement?\n(Hint: measure between your bottom rib and the top of your hip bone)")
    menu_entry_index = terminal_menu.show()
    print(f"You have selected your waist: {Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}")
    print("")
    
    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 3
    elif menu_entry_index == 2:
        points = 4
        
    print(points)

    return points

main()
