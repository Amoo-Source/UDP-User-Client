

import time
import sys
import socket
from socket import AF_INET, SOCK_DGRAM

serverPort = 12002

#last calculation
def last ():
    print ('Maximum RTT = ', str(max_rtt))
    print ('Minimum RTT = ', str(min_rtt))
    print ('Average RTT = ', str(avg_rtt/10))
    print ('Packet Loss Percentage = ',str(pk_lost/total_packets*100))
    print ('Packet retransmitted = ', str(packets_retransmitted))
    
#UDP socket
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.1", serverPort)
# waiting time of one second for reponse from server
clientSocket.settimeout(1)

min_rtt = 0
max_rtt = 0
avg_rtt = 0.0
packets_retransmitted = 0
pk_lost = 0.0
total_packets = 0.0

# Ping ten times
for i in range(10):
    
    sendTime = time.time()
    message = 'Ping ' + str(i + 1) + ' ' + str(time.strftime("%Y-%m-%d %H:%M:%S"))
    clientSocket.sendto(message.encode(), server_addr)
    recdTime = time.time()
    rtt = recdTime - sendTime
    
    #calculation AVG, MAX & MIN
    if rtt > max_rtt or max_rtt == 0:
      max_rtt = rtt
      
    if rtt < min_rtt or min_rtt == 0:
        min_rtt = rtt
    #run loop for timeout    
    try:
        data, server = clientSocket.recvfrom(1024)
        print (message)
        print ("sever resp: ", data.decode())
        print ("Calculated Round Trip Time =", rtt, "seconds")
        print ()
        
    except socket.timeout:
        
        print (message)
        print ('Request timed out')
        print ('Packet retransmitted')
        
        try:
            packets_retransmitted = packets_retransmitted + 1
            clientSocket.sendto("Retransmitted".encode(), server_addr)
            new_data, server = clientSocket.recvfrom(1024)
            print ("sever resp: ",new_data.decode())
            print ("Calculated Round Trip Time =", rtt, "seconds")
            print ()
            
        except socket.timeout(1):
            clientSocket.sendto("lost".encode(), server_addr)
            new_data, server = clientSocket.recvfrom(1024)
            
            if new_data == 'lost':
                print ('Request timed out')
                print ()
                pk_lost = pk_lost + 1
            else:
                print ("sever resp: ",new_data.decode())
                print ("Calculated Round Trip Time =", rtt, "seconds")
                print ()
            
    total_packets = total_packets + 1
    avg_rtt = avg_rtt + rtt
last ()
