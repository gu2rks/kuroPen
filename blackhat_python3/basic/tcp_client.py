import socket

target_host = "127.0.0.1"
target_port = 20000

# crate socket
#  AF_INET parameter is saying we are going to use a standard IPv4 address or hostname, 
# SOCK_STREAM indicates that this will be a TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send get request as a byte
client.send(b'kuroHat was here')

# receive data
r = client.recv(4096)

print(r.decode("utf-8"))