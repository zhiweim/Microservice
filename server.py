import socket
import requests
from bs4 import BeautifulSoup
HOST = socket.gethostbyname(socket.gethostname())
PORT = 3256

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()


def get_location_summary(location):
    location = location.replace(' ', '_')
    location = location.title()
    url = 'https://en.wikipedia.org/wiki/' + str(location)
    results = requests.get(url)
    doc = BeautifulSoup(results.text, 'html.parser')
    summary = doc.findAll('p')
    return summary[1].text


while True:
    communication_socket, address = server.accept()
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Location from client: {message}')
    return_msg = get_location_summary(message)
    communication_socket.send(return_msg.encode('utf-8'))