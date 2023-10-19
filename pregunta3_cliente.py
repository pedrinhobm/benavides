import socket
import time

def get_server_info(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    data = sock.recv(1024)
    sock.close()
    return data.decode("utf-8")

if __name__ == "__main__":
    server1_address = ('127.0.0.1', 50000)
    server2_address = ('127.0.0.1', 50001)

    while True:
        info1 = get_server_info(server1_address)
        info2 = get_server_info(server2_address)

        print(f"Informacion de uso del servidor {server1_address[0]}:{server1_address[1]}: {info1}")
        print(f"Informacion de uso del servidor {server2_address[0]}:{server2_address[1]}: {info2}")

        time.sleep(5) 
