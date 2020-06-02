import socket
import select
import sys
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

if len(sys.argv) != 2:
	print("Enter Format: Server Application ipaddr_s:port")
	sys.exit()

args = str(sys.argv[1].split(':')
ip_addr = str(args[0])
port = int(args[1])
server.bind((ip_addr, port))
server.listen(100)

print('Client connecting ..')

userlist = []
userlist.append(server)
user_templist = []
u_flist = []
user_finallist = {}

def broadcast(message, conn):
	for sockets in u_flist:
		if sockets != conn:
			try:
				sockets.sendall(message.encode('utf_8')
			except:
				sockets.close()
				u_flist.remove(sockets)
				del user_finallist[sockets]
				userlist.remove(sockets)
				
def main():
	print("Server connected on", ip_addr, port)
	while True:
		readsock,writesock,errorsock=select.select(userlist, [],[])
		for sockets in readsock:
			if sockets==server:
				newsockets,addr=server.accept()
				newsockets.sendall('Hello 1'.encode('utf_8'))
				userlist.append(newsockets)
				user_templist.append(newsockets)
				
			elif sockets in user_templist:
				try:
					nick=sockets.recv(1024).decode('utf_8')
					if nick:
						find=re.search(r'NICK\s(\S*)', nick)
						msg=str(find.group(1))
						if len(msg)>12:
							sockets.sendall(' Err: Nicknames should not exceed 12 characters'.encode('utf_8'))
						elif re.search(r'!@#\$', msg)
                            sockets.sendall('Err: No special characters in nick names'.encode('utf_8'))
                        			elif find:
                            				sockets.sendall(('Welcome to chat '+str(msg)).encode('utf_8'))
                            				u_flist.append(sockets)
							user_finallist[sockets]=msg
							user_templist.remove(sockets)
                            
                        			else:
                            				sockets.sendall('Err: Enter correct command NICK <nick>'.encode('utf_8'))
                			else:
						sockets.close()
						user_list.remove(sockets)
						user_templist.remove(sockets)
				except:
					continue
			elif sockets in u_flist:
				try:
					message=sockets.recv(1024).decode('utf_8')
					if message:
						find=re.search(r'MESSAGE\s', message)
					if len(message)>256:
						sockets.sendall('Err: Length of msg should be 256 characters'.encode('utf_8'))
					elif find:
						send_msg='MESSAGE' +str(user_finallist[sockets])+': '+message[4:]
						broadcast(send_msg,sockets)
					else:
						sockets.sendall('Err: Correct command MESSAGE <message>'.encode('utf_8'))
				else:
					sockets.close()
					user_list.remove(sockets)
					u_flist.remove(sockets)
					del user_finalist[sockets]
			except:
				continue

                    
    	server.close()
 if __name__ == "__main__":
    main()
                
