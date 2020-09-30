import socket

SERVER_IP = '192.168.1.98'
SERVER_PORT = 12345
MESSAGE = b'Hello Client!'
BUFFER_SIZE = 1024

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))

    while True:
        print('Server listening on port {}'.format(SERVER_PORT))
        server.listen(1)

        conn, addr = server.accept()
        print('Connection address:', addr)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: 
                break
            print('Received data:', data)
            conn.send(MESSAGE)

        print('Connection closed\n')
        conn.close()

if __name__ == '__main__':
    main()