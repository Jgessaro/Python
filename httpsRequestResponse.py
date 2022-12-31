# connect to an HTTPS website and output response to txt file as *.txt

import socket
import ssl

# prompt user to enter a website and store as variable
server_hostname = input("Enter a website to connect to: ")

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# wrap the socket in SSL context
ssl_sock = context.wrap_socket(s, server_hostname=server_hostname)

# connect to a webserver
ssl_sock.connect((server_hostname, 443))

# send an HTTPS request
request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(server_hostname)
ssl_sock.send(request.encode())

# receieve and print response
response = ssl_sock.recv(1024).decode()

# writes response to txt file
with open("{}.txt".format(server_hostname), "w") as f:
    f.write(response)

# close socket
ssl_sock.close()
