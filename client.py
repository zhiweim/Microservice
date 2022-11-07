import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3256

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

location = 'phoenix, arizona'
print(f'requesting location information for {location} \n')
socket.send(location.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))