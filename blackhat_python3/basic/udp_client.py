import socket

target_host = "127.0.0.1"
target_port = 80

# crate socket
# SOCK_DGRAM for udp
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDP is a connectionless protocol that is why no connect()

# send some data
client.sendto(b'AAABBBCCC',(target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(str(data))