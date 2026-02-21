# Import the nmap library to perform network scanning
import nmap

# Import datetime module to generate date for filename
from datetime import datetime


# Create a PortScanner object
scanner = nmap.PortScanner()


# Ask user to enter the target IP address
target = input("Enter your ip: ")


# Run Nmap scan:
# -sV : Service version detection
# -sS : TCP SYN scan
# -O  : OS detection (requires admin/root privileges)
scanner.scan(target, arguments="-sV -sS -O")


# Get current date in YYYY-MM-DD format
date = datetime.now().strftime("%Y-%m-%d")


# Open a file with date in filename to save scan results
with open(f"scan_{date}.txt", "w") as f:

    # Loop through all hosts found by Nmap
    for host in scanner.all_hosts():

        # Check if the host is up
        if scanner[host].state() == "up":

            # Loop through all detected protocols (tcp, udp, etc.)
            for proto in scanner[host].all_protocols():

                # Loop through all ports for that protocol
                for port in scanner[host][proto]:

                    # Get the state of the port (open/closed/filtered)
                    state = scanner[host][proto][port]["state"]

                    # Write scan result to file
                    f.write(f"{host} {proto} {port} {state} \n")
# Print confirmation message
print("Daily scan completed")
