# Import required libraries
import nmap
import json
from datetime import datetime


# Create a PortScanner object
scanner = nmap.PortScanner()

# Ask user to enter the target IP address
target = input("Enter your ip: ")


# Run Nmap scan:
# -sS : TCP SYN scan
# -sV : Service version detection
# -O  : OS detection
scanner.scan(target, arguments="-sS -sV -O")


# Get current date for filename (YYYY-MM-DD)
date = datetime.now().strftime("%Y-%m-%d")


# Dictionary to store scan results
scan_result = {}


# Loop through all hosts found in the scan
for host in scanner.all_hosts():

    # Create dictionary for each host
    scan_result[host] = {}
    scan_result[host]["state"] = scanner[host].state()
    scan_result[host]["protocols"]= {}


    # Loop through all detected protocols (tcp, udp, etc.)
    for proto in scanner[host].all_protocols():

        scan_result[host]["protocols"][proto] = {}


        # Loop through all ports for that protocol
        for port in scanner[host][proto]:
            port_data = scanner[host][proto][port]

            scan_result[host]["protocols"][proto][port] = {
                "state": port_data["state"],
                "service": port_data.get("name", ""),
                "Version": port_data.get("version", "")
                }


# Create filename using current date
filename = f"scan_{date}.json"


# Save scan results to JSON file
with open(filename, "w") as f:
    json.dump(scan_result, f, indent=4)


# Print confirmation message
print("Scan completed and saved to JSON file: ", filename)
