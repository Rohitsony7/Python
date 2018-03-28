import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#get local machine name

host = socket.gethostname()

print("HOST name is :{}".format(host))

port = 9999


#bind to the port

serversocket.bind((host, port))

serversocket.listen(5)

print("Waiting for the client's request...")

while True:
    clientsocket, addr = serversocket.accept()

    print("got a connection from %s" %str(addr))

    msg = 'THANK YOU FOR THE REQUEST ' + "\r\n"

    clientsocket.send(msg.encode('ascii'))

    clientsocket.close()

