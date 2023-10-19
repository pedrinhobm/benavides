import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)

    try:
        msg = 'solicito su tiempo'
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
        print(f"Hora actual del servidor: {data.decode('utf-8')}")
    finally:
        sock.close()
