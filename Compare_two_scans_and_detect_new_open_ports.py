import json

# Load old scan file
with open("scan_old.json", "r") as f:
    old_scan = json.load(f)

# Load new scan file
with open("scan_new.json", "r") as f:
    new_scan = json.load(f)

# Dictionary to store new open ports
new_open_ports = {}

# Loop through hosts in new scan
for host in new_scan:

    # Check if the same host exists in the old scan
    if host in old_scan:

        # Create an empty list for this host to store new open ports
        new_open_ports[host] = []

        # Loop through protocols (tcp, udp, etc.)
        for proto in new_scan[host]["protocols"]:

            # Get set of ports from new scan for this protocol
            new_ports = set(new_scan[host]["protocols"][proto].keys())

            # Get set of ports from old scan for this protocol
            # .get(proto, {}) avoids error if protocol is missing
            old_ports = set(old_scan[host]["protocols"].get(proto, {}).keys())

            # Find ports that are new
            diff_ports = new_ports - old_ports

            # Store newly opened ports
            for port in diff_ports:
                new_open_ports[host].append(f"{proto}/{port}")

# Print results
if new_open_ports:
    print("New open ports detected:")

    # Loop through each host and its new open ports
    for host, ports in new_open_ports.items():
        if ports:
            print(f"{host}:")
            for p in ports:
                print("  ", p)
else:

    # If no new ports are found
    print("No new open ports detected.")
