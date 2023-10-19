import socket

SOCK_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)

    print(f"Conectando a servidor")  
    sock.connect(server_address)

    while True:
        msg_send = input("Cliente: ")
        sock.sendall(msg_send.encode("utf-8"))

        if msg_send.lower() == 'exit':
            break

        msg_recv = sock.recv(SOCK_BUFFER)
        print(f"Servidor: {msg_recv.decode('utf-8')}")

        if msg_recv.decode('utf-8').lower() == 'exit':
            break

    sock.close()
