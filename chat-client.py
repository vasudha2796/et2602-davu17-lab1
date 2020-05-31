import socket
import select
import sys
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Enter Format: clientscript, IP address:port number, Nick")
	exit()
args = str(sys.argv[1].split(':')
ip_addr = str(args[0])
port = int(argv[1])
nick = str(sys.argv[2])
server.connect((ip_addr, port))
MESSAGE = server.recv(1024).decode('utf-8')
print(MESSAGE)
server.sendall(('NICK '+nick).decode('utf-8'))
ok = server.recv(1024).decode('utf-8')

while True:
	sockets_list = [sys.stdin, server]
	read_sockets,write_sockets, error_sockets = select.select(sockets, [], [])
	for sock in read_sockets:
		if sock == server:
			message = sock.recv(2048).decode('utf-8')
			message = message[4:]
			print(message)
		else:
			message = sys.stdin.readline()
			s.sendall(('MESSAGE '+message).encode('utf-8'))
			
						
server.close()
