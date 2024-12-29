import socket

## THIS SERVER CODE IS ONLY MEANT FOR TESTING THE CLIENT CODE, BUT IS NOT THE MAIN SERVER CODE FOR THE PROJECT


serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

print("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Connection established")
    message = connectionSocket.recv(1024).decode()
    print(f"Message received: {message}")
    connectionSocket.send("Message received".encode())
    connectionSocket.close()
    print("Connection closed")
print(message)

