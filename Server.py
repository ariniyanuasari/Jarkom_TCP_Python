import socket
import threading

HOST = '0.0.0.0'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print(f"Server berjalan di port {PORT}")

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print(message.decode())

            broadcast(message, client)

        except:
            clients.remove(client)
            client.close()
            break

while True:
    client, addr = server.accept()

    username = client.recv(1024).decode()

    join_message = f"\n=== {username} joined the chat ==="

    print(join_message)

    broadcast(join_message.encode())

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()
