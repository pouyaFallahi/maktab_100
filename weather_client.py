import socket

HOST = '127.0.0.1'
PORT = 1124

def create_tcp():
    #Create a TCP protocol socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket


def connection():
    client_socket = create_tcp()
    client_socket.connect((HOST, PORT))

    city = ''
    while city != 'exit':
        city = input('enter your city:')

        if city != 'exit':
            client_socket.send(city.encode())

            response = client_socket.recv(1024)
            print(f'server respons: {response.decode()}')

    client_socket.close()

if __name__ == '__main__':
    connection()