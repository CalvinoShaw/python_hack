import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("AAAABBBBCCCC",(target_host,target_port))
data,addr = client.recv(4096)
print data