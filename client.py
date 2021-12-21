import socket
import json
import requests
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
response = requests.post('https://httpbin.org/post',
                         json={'id': 1, 'name': 'Jessa'})

print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())
