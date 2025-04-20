import socket
import threading
import time

clients = {}  # Dictionary: {client_socket: (address, username)}

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                del clients[client]

def handle_client(client_socket, client_address):
    try:
        # Receive username
        username = client_socket.recv(1024).decode('utf-8')
        clients[client_socket] = (client_address, username)
        print(f"Connection established with {client_address} (username: {username})")
        broadcast(f"{username} joined the chat!", client_socket)
        
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if data == "/exit":
                break
            if data.startswith("/pm "):
                # Private message: /pm <userIP> <message>
                parts = data.split(" ", 3)
                if len(parts) < 3:
                    client_socket.send("Invalid format: /pm <userIP> <message>".encode('utf-8'))
                    continue
                target_ip, message = parts[1], parts[2]
                for client, (addr, uname) in clients.items():
                    if addr[0] == target_ip:
                        timestamp = time.strftime("%H:%M:%S")
                        client.send(f"[Private from {username} at {timestamp}]: {message}".encode('utf-8'))
                        client_socket.send(f"[Private to {target_ip} at {timestamp}]: {message}".encode('utf-8'))
                        break
                else:
                    client_socket.send(f"User with IP {target_ip} not found!".encode('utf-8'))
            elif data == "/list":
                # Show list of IPs
                ip_list = "\n".join([f"{addr[0]} ({uname})" for _, (addr, uname) in clients.items()])
                client_socket.send(f"Connected users:\n{ip_list}".encode('utf-8'))
            else:
                # Group message
                timestamp = time.strftime("%H:%M:%S")
                message = f"[{username} at {timestamp}]: {data}"
                print(f"Message received: {message}")
                broadcast(message, client_socket)
    except:
        pass
    
    print(f"Connection with {client_address} closed")
    username = clients[client_socket][1]
    del clients[client_socket]
    client_socket.close()
    broadcast(f"{username} left the chat")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host = '127.0.0.1'
    port = 12345
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server running on {host}:{port}...")
        
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()