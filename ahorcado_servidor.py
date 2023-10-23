import random
import socket

my_IP = "127.0.0.1"
port = 5000

dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

def choose_word():
    return random.choice(dictionary)

def hide_word(word):
    return '*' * len(word)

def replace_characters(hidden, word, guess):
    result = list(hidden)
    for i in range(len(word)):
        if word[i] == guess:
            result[i] = guess
    return ''.join(result)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((my_IP, port))
    server.listen(1)
    print(f"Arrancando servidor en {my_IP}:{port}")
    
    while True:
        conn, addr = server.accept()
        print(f"...conexion de: {addr}")
        
        data = conn.recv(1024).decode()
        
        if data == 'start':
            word = choose_word()
            hidden_word = hide_word(word)
            conn.send(hidden_word.encode())
            print("Palabra elegida:", word)
            attempts = 5
            game_over = False
            while attempts > 0 and not game_over:
                client_guess = conn.recv(1024).decode()
                if client_guess in word:
                    hidden_word = replace_characters(hidden_word, word, client_guess)
                    if hidden_word == word:
                        game_over = True
                        conn.send("¡Has ganado!".encode())
                    else:
                        conn.send(hidden_word.encode())  # Enviar la palabra oculta actualizada
                else:
                    attempts -= 1
                    if attempts == 0:
                        conn.send("Has perdido".encode())
                        game_over = True  # Indicar que el juego ha terminado
                    else:
                        conn.send(f"Intento incorrecto. Te quedan {attempts} intentos.".encode())
            conn.close()

if __name__ == "__main__":
    main()
