# Import nmap library to perform version detection
import nmap


# Create a PortScanner object
scanner = nmap.PortScanner()


# Ask the user to enter the target IP address
target = input("Please enter your IP: ")


# Run version detection scan on ports 1 to 100
scanner.scan(target,"1-100", arguments = "-sV")

# Loop through all TCP ports found in the scan result
for port in scanner[target]["tcp"]:


    # Check if the port is open
    if scanner[target]["tcp"][port]["state"] == "open":


        # Get service name and version
        service = scanner[target]["tcp"][port]["name"]
        version = scanner[target]["tcp"][port]["version"]


        #Print open port, service name and version
        print(f"Port {port} is open")
        print(f"Service: {service}")
        print(f"Version: {version}")

    
