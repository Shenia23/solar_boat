import socket

SERVER_IP = '192.168.1.98'
SERVER_PORT = 12345
MESSAGE = b'Hello Server!'
BUFFER_SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP,SERVER_PORT))
    print('Sending data: {}'.format(MESSAGE))
    client.send(MESSAGE)
    data = client.recv(BUFFER_SIZE)

    client.close()

<<<<<<< HEAD
print("The server responded: {}".format(data))
=======
    print('The server responded: {}'.format(data))


if __name__ == '__main__':
    main()
>>>>>>> a4b5185c49d32248e9dc762621ea417256cf7343
