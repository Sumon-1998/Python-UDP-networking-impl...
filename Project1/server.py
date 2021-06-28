import socket
from datetime import datetime
import time
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
server.settimeout(5)
server.bind(("",2021))
while True:
	date_time=datetime.now()
	time_stamp=date_time.strftime("%d-%b-%Y   %H:%M:%S")
	server.sendto(time_stamp.encode(),('<broadcast>',9001))
	print("Message sent...")
	time.sleep(2)
