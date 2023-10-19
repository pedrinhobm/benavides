import socket
import datetime

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    print(f"Servidor de tiempo escuchando en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)
    sock.listen()

    while True:

        conn, client_address = sock.accept()
        print(f"Conexion desde: {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)

                if data.decode('utf-8') == 'solicito su tiempo':
                    tiempo = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
                    conn.sendall(tiempo.encode('utf-8'))
                else:
                    break  

        except ConnectionResetError:
            print("El cliente ha cerrado la conexion de forma abrupta")
        finally:
            conn.close()

       