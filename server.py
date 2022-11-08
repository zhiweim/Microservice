import socket
import requests
from bs4 import BeautifulSoup
HOST = socket.gethostbyname(socket.gethostname())  # getting the current host name for the socket
PORT = 3256  # any arbitrary port number should work, as long as the client and server are connected/binded to the same one

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()


def get_location_summary(location):
    """
    The actual microservice; the summary from wikipedia is scraped using the request module and BeautifulSoup.
    """
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