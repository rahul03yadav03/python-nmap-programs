# PYTHON NMAP PROGRAMS – Network Scanning Using Python

# About This Project

- This repository contains multiple Python programs built using the `python-nmap` library.
- The purpose of this project is to practice and understand:
  - Network scanning concepts
  - Port detection
  - Service and version detection
  - OS detection
  - Script scanning
  - Subnet scanning
  - Scan comparison logic
  - Saving scan results in TXT and JSON format
- This project was created as part of my cybersecurity learning journey.


# Project Description

- Through this project, I explored how network reconnaissance works using Nmap and how it can be automated using Python.
- I implemented different types of scans including:
  - Basic port scanning
  - Full TCP SYN scanning
  - Service and version detection
  - OS detection
  - Script scanning
  - Host discovery
  - Subnet scanning
  - Comparing old and new scan results
- The goal was to understand how network information is gathered in a structured and programmatic way.


# Objectives

- Understand how Nmap works
- Learn TCP port scanning concepts
- Detect running services and versions
- Identify operating systems
- Perform host discovery
- Scan multiple IPs in a subnet
- Store scan results in JSON/TXT
- Compare scans to detect new open ports
- Practice safe and ethical network testing


# Programs Implemented

- Basic Port Scan (Ports 1–100)  
- Top 10 Ports Scan  
- Full Scan (-sS -sV -O)  
- Version Detection (-sV)  
- Script Scan (-sC)  
- Host Discovery (-sn)  
- OS Detection (-O)  
- Subnet Scan (-sn -F)  
- Save Scan Results to TXT  
- Save Scan Results to JSON  
- Compare Old vs New Scan Results


# Requirements

- Python 3.x
- Nmap installed on system
- python-nmap library



# Installation
-  Install Nmap
- Check if installed:
  - nmap --version


# If not installed:
- Linux:
  - sudo apt install nmap
- Windows:
  - Download from official Nmap website.

# Install Python Library
- pip install python-nmap



# How To Run

- Open terminal in project folder
 - Run any script:
  - python file_name.py
 - Enter the target IP address when prompted


# What Nmap Detects
- IP Address
- Host status (Up/Down)
- Open Ports
- Running Services
- Service Versions
- Operating System (when possible)
- Script Results
- Network Protocols (TCP/UDP)


# Learning Level

- Beginner to Intermediate
- Suitable for cybersecurity students
- Good foundation for network reconnaissance concepts
- Helps understand how scanners gather information



# Disclaimer

- This project is created for educational purposes only.
- Do not scan networks without proper authorization.
- Unauthorized scanning may be illegal.
- No exploitation techniques are included.



# Author

- Rahul Yadav
- Cybersecurity Student


# License

- MIT License


# Language

- Python 

