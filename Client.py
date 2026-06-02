import socket
import threading

SERVER_IP = input("Masukkan IP Server: ")
PORT = 9999

username = input("Masukkan Username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.send(username.encode())

print("\n=== hii halow di Chatroom ===")

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)

        except:
            print("Koneksi terputus")
            client.close()
            break

def send_message():
    while True:
        message = input()

        if message.strip() != "":
            full_message = f"[{username}] {message}"
            client.send(full_message.encode())

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
