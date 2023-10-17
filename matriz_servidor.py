import socket
import pickle
import numpy as np

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def handle_client(client_socket):
    # Recibir la primera matriz
    matrix1_data = client_socket.recv(1024)
    matrix1 = pickle.loads(matrix1_data)

    # Recibir la segunda matriz
    matrix2_data = client_socket.recv(1024)
    matrix2 = pickle.loads(matrix2_data)

    # Multiplicar las matrices
    result_matrix = multiply_matrices(matrix1, matrix2)

    # Enviar el resultado al cliente
    result_data = pickle.dumps(result_matrix)
    client_socket.send(result_data)

    # Cerrar la conexión
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Esperando conexiones ...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    run_server()
