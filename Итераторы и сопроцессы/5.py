import threading
import time
import random

class WriteToFile:
    def __init__(self, username):
        self.username = username
        self.file_path = f"{self.username}.txt"
        self.file_obj = None
        self.lock = threading.Lock()

    def write_to_file(self, message):
        with self.lock:
            if self.file_obj is None:
                self.file_obj = open(self.file_path, 'w')

            self.file_obj.write(message + '\n')

    def close_connection(self):
        with self.lock:
            if self.file_obj:
                self.file_obj.close()
                print(f"Connection closed for user {self.username}")

def connect_user(username, auth=True):
    write_to_file_instance = WriteToFile(username)

    if auth:
        auth_data = f"auth {username}"
        write_to_file_instance.write_to_file(auth_data)

    for message in user_connection(username):
        write_to_file_instance.write_to_file(message)

    if auth:
        write_to_file_instance.close_connection()

def user_connection(username):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    id = f"{random.randint(0, 100000000):010}"
    if auth:
        yield f"auth {id}"
    for message in user_connection(id):
        yield message
    if auth:
        yield f"disconnect {id}"

def connection():
    connections = [establish_connection(True) for _ in range(10)]
    connections.extend([establish_connection(False) for _ in range(2)])

    while connections:
        conn = random.choice(connections)
        try:
            for message in conn:
                print(message)
        except StopIteration:
            connections.remove(conn)

def main():
    threads = [threading.Thread(target=connect_user, args=(username,)) for username in range(10)]
    threads.append(threading.Thread(target=connection))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()