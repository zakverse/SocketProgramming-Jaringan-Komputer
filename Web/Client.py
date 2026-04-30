from socket import *

serverName = "127.0.0.1"
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)

print(f"Mencoba koneksi ke server {serverName}:{serverPort}...")

clientSocket.connect((serverName, serverPort))

print("Koneksi Berhasil")

filePath = input("Input file path (contoh : /index.html) : ")

requestMessage = f"GET {filePath} HTTP/1.1\r\nHost: {serverName}\r\nConnection: close\r\n\r\n"

print(requestMessage)

clientSocket.send(requestMessage.encode())

response = b""

while True:
    data = clientSocket.recv(4096)

    if not data:
        break

    response += data

print("\nFrom server :\n", response.decode(errors='replace'))

clientSocket.close()