from socket import *

# Menentukan port server
serverPort = 12000

# Membuat socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind ke port
serverSocket.bind(('', serverPort))

# Server siap menerima koneksi 
serverSocket.listen(1)

# Tampilan Pesan bahwa server siap menerima koneksi
print("Server TCP siap menerima koneksi...")

while True:
    # Menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept()

    # Menerima pesan dari client
    sentence = connectionSocket.recv(2048)

    # Memproses data dengan mengubahnya menjadi huruf besar
    capitalizedSentence = sentence.decode().upper()

    # Mengirim kembali ke client (harus di-encode menjadi bytes)
    connectionSocket.send(capitalizedSentence.encode())

    # Menutup koneksi
    connectionSocket.close()