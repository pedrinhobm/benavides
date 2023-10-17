import socket
import pickle
import numpy as np

def generar_matrices():
    # Generar dos matrices cuadradas de 2x2
    matriz1 = np.array([[1, 2], [3, 4]])
    matriz2 = np.array([[2, 0], [1, 1]])
    return matriz1, matriz2

def cliente():
    # Configuración del cliente
    host = '127.0.0.1'
    port = 12345
    # Crear un socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    cliente_socket.connect((host, port))

    # Generar matrices
    matriz1, matriz2 = generar_matrices()

    # Enviar matrices al servidor
    cliente_socket.send(pickle.dumps(matriz1))
    cliente_socket.send(pickle.dumps(matriz2))

    # Recibir el resultado del servidor
    resultado = pickle.loads(cliente_socket.recv(1024))

    # Imprimir el resultado
    print("Producto de matrices:")
    print(resultado)

    # Cerrar la conexión
    cliente_socket.close()

if __name__ == "__main__":
    cliente()
