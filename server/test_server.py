#servidor TCP falso

import codecs

import socket as sck
import time

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21568
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         # connections are full, others will be rejected.


def loop():
    while True:
        print('Waiting for connection...')
        # Waiting for connection. Once receiving a connection, the function accept() returns a separate 
        # client socket for the subsequent communication. By default, the function accept() is a blocking 
        # one, which means it is suspended before the connection comes.
        tcpCliSock, addr = tcpSerSock.accept() 
        print('...connected from :', addr)     # Print the IP address of the client connected with the server.

        while True:
            data = ''
            data = codecs.decode(tcpCliSock.recv(BUFSIZ))    # Receive data sent from the client. 
            # Analyze the command received and control the car accordingly.
            if not data:
                break
            if data == ctrl_cmd[0]:
                print('motor moving forward')

            elif data == ctrl_cmd[1]:
                print('recv backward cmd')

            elif data == ctrl_cmd[2]:
                print('recv left cmd')

            elif data == ctrl_cmd[3]:
                print('recv right cmd')

            elif data == ctrl_cmd[6]:
                print('recv home cmd')

            elif data == ctrl_cmd[4]:
                print('recv stop cmd')

            elif data == ctrl_cmd[5]:
                print('read cpu temp...')
                temp = 0 #cpu_temp.read()
                tcpCliSock.send('[%s] %0.2f' % (time.ctime(), temp))

            elif data == ctrl_cmd[8]:
                print('recv x+ cmd')

            elif data == ctrl_cmd[9]:
                print('recv x- cmd')

            elif data == ctrl_cmd[10]:
                print('recv y+ cmd')

            elif data == ctrl_cmd[11]:
                print('recv y- cmd')

            elif data == ctrl_cmd[12]:
                print('home_x_y')

            elif data[0:5] == 'speed':     # Change the speed
                print(data)

            elif data[0:5] == 'turn=':	#Turning Angle
                print('data =', data)

            elif data[0:8] == 'forward=':
                print('data =', data)

            elif data[0:9] == 'backward=':
                print('data =', data)

            else:
                print('Command Error! Cannot recognize command: ' + data)


def close():
    tcpSerSock.close()


if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		close()