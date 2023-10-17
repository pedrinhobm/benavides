import socket

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        # El cliente elige la posición y la envía al servidor
        posicion = int(input("Ingrese la posición deseada: "))
        sock.sendall(str(posicion).encode("utf-8"))

        # El cliente recibe la respuesta del servidor
        data = sock.recv(1024)
        print(f"El número en la posición {posicion} es: {data.decode('utf-8')}")
    finally:
        print("Cerrando conexión")
        sock.close()
