from socket import *

# Menentukan port server
serverPort = 12000

# Membuat socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Mengikat socket ke alamat dan port
serverSocket.bind(('', serverPort))

print("Server UDP siap menerima pesan...")

# Menerima pesan dari client 
while True:
    # Menerima pesan dari client `(buffer size 2048 bytes)
    message, clientAddress = serverSocket.recvfrom(2048)

    # mengubah pesan menjadi huruf besar
    modifiedMessage = message.decode().upper()

    # Mengirim balasan ke client (harus di-encode menjadi bytes)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)