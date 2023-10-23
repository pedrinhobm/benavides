import socket
import numpy as np
import time

def calcular_negativo(imagen):
    negativo = 255 - imagen
    return negativo

def recibir_imagen_y_calcular_negativo():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(1)
    print("Esperando conexión...")
    
    try:
        while True:
            conn, addr = server.accept()
            print(f"Conexión establecida desde {addr}")
            
            try:
                start_time = time.time()
                data = conn.recv(4096)
                end_time = time.time()
                print(f"Tiempo para recibir la imagen en el servidor: {end_time - start_time} segundos")
                
                imagen = np.frombuffer(data, dtype=np.uint8).reshape((64, 64))
                
                start_time = time.time()
                negativo = calcular_negativo(imagen)
                end_time = time.time()
                print(f"Tiempo para calcular negativo en el servidor: {end_time - start_time} segundos")
                
                start_time = time.time()
                conn.send(negativo.tobytes())
                end_time = time.time()
                print(f"Tiempo para enviar el negativo desde el servidor: {end_time - start_time} segundos")
            except Exception as e:
                print(f"Error en la comunicación: {e}")
            finally:
                conn.close()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()

if __name__ == "__main__":
    recibir_imagen_y_calcular_negativo()
