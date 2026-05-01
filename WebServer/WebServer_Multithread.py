# Import Socket Library
from socket import *
# Import Threading Library untuk menangani multiple client
import threading

# Proses untuk menangani setiap client
def handle_client(connectionSocket):
    try:
        # Menerima request dari browser (client) dalam bentuk bytes (decode ke string)
        message = connectionSocket.recv(1024).decode()

        # Mengambil nama file dari request (misalnya: GET /index.html HTTP/1.1)
        filename = message.split()[1]

        # Membuka file yang diinginkan
        f = open(filename[1:], 'r')  # Menghilangkan '/' dari nama file
        outputdata = f.read()

        # Kirim response HTTP header ke client
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode())
        # Kirim isi file ke client
        connectionSocket.sendall(outputdata.encode())

        #Tutup koneksi setelah selesai mengirim response
        connectionSocket.close()

    except:
        # Jika file tidak di temukan atau terjadi error, kirim response 404 Not Found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        connectionSocket.close()

# Setup server socket
serverPort = 8080

# Membuat socket TCP (Socket Stream = TCP, Socket Datagram = UDP)
serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind Socket dengan Alamat dan Port
serverSocket.bind(('', serverPort))

# Server siap menerima koneksi
serverSocket.listen(5)

# Menampilkan pesan bahwa server siap menerima koneksi
print("Web Server Multithread siap menerima koneksi di port", serverPort)

# Loop utama untuk menerima koneksi
while True:
    # Menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    # Membuat thread untuk menangani client
    clientThread = threading.Thread(target=handle_client, args=(connectionSocket,))
    clientThread.start()
