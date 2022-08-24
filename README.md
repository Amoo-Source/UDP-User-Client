# UDP-User-Client

When both Server.py and Client.py connect, the IP address for client is displayed on server 
with ping counts and on client ping message is sent to server where the server will retrieve the message 
and send it back in uppercase. In the event where the message will timeout, the client will retransmit 
and try again. After a few attempts the packet will be lost and process will continue. At the end of the 
client side a print of the max, min, average, packet loss and packet retransmitted is calculated and 
printed. 
