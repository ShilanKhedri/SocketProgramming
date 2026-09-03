<div dir="ltr" align="left">

# Multi-Client Chat Application

A phased implementation of a multi-client chat system built in Python using socket programming, threading, and a GUI interface.

## 🛠️ How to Run

### 1. Start the Server
Run the following command to launch the server (runs on `127.0.0.1:12345` by default):

```bash
python server.py
```

### 2. Start the Client
Run the client script in a separate terminal window:

```bash
python client.py
```

* **Phases 1–3:** Messages are sent and received via the command-line interface (CLI).
* **Phase 4:** Launches a Graphical User Interface (GUI).

---

## 💬 Commands

* `/exit` — Disconnect and leave the chat room.
* `/list` — Display the list of currently connected users *(Phase 4)*.
* `/pm <userIP> <message>` — Send a private message to a specific user *(Phase 4)*.

---

## 📁 Project Structure

```text
├── server.py   # Server implementation handling connections and message routing
└── client.py   # Client application for connection management and user interface
```

> **Note:** Designed with clean architecture principles, self-explanatory naming, and robust error handling.

---

## 🚀 Development Phases

### Phase 1: Basic Connection Setup
* Basic handshake between client and server.
* Server receives `"Hello Server!"` and responds with `"Hello Client!"`.
* Graceful connection termination.

### Phase 2: Multi-Client Support
* Multithreading integrated on the server side to handle multiple concurrent clients.
* Connection and disconnection events logged with client IP addresses.

### Phase 3: Group Chat & Broadcasting
* Broadcasts messages from any client to all active participants.
* Displays sender IP addresses alongside incoming messages.
* `/exit` command integrated for clean disconnection.

### Phase 4: Graphical Interface & Advanced Features
* Graphical User Interface built with `tkinter`.
* Support for private messaging using `/pm`.
* Display of usernames, timestamps, and active user list via `/list`.
* Comprehensive error handling for network interruptions.

</div>
