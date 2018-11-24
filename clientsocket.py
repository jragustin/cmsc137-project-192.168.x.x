import socket
import sys
sys.path.append('./proto/')

from threading import Thread
from tcp_packet_pb2 import TcpPacket
from player_pb2 import Player
from pprint import pprint

BUFF = 1024

def main():
	p1 = Player()
	p1.name="Jerico"
	p1.id="137"
	TCP_packets = TcpPacket()

	# pprint(dir(TCP_packets))
	# print(connect.player)
	TCP_packets.type=2
	createLobby = TCP_packets.CreateLobbyPacket()
	createLobby.type = 1
	createLobby.max_players = 3
	# pprint(dir(createLobby))
	s = createLobby.SerializeToString()
	client.send(s)
	mess = client.recv(BUFF)
	print(mess)
	
	


	connect = TCP_packets.ConnectPacket()
	connect.type=1
	connect.player.name="Jerico"
	connect.player.id="1"

	client.send(s)
	mess = client.recv(BUFF)
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
