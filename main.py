import pyfiglet
from modules import portscanner
from modules import subdomain_finder
from modules import dns_lookup
from modules import exploit_db_search
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def run():
    while True:
        print("Welcome")
        ascii_banner = pyfiglet.figlet_format("Nexus")
        print(ascii_banner)
        print('-' * 32)
        print("The swiss army knife for pentest.")
        print('''
==============================
[ 1 ] Port Scanner
[ 2 ] Subdomain Finder
[ 3 ] DNS Lookup
[ 4 ] Exploit Database Search
[ 5 ] Exit
==============================''')
        choice = int(input("Select an option: "))

        if choice == 1:
            clear()
            portscanner.run()
        elif choice == 2:
            clear()
            subdomain_finder.run()
        elif choice == 3:
            clear()
            dns_lookup.run()
        elif choice == 4:
            clear()
            exploit_db_search.run()
        elif choice == 5:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()