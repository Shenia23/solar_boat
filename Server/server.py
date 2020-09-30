import socket

SERVER_IP = "192.168.1.98"
SERVER_PORT = 12345
MESSAGE = b"Hello Client!"
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(1)

conn, addr = server.accept()
print('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        break
    print("received data:", data)
    conn.send(MESSAGE)  # echo
conn.close()