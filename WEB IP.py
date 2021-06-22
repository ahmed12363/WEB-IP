import socket
import os
import time
os.system('clear')

os.system("figlet ip web")
print('\033[1;31mwelcome')
v = input('\033[0;34mset the web:')
print('please wait')
time.sleep(4)
print('\033[1;31mDone')
time.sleep(2)
ip = socket.gethostbyname(v)
print(ip)








