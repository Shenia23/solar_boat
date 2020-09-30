import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
MESSAGE = b"Hello Server!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP,SERVER_PORT))
client.send(MESSAGE)
data = client.recv(1024)

client.close()

print("The server responded: {}".format(data))