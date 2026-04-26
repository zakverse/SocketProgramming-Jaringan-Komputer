from socket import *

# Menentukan alamat server (localhost) dan port yang digunakan
serverName = 'localhost'
serverPort = 12000

# Membuat socket UDP (SOCK_DGRAM = UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Input pesan dari user
message = input("Masukkan Pesan: ")

# Mengirim Pesan ke server (harus di-encode menjadi bytes) 
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Menerima balasan dari server (buffer size 2048 bytes)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Menampilkan hasil dari server (harus di-decode dari bytes ke string)
print("Balasan dari server: ", modifiedMessage.decode())

# Menutup socket setelah selesai
clientSocket.close()