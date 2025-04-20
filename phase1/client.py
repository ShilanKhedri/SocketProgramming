import socket

def start_client():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set address and port
    host = '127.0.0.1'
    port = 12345
    
    # Connect to server
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    
    # Send message
    message = "Hello Server!"
    client_socket.send(message.encode('utf-8'))
    
    # Receive response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    
    # Close connection
    client_socket.close()

if __name__ == "__main__":
    start_client()