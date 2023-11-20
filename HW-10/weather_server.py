import socket
from get_weather_data import get_weather_data

HOST = '127.0.0.1'
PORT = 1124

def create_tcp():
    #Create a TCP protocol socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(server_socket)
    return server_socket

def connection():
    server_socket = create_tcp()
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    print('server is run, waiting client...')

    client_socket, client_address = server_socket.accept()
    print(f'connected to {client_address}')

    city = ''
    while city != 'exit':
        try:
            city = client_socket.recv(1024)

            if city != 'exit':
                response = get_weather_data(city)
                if response:
                    message = f"Weather in {city}:\nTemperature: {response['main']['temp']}°C\nDescription: {response['weather'][0]['description']}"
                else:
                    message = 'Failed to fetch weather data.'

                client_socket.send(message.encode())

        except TypeError:
            error_message = 'Please enter the name of the city'
            client_socket.send(error_message.encode())


    server_socket.close()
    client_socket.close()

if __name__ == '__main__':
    connection()
