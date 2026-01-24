# Nexus, the Swiss Army Knife for pentest
The Nexus is a comprehensive pentesting tool that combines multiple functionalities into a single package. It is designed to assist security professionals in performing various tasks such as port scanning, DNS lookups, vulnerability assessments, and more.
Warning: Nexus is designed to aid in information security in an ethical and secure manner; misuse of Nexus can lead to consequences!

## Requirements
- Python 3.10 or higher
- Required Python packages (listed in requirements.txt)
- Internet connection for certain functionalities
- The OS must be Windows or Linux-based


## TCP Port Scanner
A scanner to identify open ports and their running services.

Features:
- Identifies open TCP ports on a target host.
- Detects services running on open ports.
- Support for IPv4 and IPv6 addresses.
- Configurable timeout and scan speed.
- Stealth Mode to minimize detection.

## Example
Input: 127.0.0.1

Output:
Open Ports:
22 - ssh
80 - http
443 - https

## Dns Lookup
A tool for identifying domain names.

Features:
- Resolves domain names to IP addresses (IPv4/IPv6), allowing the identification of the actual destination of network connections before scanning.

## Example
Input: google.com

Output:
142.250.78.14
2a00:1450:4009:80b::200e

## Subdomain Finder
A tool for finding subdomains of a given domain.

Features:
- Uses a predefined list of common subdomains to discover potential subdomains.
- It contains 5 subdomain search modes, with mode 1 being the fastest but incomplete, and mode 5 being complete but slow.
- It helps in discovering flaws, from minor to critical, in discovered subdomains.

## Example
Input: Mode 3, example.com

Output:
blog.example.com
shop.example.com
dev.example.com
mail.example.com
admin.example.com

## Exploit Database Search
A tool for searching known vulnerabilities and exploits.

Features:
- Searches a local database of known vulnerabilities and exploits based on user-defined keywords.
- It helps in finding exploits for an ethical penetration test.

## Example
Input: CVE-2021-44228

Output:
Exploit found: Apache Log4j2 Remote Code Execution (CVE-2021-44228)
Description: A critical vulnerability in Apache Log4j2 that allows remote code execution.
Reference: https://nvd.nist.gov/vuln/detail/CVE-2021-44228

## How to use the Nexus
1. Download the Nexus tool from the repository using the command:
   ```git clone https://github.com/RetroGuy1336/Nexus-Project.git``
2. Install the required Python packages using pip:
   ```pip install -r requirements.txt```
3. Run the Nexus tool using Python:
   ```python3 main.py```
4. Follow the on-screen instructions to select and use the desired functionality.

## Contributing
Contributions to the Nexus project are welcome! If you have suggestions for new features, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.