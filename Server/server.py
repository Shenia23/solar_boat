import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12340
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

        conn.setblocking(0)


        f = open("recibido.txt", "wb")

        while (True):

    # Recibimos y escribimos en el fichero
            try:
                input_data = conn.recv(1024)
                f.write(input_data)
            except BlockingIOError:
                break

        f.close()

        
        print("El archivo se ha recibido correctamente.")

        conn.send(b'Fichero recibido')

        conn.close()

if __name__ == '__main__':
    main()