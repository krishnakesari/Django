import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a phone
mysock.connect(('data.pre4e.org', 80)) # dial a phone
cmd = 'GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n' .encode() # dial this web 
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()