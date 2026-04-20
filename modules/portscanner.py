# Import necessary modules for packet manipulation, timing, and system operations
from scapy.all import *
import time
import os

# Define ANSI color codes for colored terminal output
blue = '\033[1;34m'
red = '\033[1;31m'

# Function to save the results of the port scan to a file
def save_results(filename, open_ports, service_name):
    # Open the file in write mode
    with open(filename, "w") as output:
        # Write the header for open ports
        output.write("Open Ports:\n")
        # Loop through each open port and write it with the service name
        for port in open_ports:
            output.write(f"{port}: {service_name}\n")

# ASCII art for the port scanner banner
ghost = r'''
     .-.
   .'   `.                  ---------------
   :g g   :               < | PORTSCANNER |
   : o    `.                ---------------
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'
'''.center(30)

# Main function to run the port scanner
def run():
    # Infinite loop to allow multiple scans
    while True:
        # Print the banner in red color
        print(red)
        print(ghost)
        print('=' * 32)
        print(blue)
        # Prompt user for IP type (IPv4 or IPv6)
        ip_type = int(input("IP Type (1- IPv4 | 2- IPv6): "))
        # Prompt user for the target host
        host = input("Host: ")
        # Prompt user for the initial port to scan
        initial_port = int(input("Initial port (0-65535): "))
        # Prompt user for the final port to scan
        final_port = int(input("Final port (0-65535): "))
        print('-' * 32)
        # Prompt user for stealth mode selection
        stealth = int(input('''Waiting time between each door
-=-=-=-=-=-=-=-=-=-=-=
[ 0 ] Aggressive
[ 1 ] Less Aggressive
[ 2 ] Moderate
[ 3 ] Silent
[ 4 ] Stealth Mode
-=-=-=-=-=-=-=-=-=-=-
@Nexus~# '''))

        # Dictionary mapping stealth modes to delay times
        stealth_modes = {
            0: 0,
            1: 0.1,
            2: 0.3,
            3: 0.7,
            4: 1.5
        }

        # Lists to store open ports for IPv4 and IPv6
        open_ports_ipv4 = []
        open_ports_ipv6 = []

        # Dictionary of common services and their default ports
        services = {
            21: "FTP",
            22: "SSH",
            23: "TELNET",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            445: "SMB",
            3306: "MySQL",
            3389: "RDP",
            6379: "Redis",
            27017: "MongoDB"
        }

        # Function to clear the terminal screen
        def clear_screen():
            # Use 'cls' for Windows, 'clear' for Unix-like systems
            os.system('cls' if os.name == 'nt' else 'clear')

        # Function to scan ports on an IPv4 address
        def scan_ipv4():
            # Loop through the port range
            for port in range(initial_port, final_port + 1):
                # Create a SYN packet for the target port
                pacote = IP(dst=host) / TCP(dport=port, flags="S")
                # Send the packet and wait for a response
                resposta = sr1(pacote, timeout=1, verbose=0)

                # Check if no response was received
                if resposta is None:
                    print(f"[ ? ] {port} is FILTERED")

                # Check if the response has a TCP layer
                elif resposta.haslayer(TCP):
                    # If SYN-ACK received, port is open
                    if resposta[TCP].flags == "SA":
                        # Get the service name for the port
                        service_name = services.get(port, "Unknown")
                        print(f"[ + ] {port} is OPEN - {service_name}")

                        # Add the port to the open ports list
                        open_ports_ipv4.append(port)
                        # Save the results to file
                        save_results("open_ports_ipv4.txt", open_ports_ipv4, service_name)

                        # Send RST to close the connection
                        send(IP(dst=host)/TCP(dport=port, flags="R"), verbose=0)

                    # If RST-ACK received, port is closed
                    elif resposta[TCP].flags == "RA":
                        pass  # Do nothing for closed ports

                # If response is unknown
                else:
                    print(f"[ ? ] {port} unknown")

                # Apply stealth delay between scans
                time.sleep(stealth_modes[stealth])

            # Return the list of open ports
            return open_ports_ipv4

        # Function to scan ports on an IPv6 address
        def scan_ipv6():
            # Loop through the port range
            for port in range(initial_port, final_port + 1):
                # Create a SYN packet for IPv6
                pacote = IPv6(dst=host) / TCP(dport=port, flags="S")
                # Send the packet and wait for a response
                resposta = sr1(pacote, timeout=1, verbose=0)

                # Check if no response was received
                if resposta is None:
                    print(f"[ ? ] {port} is FILTERED")

                # Check if the response has a TCP layer
                elif resposta.haslayer(TCP):
                    # If SYN-ACK received, port is open
                    if resposta[TCP].flags == "SA":
                        # Get the service name for the port
                        service_name = services.get(port, "Unknown")
                        print(f"[ + ] {port} is OPEN - {service_name}")

                        # Add the port to the open ports list
                        open_ports_ipv6.append(port)

                        # Send RST to close the connection
                        send(IPv6(dst=host) / TCP(dport=port, flags="R"), verbose=0)

                    # If RST-ACK received, port is closed
                    elif resposta[TCP].flags == "RA":
                        pass  # Do nothing for closed ports

                # If response is unknown
                else:
                    print(f"[ ? ] {port} unknown")

                # Apply stealth delay between scans
                time.sleep(stealth_modes[stealth])

            # Return the list of open ports
            return open_ports_ipv6

        # Check the IP type and call the appropriate scan function
        if ip_type == 1:
            scan_ipv4()
        elif ip_type == 2:
            scan_ipv6()

        # Print separator
        print('-=' * 21)
        # Ask user if they want to perform another scan
        resp = str(input("Do you want to perform another scan? [Y/N]: ")).upper().strip()
        # If yes, clear screen and continue; else, break the loop
        if resp == 'S':
            clear_screen()
            continue
        else:
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    run()