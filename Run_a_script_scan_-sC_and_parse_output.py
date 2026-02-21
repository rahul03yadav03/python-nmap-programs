# Import the nmap library to perform script scanning
import nmap


# Create a PortScanner object
scanner = nmap.PortScanner()


# Ask the user to enter the target IP address
target = input("Please enter a IP: ")


# Run default script scan (-sC) on ports 1 to 100
scanner.scan(target,"1-100", arguments="-sC")


# Check if the target host appears in the scan results
if target in scanner.all_hosts():

    # Loop through all TCP ports found in the scan result
    for port in scanner[target]["tcp"]:

        # Check if the port is open
        if scanner[target]["tcp"][port]["state"] == "open":

            # Print the open port number
            print(f"Port {port} is open")

            # Check if script output exists for this port
            if "script" in scanner[target]["tcp"][port]:

                
                # Loop through each script name and its output
                for script_name, script_output in scanner[target]["tcp"][port]["script"].items():
                    print(f"Script Name: {script_name}")
                    print(f"SCript Output: {script_output}")

            else:

                # Print this if no script output is available for the port
                print("No script output")

else:

    # Print this if the host is not found in the scan results
    print("Host not found")
