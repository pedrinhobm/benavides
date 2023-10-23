import socket
import numpy as np
import matplotlib.pyplot as plt
import time

def guardar_imagen_como_png(img_array):
    plt.imshow(img_array, cmap='gray')
    plt.axis('off')
    plt.savefig('imagen_en_negativo.png', bbox_inches='tight')

def enviar_imagen_calcular_negativo():
    imagen = np.load('lena_64x64.npy')
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('localhost', 12345))
        start_time = time.time()
        client.send(imagen.tobytes())
        end_time = time.time()
        print(f"Tiempo para enviar la imagen desde el cliente: {end_time - start_time} segundos")
        
        data = client.recv(4096)
        
        start_time = time.time()
        negativo = np.frombuffer(data, dtype=np.uint8).reshape((64, 64))
        end_time = time.time()
        print(f"Tiempo para recibir el negativo en el cliente: {end_time - start_time} segundos")
        
        start_time = time.time()
        guardar_imagen_como_png(negativo)
        end_time = time.time()
        print(f"Tiempo para guardar la imagen en el cliente: {end_time - start_time} segundos")
    except Exception as e:
        print(f"Error en la comunicación con el servidor: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    enviar_imagen_calcular_negativo()
