from socket import *

# Menentukan alamat server dan port
serverName = 'localhost'
serverPort = 12000

# Membuat socket TCP (SOCK_STREAM = TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Menghubungkan ke server
clientSocket.connect((serverName, serverPort))

# Input pesan
message = input('Masukkan Pesan: ')

# Kirim pesan
clientSocket.send(message.encode())

# Terima balasan
modifiedMessage = clientSocket.recv(1024)

# Tampilkan hasil
print('Balasan dari Server:', modifiedMessage.decode())

# Tutup koneksi
clientSocket.close()
