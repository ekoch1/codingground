# server.py 
# hosts server for transmitting arduino commands to

#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 10465                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print host

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    while True:
        data = c.recv(1024)
        if data == 'stop' | data == 'stop all':
            break
        else:
            print data
    c.close()                # Close the connection
    print 'Connection with ', addr, ' closed'
    if data == 'stop all':
        break
print 'Server shutting down...'
    