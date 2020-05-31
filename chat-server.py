import socket
import select
import sys
import re

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
if len(sys.argv) != 2:
	print("Enter Format: Server Application ipaddr_s:port")
	sys.exit(1)
args = str(sys.argv[1].split(':')
ip_addr = str(args[0])
port = str(args[1])
server.bind((ip_addr, port))
server.listen(100)

userlist = []
user_templist = []
u_list = {}

def broadcast(message, conn):
	for users in userlist:
		if users != conn:
			try:
				users.send(message)
			except:
				users.close()
				userlist.remove(users)
				
def main():
	print("Server connected on", ip_addr, port)
	while True:
		readsock,writesock,errorsock=select.select(userlist, [],[])
		for users in readsock:
			if users==server:
				newuser,addr=server.accept()
				newuser.sendall('Hello'.encode('utf_8'))
				userlist.append(newuser)
				user_templist.append(newuser)
				
			elif users in user_templist:
				try:
					nick=users.recv(1024).decode('utf_8')
					if nick:
						find=re.search(r'NICK\s(\S*)', nick)
						msg=str(find.group(1))
						if len(msg)>12:
							users.sendall(' Nicknames should not exceed 12 characters')
						elif re.search(r'!@#$\' msg)
                            				users.sendall('No special characters in nick names'.encode('utf_8'))
                        		elif find:
                            			users.sendall(('Welcome to chat '+str(msg)).encode('utf_8'))
                            			u_list[users]=msg
                            			user_templist.remove(users)
                        		else:
                            			users.sendall('Enter command NICK <nick>'.encode('utf_8'))
					else:
						users.close()
						userlist.remove(users)
						user_templist.remove(users)
                			except:
                    				continue

				elif users in u_list:
					try:
						msg=users.recv(1024).decode('utf_8')
						if msg:
							find=re.search(r'@#%/\s',msg)
							if len(msg)>256:
								users.sendall('Message should be 256 characters limit'.encode('utf_8'))
							elif find:
								msg_s = 'MSG '+str(u_list[users]+': '+msg[4:]
								broadcast(msg_s, users)
							else:
								users.sendall('Enter MSG <msg>'.encode('utf_8'))
							else:
								users.close()
								userlist.remove(users)
								del u_list[users]
							except:
								continue
				server.close()
if __name__ == "__main__":
	main()

                    	
    server.close()
 if __name__ == "__main__":
    main()
                
