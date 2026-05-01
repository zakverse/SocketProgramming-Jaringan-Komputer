from socket import *

# Menetukan Server
serverName = 'localhost'

# Menentukan Port Server
serverPort = 8080

# Membuat socket TCP(Socket Stream = TCP, Socket Datagram = UDP)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Menghubungkan ke server
clientSocket.connect((serverName, serverPort))

# Mengirim request HTTP GET ke server
request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

# Kirim request ke server
clientSocket.send(request.encode())

# Menerima response dari server
response = clientSocket.recv(1024).decode()

# Menampilkan response dari server
print(response.decode())

# Tutup koneksi
clientSocket.close()