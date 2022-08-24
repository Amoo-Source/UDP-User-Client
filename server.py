

import random
import sys
from socket import *

localIP = "127.0.0.1"
server_port = 12002
#UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#  IP address and port number to socket
serverSocket.bind((localIP, server_port))

sequence_number = 1


while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    array = message.split(b' ')
    array_type = array[0]
    array_seq = str(array[1])
    clientIP  = "Connection from message{}".format(address) + " message " + str(sequence_number)
    #clientIP  = "Connection from message{}".format(address) + " message " + str(array[1])
    print(clientIP)
    sequence_number = sequence_number + 1
    # Capitalize the message from the client
    message = message.decode().upper()
    
    # If rand is less is than 3, we consider the packet lost
    if rand <= 3:
        retransmit_message, (ip, port) = serverSocket.recvfrom(1024)
        
        if retransmit_message == b'Retransmitted':
            print(clientIP)
            
        elif retransmit_message == b'lost':   
            serverSocket.sendto(retransmit_message.encode(), address) 
            print(clientIP)
            
        else:
            print(clientIP)
            
    else:
        print(clientIP)

    # Otherwise, the server responds
    serverSocket.sendto(message.encode(), address)
