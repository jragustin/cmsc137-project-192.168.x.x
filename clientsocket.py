import socket
import sys
import os
sys.path.append('./proto/')

from threading import Thread
from tcp_packet_pb2 import TcpPacket
from player_pb2 import Player
from pprint import pprint


BUFF = 1024


	
def menu():
	print("=======MENU=======")
	print("[1]	Create Lobby")
	print("[2]	Join Lobby")
	print("[3]	Exit")




def receive(client,chat):
	# print(chat)
	serverDown = False
	while clientRunning and (not serverDown):
		try:
			r = client.recv(BUFF)
			chat.ParseFromString(r)
			if(chat.type==TCPPackets.CHAT):
				print("\n",chat.player.name, ">",chat.message)
				
			elif(chat.type==TCPPackets.ERR_LDNE):
				print(chat.err_msg)
			elif(chat.type==TCPPackets.ERR_LFULL):
				print(chat.err_msg)
			elif(chat.type==TCPPackets.ERR):
					print(chat.err_msg)

		except Exception as e:
			print(e)
			# print('Server is Down. You are now Disconnected. Press enter to exit...')
			# serverDown = True




if __name__ == '__main__':
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# server = '202.92.144.45'
	server = '202.92.144.45'
	port = 80

	address = (server,port)


	client.connect(address)

	TCPPackets = TcpPacket()

	while True:
		menu()
		choice = int(input("Choice: "))
		if choice==1:
			clientRunning=True
			# TCPPackets.ConnectPacket.type=1
			# TCPPackets.type=TCPPackets.CREATE_LOBBY

			createLobby = TCPPackets.CreateLobbyPacket()
			createLobby.type = TCPPackets.CREATE_LOBBY
			createLobby.max_players=int(input("Max number of players:"))
			# createLobby.max_players=3
			s = createLobby.SerializeToString()
			client.send(s)
			r = client.recv(BUFF)
			#then check the type of the received packet
			#create a ConnectPacket packet with the received lobby_id
			#send ConnectPacket
			#check the type of the received packet
			#make a ChatPacket packet
			#check the type of the received packet
			#make a thread for recv and send
			#disconnect
			createLobby.ParseFromString(r)
			
			if (createLobby.type==TCPPackets.CREATE_LOBBY):
				TCPPackets.type=TCPPackets.CONNECT
				conn = TCPPackets.ConnectPacket()
				conn.type=TCPPackets.CONNECT
				conn.lobby_id=createLobby.lobby_id
				name=input("Player name: ")
				conn.player.name=name
				print("connecting...")
				s = conn.SerializeToString()
				client.send(s)
				r = client.recv(BUFF)

				conn.ParseFromString(r)

				if(conn.type==TCPPackets.CONNECT):
					TCPPackets.type=TCPPackets.CHAT
					chat = TCPPackets.ChatPacket()
					# pprint(chat)
					# os.system("clear")
					print("You've created a chat lobby with the lobby ID of ", conn.lobby_id)

					thread_receive = Thread(target=receive, args=[client,chat])
					thread_receive.start()

					while clientRunning:
						TCPPackets.type=TCPPackets.CHAT
						chat = TCPPackets.ChatPacket()
						chat.type=TCPPackets.type
						chat.player.name = conn.player.name
						chat.player.id = conn.player.id
						chat.message = input()
						if(chat.message.lower()=="quit"): 
							clientRunning=False
							chat.message = "**quit"
							discon = TCPPackets.DisconnectPacket()
							discon.type=TCPPackets.DISCONNECT
							
							s = discon.SerializeToString()
							client.send(s)
							# print("\nYou>", chat.message)
							break
						else:
							# pprint(chat)
							s = chat.SerializeToString()
							client.send(s)
							# print("\nYou>", chat.message)
				elif(conn.type==TCPPackets.ERR_LDNE):
					print(conn.err_msg)
				elif(conn.type==TCPPackets.ERR_LFULL):
					print(conn.err_msg)
				elif(conn.type==TCPPackets.ERR):
					print(conn.err_msg)


					


		elif choice==2:
			# create ConnectPacket packet
			#get the lobby_id
			#get player_id and name
			#send ConnectPacket
			#create ChatPacket packet 
			#check the type of the received packet
			# Disconnect 
			clientRunning=True
			print("connecting...")
			TCPPackets.type=TCPPackets.CONNECT
			conn = TCPPackets.ConnectPacket()
			conn.type=TCPPackets.CONNECT
			conn.lobby_id=input("Enter Lobby ID: ")
			name=input("Player name: ")
			conn.player.name=name
			s = conn.SerializeToString()
			client.send(s)
			r = client.recv(BUFF)

			conn.ParseFromString(r)

			if(conn.type==TCPPackets.CONNECT):
				TCPPackets.type=TCPPackets.CHAT
				chat = TCPPackets.ChatPacket()
				chat.type=TCPPackets.type
				chat.player.name = conn.player.name
				chat.player.id = conn.player.id
				# os.system("clear")
				print("You joined in the lobby ", conn.lobby_id)

				thread_receive = Thread(target=receive, args=[client,chat])
				thread_receive.start()

				while clientRunning:

					chat.type=TCPPackets.type
					chat.player.name = conn.player.name
					chat.player.id = conn.player.id
					chat.message = input()
					
					if(chat.message.lower()=="quit"): 
						clientRunning=False
						chat.message = "**quit"
						discon = TCPPackets.DisconnectPacket()
						discon.type=TCPPackets.DISCONNECT
						print(discon.type)
						s = discon.SerializeToString()
						client.send(s)
						# print("\nYou>", chat.message)
						break
					else:
						s = chat.SerializeToString()
						client.send(s)
						# print("\nYou>", chat.message)
			elif(conn.type==TCPPackets.ERR_LDNE):
				print(conn.err_msg)
			elif(conn.type==TCPPackets.ERR_LFULL):
				print(conn.err_msg)
			elif(conn.type==TCPPackets.ERR):
				print(conn.err_msg)
		else:
			break




