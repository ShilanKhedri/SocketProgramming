import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            break
    client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 12345
    
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")
    
    # Start thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    # Send messages
    while True:
        message = input()
        if message == "/exit":
            client_socket.send(message.encode('utf-8'))
            break
        client_socket.send(message.encode('utf-8'))
    
    client_socket.close()
    sys.exit(0)

if __name__ == "__main__":
    start_client()