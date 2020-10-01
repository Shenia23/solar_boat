import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12340
MESSAGE = b'Hello Server!'
BUFFER_SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP,SERVER_PORT))
    print('Sending data: ')

  #while True:
    f = open("myfile.txt", "rb")
    content = f.read(1024)
    
    while content:
        # Enviar contenido.
        client.send(content)
        content = f.read(1024)
    
    print('File sent')

    #client.send(MESSAGE)
    data = client.recv(BUFFER_SIZE)

    client.close()
    f.close()

    print('The server responded: {}'.format(data))

def generate_file():
    print('Generación de un fichero para probar el envio de datos en conexión WiFi')
    file = open("prueba.txt", "w")
    file.write("Para comprobar el correcto funcionamiento de la conexión")
    file.close()
        

if __name__ == '__main__':
    main()
