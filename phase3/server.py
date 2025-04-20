import socket
import threading

clients = []  # List of connected clients

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket, client_address):
    clients.append(client_socket)
    print(f"Connection established with {client_address}")
    
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data == "/exit":
                break
            message = f"{client_address[0]}: {data}"
            print(f"Message received: {message}")
            broadcast(message, client_socket)
        except:
            break
    
    print(f"Connection with {client_address} closed")
    clients.remove(client_socket)
    client_socket.close()
    broadcast(f"{client_address[0]} left the chat")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '127.0.0.1'
    port = 12345
    
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server running on {host}:{port}...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()