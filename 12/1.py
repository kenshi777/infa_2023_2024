import socket
from threading import Thread

def listener(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print("Received:", data.decode('utf-8'))
        except ConnectionResetError:
            break

def main():
    server_address = "51.250.21.231"
    server_port = 9000

    # Подключение к серверу
    sock = socket.socket()
    sock.connect((server_address, server_port))

    # Запуск потока для прослушивания входящих сообщений
    listener_thread = Thread(target=listener, args=(sock,))
    listener_thread.start()

    try:
        while True:
            # Отправка запроса
            message = input("Enter your message: ")
            sock.send(message.encode())

    except KeyboardInterrupt:
        print("Client terminated by user.")
    finally:
        # Завершение потока при завершении программы
        listener_thread.join()
        sock.close()

if __name__ == "__main__":
    main()
