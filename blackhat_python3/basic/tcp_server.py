import socket
import threading

bind_ip = "0.0.0.0" #local host
bind_port = 20000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5) # check this if you want to listen for more request

print('[*] Listening on %s:%d' % (bind_ip, bind_port))

# thread for handeling clients
def handle_client(client_socket):
    # print out what the client sends
    r = client_socket.recv(1024)
    print('[*] Received: %s' % r.decode("utf-8"))

    # send back a message
    client_socket.send(b'WAZZAP')

    client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Accepted connection from: %s:%d' % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
