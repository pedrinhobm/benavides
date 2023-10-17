import socket

SOCK_BUFFER = 1024

def obtener_valor(posicion):
    # Lee el archivo de texto 'codigo.txt' y devuelve el valor en la posición indicada
    with open('codigo.txt', 'r') as file:
        numeros = [int(num) for num in file.read().split()]
        if 0 < posicion <= len(numeros):
            return numeros[posicion - 1]
        else:
            return None

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Iniciando servidor en IP {server_address[0]} y puerto {server_address[1]}")

    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("Esperando conexiones ...")
        conn, client_address = sock.accept()
        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)

                if data:
                    posicion = int(data.decode("utf-8"))
                    valor = obtener_valor(posicion)

                    if valor is not None:
                        conn.sendall(str(valor).encode("utf-8"))
                        print(f"Enviado valor {valor} para la posición {posicion}")
                    else:
                        conn.sendall("Posición fuera de rango".encode("utf-8"))
                        print("Posición fuera de rango")
                else:
                    print("No hay más datos")
                    break
        except (ConnectionResetError, ValueError):
            print("El cliente ha cerrado de forma abrupta la conexión o ha enviado datos no válidos")
        finally:
            print("Cerrando la conexión")
            conn.close()

