import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    print(f"Servidor de chat escuchando en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)
    sock.listen(1)

    conn, add = sock.accept()
    print(f"Conexion desde: {add[0]}:{add[1]}")

    while True:
        msg_recv = conn.recv(SOCK_BUFFER)
        print(f"Cliente: {msg_recv.decode('utf-8')}")

        if msg_recv.decode('utf-8').lower() == 'exit':
            break

        msg_send = input("Servidor: ")
        conn.sendall(msg_send.encode("utf-8"))


    sock.close()
