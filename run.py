import sys  # import sys library for correct exit from program
from os import system  # import system functions for cleaning terminal
from colorama import Fore, Back, Style  # import colors sheme
from simple_term_menu import TerminalMenu  # import Simple Terminal Menu
from introduction import *  # import introduction() function from separate file


def main():
    """
    Main function that starts test (risk) calculator that helps to find out
    your risk of type 2 diabetes in the next 10 years
    """

    while True:
        system("clear")
        introduction()
        menu_start()
        age = get_age()
        gender = get_gender()

        if gender == "Male":
            waist = get_waist_male()
        else:
            waist = get_waist_female()

        bmi = body_mass_index()
        fruits = get_fruits()
        exercises = get_exercises()
        medication = get_medication()
        sugar_level = get_sugar_level()
        relatives = get_relatives()

        total = (
            age
            + waist
            + bmi
            + fruits
            + exercises
            + medication
            + sugar_level
            + relatives
        )

        conclusion(total)
        print("")
        test_again()


def menu_start():
    """The function that provides choice for user to start test or not"""

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
    """Getting age range points"""

    options = [
        "Under 45 years old",
        "45 - 54 years old",
        "55 - 64 years old",
        "Over 65 years old",
    ]
    terminal_menu = TerminalMenu(options, title="How old are you?")
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected your age:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 2
    elif menu_entry_index == 2:
        points = 3
    elif menu_entry_index == 3:
        points = 4

    return points


def get_gender():
    """Getting gender"""

    options = ["Male", "Female"]
    terminal_menu = TerminalMenu(options, title="Choose your gender:")
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected your gender:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        return "Male"
    else:
        return "Female"


def get_waist_male():
    """Getting waist points if Male"""

    options = ["Less than 94 cm", "94 - 102 cm", "More than 102 cm"]
    terminal_menu = TerminalMenu(
        options,
        title="What is your waist measurement?\n" +
        "(Hint: measure between your bottom rib and the top of your hip bone)"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected your waist:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 3
    elif menu_entry_index == 2:
        points = 4

    return points


def get_waist_female():
    """Getting waist points if Female"""

    options = ["Less than 80 cm", "80 - 88 cm", "More than 88 cm"]
    terminal_menu = TerminalMenu(
        options,
        title="What is your waist measurement?\n" +
        "(Hint: measure between your lowest rib and the top of your hip bone)"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected your waist:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 3
    elif menu_entry_index == 2:
        points = 4

    return points


def body_mass_index():
    """
    Getting height, weight and calculating BMI.
    Getting points depending on BMI.
    """

    while True:
        try:
            height = input(
                "How tall are you in centimeters? "
                + Fore.BLUE
                + "(For example 176): "
                + Style.RESET_ALL
            )
            if height.isnumeric() and int(height) > 130 and int(height) < 220:
                break
            else:
                raise ValueError(
                    Fore.RED
                    + ("Please enter your real height in centimeters")
                    + Style.RESET_ALL
                )
        except ValueError as err:
            print(f"Invalid input: {err}")
            print("")

    print("")

    while True:
        try:
            weight = input(
                "How much do you weight in kilograms? "
                + Fore.BLUE
                + "(For example 83): "
                + Style.RESET_ALL
            )
            if weight.isnumeric() and int(weight) > 30 and int(weight) < 200:
                break
            else:
                raise ValueError(
                    Fore.RED
                    + ("Please enter your real weight in kilograms")
                    + Style.RESET_ALL
                )
        except ValueError as err:
            print(f"Invalid input: {err}")
            print("")

    get_bmi = round(float(weight) / (float(height) / 100) ** 2)

    print("")
    print(
        "Your Body Mass Index (BMI) is: "
        + Fore.YELLOW
        + str(get_bmi)
        + Style.RESET_ALL
    )
    print(
        f"{Fore.CYAN}{Style.DIM}",
        f"BMI is a simple way to check if your weight is healthy for your",
        f"height.\n",
        f"Why does this matter?\n",
        f"Being overweight or obese increases your risk of type 2 diabetes.\n",
        f"{Style.RESET_ALL}"
    )

    if get_bmi < 25:
        points = 0
        print(f"{Fore.GREEN}Your BMI is very good{Style.RESET_ALL}\n")

    elif get_bmi <= 30:
        points = 1
        print(f"{Fore.MAGENTA}Your BMI is average{Style.RESET_ALL}\n")

    elif get_bmi > 30:
        points = 3
        print(f"{Fore.RED}Your BMI is bad{Style.RESET_ALL}\n")

    return points


def get_fruits():
    """Getting points depending on eating fruits"""

    options = ["Every day", "Not every day"]
    terminal_menu = TerminalMenu(
        options, title="How often do you eat vegetables, fruits or berries?"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected you eat vegetables, fruits or berries:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 1

    return points


def get_exercises():
    """Getting points depending on making physical exercises"""

    options = ["YES", "NO"]
    terminal_menu = TerminalMenu(
        options,
        title="Do you do physical exercises?\n" +
        "(including walking for 30 minutes every day," +
        "at least 3 hours during the week)"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected you do physical exercises:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 2

    return points


def get_medication():
    """Getting points depending on taking medications"""

    options = ["NO", "YES"]
    terminal_menu = TerminalMenu(
        options,
        title="Have you ever taken medication to lower your blood pressure?"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected you took medication to lower your blood pressure:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 2

    return points


def get_sugar_level():
    """Get points depending on previously detected high blood sugar level"""

    options = ["NO", "YES"]
    terminal_menu = TerminalMenu(
        options,
        title="Have you ever had high blood sugar level?\n" +
        "(during check-ups, illness or pregnancy)"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected you had high blood sugar level:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 0
    elif menu_entry_index == 1:
        points = 5

    return points


def get_relatives():
    """Getting points depending on diabetes detected on relatives"""

    options = [
        "Yes. Parents, brother/sister, children",
        "Yes. Grandparents, aunts/uncles, cousins",
        "NO",
    ]
    terminal_menu = TerminalMenu(
        options,
        title="Did any of your relatives have type 1 or type 2 diabetes?"
    )
    menu_entry_index = terminal_menu.show()
    print(
        f"You have selected your relatives had type 1 or type 2 diabetes:",
        f"{Fore.YELLOW}{options[menu_entry_index]}{Style.RESET_ALL}"
    )
    print("")

    if menu_entry_index == 0:
        points = 5
    elif menu_entry_index == 1:
        points = 2
    elif menu_entry_index == 2:
        points = 0

    return points


def conclusion(score):
    """Conclusion function that provides result depending on points earned"""

    print("CONCLUSION:")

    if score < 12:
        print(
            f"{Back.GREEN}",
            f"You earned less than 12 points",
            f"{Style.RESET_ALL}",
            f"{Fore.GREEN}",
            f"\nYou are in good health and should continue to live a healthy",
            f"lifestyle.",
            f"{Style.RESET_ALL}",
        )

    elif score <= 14:
        print(
            f"{Back.CYAN}",
            f"You earned 12 - 14 points",
            f"{Style.RESET_ALL}",
            f"{Fore.CYAN}",
            f"\nYou may have prediabetes. You should check your blood sugar",
            f"level.",
            f"\nYou should ask your doctor about lifestyle changes.",
            f"{Style.RESET_ALL}",
        )

    elif score <= 20:
        print(
            f"{Back.MAGENTA}",
            f"You earned 15 - 20 points",
            f"{Style.RESET_ALL}",
            f"{Fore.MAGENTA}",
            f"\nYou may have prediabetes or type 2 diabetes.",
            f"You should check your blood sugar level.",
            f"You should see an endocrinologist, change your lifestyle;",
            f"you may need medication to control your blood sugar level.",
            f"{Style.RESET_ALL}",
        )

    elif score > 20:
        print(
            f"{Back.RED}",
            f"You earned more than 20 points",
            f"{Style.RESET_ALL}",
            f"{Fore.RED}",
            f"\nYou most likely have type 2 diabetes.",
            f"\nYou should check and control your blood sugar level,",
            f"see an endocrinologist.",
            f"\nYou should change your lifestyle; ",
            f"you may also need medication to control your blood sugar level.",
            f"{Style.RESET_ALL}",
        )


def test_again():
    """Question function if user wants to test again"""

    while True:
        try:
            start = input(
                "Would you like to test again? "
                + Fore.BLUE
                + "(Y/N): "
                + Style.RESET_ALL
            ).upper()
            if start == "Y":
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


if __name__ == '__main__':
    main()  # Call the main function
