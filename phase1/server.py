import socket

def start_server():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Set address and port
    host = '127.0.0.1'
    port = 12345
    
    # Bind socket to address and port
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server running on {host}:{port}...")
    
    while True:
        # Accept client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive message
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Message received: {data}")
        
        # Send response
        response = "Hello Client!"
        client_socket.send(response.encode('utf-8'))
        
        # Close connection
        client_socket.close()
        print(f"Connection with {client_address} closed")

if __name__ == "__main__":
    start_server()