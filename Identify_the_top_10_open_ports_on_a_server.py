#import nmap library to scan to 10 ports
import nmap


#create a portscanner object
scanner = nmap.PortScanner()


#Ask user to enter ip address
ip = input("Enter your ip: ")


#Run a scan on the top 10 most common ports
scanner.scan(ip, arguments = "--top-ports 10")

#Check if the host appear in the scan results
if ip in scanner.all_hosts():

    #Check if TCP scan results exist for the host
    if "tcp" in scanner[ip]:

        #Loop through all TCP ports found in the scan result
        for port in scanner[ip]["tcp"]:

            #Check if the port state is open
            if scanner[ip]["tcp"][port]["state"] == "open":

                #Print the open port number
                print(f"Port {port} is open on host {ip}")


#Run this if the host is not found in scan result
else:
    print("Host not found or unreachable")
