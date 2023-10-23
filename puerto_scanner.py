import socket
import sys

def escanear_puertos(ip):
    for puerto in range(1, 101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((ip, puerto))
            print(f"Puerto {puerto} está abierto")
        except (socket.timeout, ConnectionRefusedError):
            print(f"Puerto {puerto} está cerrado")

        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python puerto_escaner.py <dirección_ip>")
        sys.exit(1)

    direccion_ip = sys.argv[1]
    escanear_puertos(direccion_ip)
