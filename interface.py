import subprocess as ssp
from _ast import Raise

from scraping import bounty_platforms

def main():
    ssp.run(['clear'])
    print("Welcome to the bug bounty platform scraper!")
    print("What do you want to do?")
    print("1. Get the list of bounty platforms")
    print("2. Sanitize the list of sites")
    print("3. Extract keywords from the list of sites")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bounty_platforms.get_sites_list()
    elif choice == "2":
        bounty_platforms.sanitize()
    elif choice == "3":
        bounty_platforms.extract_keywords()
    elif choice == "4":
        print("Thanks for using this tool!")
        raise SystemExit()

    else:
        print("Invalid choice!")
        main()

if __name__ == "__main__":
    main()