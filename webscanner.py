os.system('clear')
os.system('pip install pyfiglet')
os.system('clear')
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Website Scanner'))
print('By Yosif')
print('')
import os
import socket
import time
USER = input("[+]Enter Website: ")
time.sleep(0.3)
print("")
print("[+]Please Wait")
print("")
time.sleep(2)
ip = socket.gethostbyname(USER)
print(ip)
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('by yosif'))








