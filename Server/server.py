import socket
import time

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
            
            start = time.time()
            data_bits = 0.0


            conn.settimeout(1.0)

            f = open("recibido.txt", "wb")

            while (True):
                try:
                    input_data = conn.recv(BUFFER_SIZE)
                    
                    data_bits += len(input_data)*8.0
                    timediff = time.time() - start
                    bitrate = data_bits/(timediff*1000000)
                    
                    print('Bitrate: {:.3f} Mbps'.format(bitrate))
                    f.write(input_data)
                except socket.timeout:
                    break

            f.close()

            print("El archivo se ha recibido correctamente.\n")

            conn.send(b'Fichero recibido')

            conn.close()

        except KeyboardInterrupt:
            conn.close()
            server.close()
            print(' ->Shutting down the server')
            exit()

if __name__ == '__main__':
    main()
