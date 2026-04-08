import socket
import time
import os

blue = '\033[1;34m'
red = '\033[1;31m'

def save_results(filename, open_ports, service_name):
    with open(filename, "w") as output:
        output.write("Open Ports:\n")
        for port in open_ports:
            output.write(f"{port}: {service_name}\n")

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

def run():
    while True:
        print(red)
        print(ghost)
        print('=' * 32)
        print(blue)
        #INSERT THE HOST AND THE TYPE OF IP TO SCAN
        ip_type = int(input("IP Type (1- IPv4 | 2- IPv6): "))
        host = input("Host: ")
        initial_port = int(input("Initial port (0-65535): "))
        final_port = int(input("Final port (0-65535): "))
        print('-' * 32)
        stealth = int(input('''Waiting time between each door
-=-=-=-=-=-=-=-=-=-=-=
[ 0 ] Aggressive
[ 1 ] Less Aggressive
[ 2 ] Moderate
[ 3 ] Silent
[ 4 ] Stealth Mode
-=-=-=-=-=-=-=-=-=-=-
@Nexus~# '''))

        #DICTIONARY OF STEALTH MODES
        stealth_modes = {
            0: 0,
            1: 0.1,
            2: 0.3,
            3: 0.7,
            4: 1.5
        }


        #STORES OPEN PORTS
        open_ports_ipv4 = []
        open_ports_ipv6 = []

        #DICTIONARY OF SERVICES AND PORTS
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

        #FUNCTION TO CLEAR SCREEN
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        #FUNCTION TO SCAN IPV4
        def scan_ipv4():
            #CREATES A LOOP TO SCAN OPEN PORTS
            for ports in range(initial_port, final_port +1):

                #CREATES A CONNECTION WITH THE HOST
                ipv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                #TIME TO SCAN PORTS (sleep)
                ipv4.settimeout(1)

                #SHOWS CONNECTION RESULTS
                resultado = ipv4.connect_ex((host, ports))

                #IF THE RESULT IS 0, THE PORT IS OPEN
                if resultado == 0:
                    service_name = services.get(ports, "Unknown")
                    print(f"[+] {ports} OPEN - {service_name}")

                    #ADDS THE OPEN PORT TO A LIST
                    open_ports_ipv4.append(ports)
                    save_results("open_ports_ipv4.txt", open_ports_ipv4, service_name)

                #CLOSES THE CONNECTION WITH THE HOST
                ipv4.close()
                time.sleep(stealth_modes[stealth])

            return open_ports_ipv4

        #FUNCTION TO SCAN IPV6
        def scan_ipv6():
                #CREATES A LOOP TO SCAN OPEN PORTS
            for ports in range(initial_port, final_port +1):

                #CREATES A CONNECTION WITH THE HOST
                ipv6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

                #TIME TO SCAN PORTS (sleep)
                ipv6.settimeout(1)

                #SHOWS CONNECTION RESULTS
                resultado = ipv6.connect_ex((host, ports, 0, 0))

                #IF THE RESULT IS 0, THE PORT IS OPEN
                if resultado == 0:
                    service_name = services.get(ports, "Unknown")
                    print(f"[+] {ports} OPEN - {service_name}")

                    #ADDS THE OPEN PORT TO A LIST
                    open_ports_ipv6.append(ports)
                    save_results("open_ports_ipv6.txt", open_ports_ipv6, service_name)

                #CLOSES THE CONNECTION WITH THE HOST
                ipv6.close()
                time.sleep(stealth_modes[stealth])
            return open_ports_ipv6

        if ip_type == 1:
            scan_ipv4()
        elif ip_type == 2:
            scan_ipv6()

        print('-=' * 21)
        resp = str(input("Do you want to perform another scan? [Y/N]: ")).upper().strip()
        if resp == 'S':
            clear_screen()
            continue
        else:
            break

if __name__ == "__main__":
    run()