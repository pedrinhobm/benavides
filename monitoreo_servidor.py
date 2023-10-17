import socket
import threading
import time

def handle_client(client_socket):
    # Manejo de la conexión con un cliente
    print(f"Conexion entrante de {client_socket.getpeername()}")
    client_socket.send(b"Bienvenido al servidor")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    print("Esperando conexiones ...")

    try:
        while True:
            client_sock, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_sock,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Cerrando el servidor ...")
        server.close()


if  __name__ == "__main__" :
    start_server()
