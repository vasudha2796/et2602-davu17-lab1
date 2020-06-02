import socket
import select
import sys
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Enter Format: clientscript, IP address:port number, Nick")
	sys.exit()

args = str(sys.argv[1].split(':')
ip_addr = str(args[0])
port = int(argv[1])
nick = str(sys.argv[2])
server.connect((ip_addr, port))

message = server.recv(2048).decode('utf-8')
print(message)

server.sendall(('NICK '+nick).encode('utf-8'))
ok_message = server.recv(2048).decode('utf-8')
if re.search('Error', ok_message) or re.search('ERROR', ok_message):
	print(ok_message)
	sys.exit()
print(ok_message)


while True:
	sockets_list = [sys.stdin, server]
	read_sockets,write_sockets, error_sockets = select.select(sockets, [], [])
	for sockets in read_sockets:
		if sockets == server:
			message = sockets.recv(2048).decode('utf-8')
			print(message)
		else:
			message = sys.stdin.readline()
			
			message = 'MSG' + message
			if message == '\n':
				continue
			else:
				server.sendall(message.encode('utf-8'))
			
						
server.close()
