import socket
from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(BUFFER_SIZE).decode()

        #GET /file.html HTTP/1.1
        if not message or len(message.split()) < 2:
            print("[WARNING] Received empty or malformed HTTP Request")
            connectionSocket.close()
            return
        
        print(message)

        filename = message.split()[1]
        f = open(filename[1:], 'r', encoding="UTF-8")
        outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send(f"filename: {filename}\r\n".encode())
        connectionSocket.send("\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())

        error_message = "<html><head><title>404 Not Found</title></head>" \
                        "<body><h1>404 Not Found</h1><p>The requested file was not found on this server.</p></body></html>"
        connectionSocket.send(error_message.encode())
        connectionSocket.close()

SERVER_IP = "192.168.1.40"
SERVER_PORT = 6789
BUFFER_SIZE = 4096

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((SERVER_IP, SERVER_PORT))
serverSocket.listen(5)

print(f"[SERVER] Web Server is running on {SERVER_IP}:{SERVER_PORT}")
print("[SERVER] waiting for connection...")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"[SERVER] connection from {addr}")

    client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))

    client_thread.start()