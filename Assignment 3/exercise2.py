import os
import socket
import platform

username = os.getlogin() # Get the username

hostname = socket.gethostname() # Get the hostname

ip_address = socket.gethostbyname(hostname) # Get the IP address

os_name = platform.system() # Get the OS name

print(f"Username : {username}")
print(f"Hostname : {hostname}")
print(f"IP Address : {ip_address}")
print(f"OS Name : {os_name}")