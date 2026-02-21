#Import namp library to perform the port scanning
import nmap

#create a port scanner object
scanner = nmap.PortScanner()


#Ask user to enter their ip
target = input("Please enter your IP: ")

#Scan port from 1 to 100 on the target ip
scanner.scan(target, "1-100")


#Loop through all tcp ports found in the scan result
for port in scanner[target]["tcp"]:

    
    #Check the state of the current port
    state = scanner[target]["tcp"][port]["state"]


    #check if the port is open 
    if state == "open":

        #print only open ports
        print(f"Port {port} is open")

