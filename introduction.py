from colorama import Fore, Back, Style


def introduction():
    """Introduction function"""

    print(
        f"""{Fore.YELLOW}
          Welcome to our program that helps to find out your risk of
                      type 2 diabetes in the next 10 years

To calculate your risk we will ask you for some data related to your health.
This program doesn't save or transfer any data you provided so anyone cannot
identify you. You are in safe place.{Style.RESET_ALL}

When you pass through our test you'll find out that potential risk level for
developing diabetes in the next 10 years of life depending on points earned:

{Fore.GREEN}Less than 12 points{Style.RESET_ALL}: Low risk
{Fore.CYAN}12 - 14 points{Style.RESET_ALL}:      Average risk
{Fore.MAGENTA}15 - 20 points{Style.RESET_ALL}:      High risk
{Fore.RED}More than 20 points{Style.RESET_ALL}: Very High risk
"""
    )
