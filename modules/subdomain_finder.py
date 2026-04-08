import socket

yellow = '\033[1;33m'

WORDLISTS = {
    1: "wordlists/n0kovo_subdomains_tiny.txt",
    2: "wordlists/n0kovo_subdomains_small.txt",
    3: "wordlists/n0kovo_subdomains_medium.txt",
    4: "wordlists/n0kovo_subdomains_large.txt",
    5: "wordlists/n0kovo_subdomains_huge.txt"
}

tux = r'''
            .-"""-.
           '       \
          |,.  ,-.  |
          |()L( ()| |                 -----------------
          |,'  `".| |                 |   SUBDOMAIN   |
          |.___.',| `                 |    FINDER     |
         .j `--"' `  `.               -----------------
        / '        '   \
       / /          `   `.
      / /            `    .
     / /              l   |
    . ,               |   |
    ,"`.             .|   |
 _.'   ``.          | `..-'l
|       `.`,        |      `.
|         `.    __.j         )
|__        |--""___|      ,-'
   `"--...,+""""   `._,.-' 
'''

def scan_subdomains(domain, wordlist_path):
    found = 0

    try:
        with open(wordlist_path, "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("Wordlist not found.")
        return

    print("\nStarting search...\n")

    filename = "subdomains_found.txt"
    with open(filename, "w") as output:
        output.write("Subdomains found:\n")

        for sub in subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(full_domain)
                print(f"[+] {full_domain} | Discovered")
                output.write("-=" * 15 + "\n")
                output.write(full_domain + "\n")
                output.flush() 
                found += 1
            except socket.gaierror:
                pass

    print(f"\nTotal found: {found}")
    input("\nPress Enter to exit...")

def run():
    print(yellow)
    print(tux)
    print('=' * 35)
    print("Subdomain Finder selected")
    print("Select the type of subdomain search")

    try:
        domain_type = int(input("""
===================
[ 1 ] Faster
[ 2 ] Summary
[ 3 ] The majority
[ 4 ] Complete
[ 5 ] All of this
===================
@Nexus~# """))
    except ValueError:
        print("Invalid option.")
        return

    if domain_type not in WORDLISTS:
        print("Invalid option.")
        return

    domain = input("Enter the domain address: ").strip()
    scan_subdomains(domain, WORDLISTS[domain_type])

if __name__ == "__main__":
    run()