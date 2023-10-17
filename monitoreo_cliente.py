import socket
import time

def check_server_status():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)
        client.connect(('127.0.0.1', 12345))
        response = client.recv(1024).decode('utf-8')
        client.close()
        return response == "Bienvenido al servidor"
    except (socket.timeout, ConnectionRefusedError):
        return False

def print_status_message(status):
    if status:
        print("\033[92m[*] El servidor está operativo\033[0m")  # Código ANSI para texto verde
    else:
        print("\033[91m[-] El servidor no responde\033[0m")  # Código ANSI para texto rojo

while True:
    server_status = check_server_status()
    print_status_message(server_status)
    time.sleep(5)
