#Import nmap library to perform host discovery
import nmap


#create a portscanner object
scanner = nmap.PortScanner()


# Ask the user to enter the target IP address
target = input("Please enter your ip: ")

#Run a host discovery scan (-sn checks if the host is alive without scanning ports)
scanner.scan(target, arguments = "-sn")

# Check if the target host appears in the scan results
if target in scanner.all_hosts():

    # Get the state of the host (up or down)
    state = scanner[target].state()

    # Print whether the host is up or down
    print(f"The host is {state}")


else:

    # Print this message if the host is not found in scan results
    print("Host not found")
