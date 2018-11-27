import socket
import sys
sys.path.append('./proto/')

from threading import Thread
from tcp_packet_pb2 import TcpPacket
from player_pb2 import Player
from pprint import pprint

BUFF = 1024


def establishConnect(tcppacket):
	connect = tcppacket.ConnectPacket()
	connect.type = tcppacket.type
	connect.player.name="Jerico"
	connect.player.id=1


def main():
	p1 = Player()
	p1.name="Jerico"
	p1.id="137"

	TCP_packets = TcpPacket()
	

	while True:
		menu()
		choice = int(input("Choice: "))
		if choice==1:
			# TCP_packets.ConnectPacket.type=1
			# TCP_packets.type=TCP_packets.CREATE_LOBBY

			createLobby = TCP_packets.CreateLobbyPacket()
			createLobby.type = TCP_packets.CREATE_LOBBY
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
			print(createLobby.lobby_id)
			# pprint(dir(mess))
			if (createLobby.type==2):
				print("connecting...")
				TCP_packets.type=TCP_packets.CONNECT
				conn = TCP_packets.ConnectPacket()
				conn.type=TCP_packets.CONNECT
				conn.lobby_id=createLobby.lobby_id
				conn.player.name=input("Player name: ")
				s = conn.SerializeToString()
				client.send(s)
				r = client.recv(BUFF)

		elif choice==2:
			# create ConnectPacket packet
			#get the lobby_id
			#get player_id and name
			#send ConnectPacket
			#create ChatPacket packet 
			#check the type of the received packet
			# Disconnect 
			pass
		else:
			break


	# print("hey")
	# connect = TCP_packets.ConnectPacket()
	# connect.type=1
	# connect.player.name="Jerico"
	# connect.player.id="1"

	# pprint(dir(TCP_packets))
	# print(connect.player)
	# TCP_packets.type=
	# createLobby = TCP_packets.CreateLobbyPacket()
	# createLobby.type = 0
	# createLobby.max_players = 3
	# pprint(dir(createLobby))
	# s = createLobby.SerializeToString()
	# client.send(s)
	# mess = client.recv(BUFF)
	# print(mess)
	
	
	# client.send(s)
	# mess = client.recv(BUFF)
	# TCP_packets.type=1
	""" while True:
		menu()
		choice = int(input("Choice: "))
		if choice==1:
			# TCP_packets.ConnectPacket.type=1

			if (TCP_packets.type==1):
				TCP_packets.ConnectPacket.type=TCP_packets.type
				print(TCP_packets.ConnectPacket)
				TCP_packets.ConnectPacket.player=player
		elif choice==2:
			pass
		else:
			break

 """




	# print(client)

	# msg = client.recv(1024)

	# client.close()

	# print(msg.decode('ascii'))

def menu():
	print("=======MENU=======")
	print("[1]	Create Lobby")
	print("[2]	Join Lobby")
	print("[3]	Exit")

if __name__ == '__main__':
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# server = '202.92.144.45'
	server = '202.92.144.45'
	port = 80

	address = (server,port)


	client.connect(address)


	main()
