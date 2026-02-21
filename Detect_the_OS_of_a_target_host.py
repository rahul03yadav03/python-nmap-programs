#import nmap library 
import nmap


#create a port scanner object
scanner = nmap.PortScanner()


#ask user to enter the IP address
target = input("Please enter your IP: ")


#Run os detection scan (-O requires admin/root privileges)
scanner.scan(target, arguments= "-O")

# Check if the target host exists in the scan results
if target in scanner.all_hosts():
    #check if OS match rsults exist
    if "osmatch" in scanner[target]:
        for os in scanner[target]["osmatch"]:
            print("The name of OS is: ", os["name"])


    #run this if os not found
    else:
        print("OS could not be detected.")


# Run this if the host is not found in scan results
else:
    print("Host not found")
