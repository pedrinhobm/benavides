import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(1)

    print("Esperando a que el cliente se conecte...")
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    while True:
        message = input('> ')
        client_socket.send(message.encode())

        if message.lower() == 'salir':
            break

        received_message = client_socket.recv(1024).decode()
        print(f'Cliente: {received_message}')

        if received_message.lower() == 'salir':
            break

    print("Conversación terminada.")
    server_socket.close()

if __name__ == "__main__":
    start_server()
