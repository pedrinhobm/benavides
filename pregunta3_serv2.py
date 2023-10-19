import socket
import psutil  

def get_server_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    return cpu_usage, ram_usage

if __name__ == "__main__":
    server_address = ('127.0.0.1', 50001)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen()

    print(f"Servidor de monitoreo escuchando en {server_address[0]}:{server_address[1]}")

    while True:
        conn, add = sock.accept()
        cpu_usage, ram_usage = get_server_stats()
        message = f"CPU Usage: {cpu_usage}% , RAM Usage: {ram_usage}%"
        conn.sendall(message.encode("utf-8"))
        conn.close()
