import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12345
MESSAGE = b'Hello Client!'
BUFFER_SIZE = 1024

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))

    while True:
        try:
            print('Server listening on port {}'.format(SERVER_PORT))
            server.listen(1)

            conn, addr = server.accept()
            print('Connection address:', addr)

            conn.setblocking(0)

            f = open("recibido.txt", "wb")

            while (True):
                try:
                    input_data = conn.recv(BUFFER_SIZE)
                    print(input_data)
                    f.write(input_data)
                except BlockingIOError:
                    break

            f.close()

            print("El archivo se ha recibido correctamente.")

            conn.send(b'Fichero recibido')

            conn.close()

        except KeyboardInterrupt:
            conn.close()
            server.close()
            print(' ->Shutting down the server')
            exit()

if __name__ == '__main__':
    main()
