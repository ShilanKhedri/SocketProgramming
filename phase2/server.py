import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connection established with {client_address}")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Message received from {client_address}: {data}")
            response = f"Server: Message '{data}' received!"
            client_socket.send(response.encode('utf-8'))
        except:
            break
    print(f"Connection with {client_address} closed")
    client_socket.close()

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