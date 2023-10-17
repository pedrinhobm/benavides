import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    while True:
        received_message = client_socket.recv(1024).decode()
        print(f'Servidor: {received_message}')

        if received_message.lower() == 'salir':
            break

        message = input('> ')
        client_socket.send(message.encode())

        if message.lower() == 'salir':
            break

    print("Conversación terminada.")
    client_socket.close()

if __name__ == "__main__":
    start_client()
