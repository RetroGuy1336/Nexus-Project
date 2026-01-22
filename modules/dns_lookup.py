import socket
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def run():
    while True:
        print("Dns Lookup selected")
        print("Enter the domain adress. Ex:www.google.com")
        domain_adress = str(input(": "))

        try:
            results = socket.getaddrinfo(domain_adress, None)

            print("\nResults Found:\n")

            ips = set() #<- avoids duplicate IP addresses

            filename = "dns_found.txt"
            with open(filename, "w") as output:
                output.write("DNS IP address found:\n")
                for result in results:
                    ip = result[4][0]
                    ips.add(ip)

                for ip in ips:
                    print(ip)
                    output.write("-=" * 15 + "\n")
                    output.write(ip + "\n")
                    output.flush() 

            

        except socket.gaierror:
            print("Error: The domain could not be resolved..")
        resp = str(input("\nDo you want to perform another lookup? [Y/N]: ")).upper().strip()
        if resp == 'S':
            continue
        else:
            clear()
            break     
    

if __name__ == "__main__":
    run()