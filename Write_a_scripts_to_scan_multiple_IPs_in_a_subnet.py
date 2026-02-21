#import nmap library to scan multiple ip
import nmap


#create a port scanner object
scanner = nmap.PortScanner()

#Ask user to enter subnet
target = input("Please enter your ip(subnet, ex:- xxx.xxx.xxx.xxx/24): ")


#Run a ping scan (-sn) and fast port scan (-F) on the subnet
scanner.scan(target, arguments="-sn -F")


#Loop through all hosts found in the scan results
for ip in scanner.all_hosts():

    #Check if the host is up
    if scanner[ip].state()=="up":

        #Loop through all tcp ports for that host
        for port in scanner[ip]["tcp"]:


            #Check if the port is open and print the open port
            if scanner[ip]["tcp"][port]["state"] == "open":
                print(f"IP {ip} is open on Port {port}")
