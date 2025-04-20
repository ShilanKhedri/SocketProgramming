import socket
import threading
import tkinter as tk
from tkinter import messagebox
import sys

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Socket Chat")
        self.client_socket = None
        self.username = None
        
        # GUI
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        # Username input
        tk.Label(self.frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()
        
        # Connect button
        tk.Button(self.frame, text="Connect to Server", command=self.connect_to_server).pack(pady=5)
        
        # Chat area
        self.chat_area = tk.Text(self.frame, height=20, width=50, state='disabled')
        self.chat_area.pack(pady=5)
        
        # Message input
        self.message_entry = tk.Entry(self.frame, width=50)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)
        
        # Send button
        tk.Button(self.frame, text="Send", command=self.send_message).pack(pady=5)
        
    def connect_to_server(self):
        self.username = self.username_entry.get()
        if not self.username:
            messagebox.showerror("Error", "Please enter a username!")
            return
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12345
        
        try:
            self.client_socket.connect((host, port))
            self.client_socket.send(self.username.encode('utf-8'))
            self.append_message(f"Connected to server {host}:{port}")
            
            # Disable username input
            self.username_entry.config(state='disabled')
            
            # Start thread for receiving messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")
            self.client_socket.close()
        
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.append_message(message)
            except:
                break
        self.append_message("Connection lost!")
        self.client_socket.close()
        
    def send_message(self, event=None):
        if not self.client_socket:
            messagebox.showerror("Error", "Connect to server first!")
            return
        
        message = self.message_entry.get()
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
                if message == "/exit":
                    self.client_socket.close()
                    self.root.quit()
                    sys.exit(0)
                self.message_entry.delete(0, tk.END)
            except:
                self.append_message("Error sending message!")
        
    def append_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def on_closing(self):
        if self.client_socket:
            try:
                self.client_socket.send("/exit".encode('utf-8'))
                self.client_socket.close()
            except:
                pass
        self.root.quit()
        sys.exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()