from datetime import datetime
import socket

server_address = ('127.0.0.1', 6789)
max_size = 4096

print('Starting the client', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
client.close()