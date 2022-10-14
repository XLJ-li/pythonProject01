from socket import *

server_socket = socket(AF_INET, SOCK_STREAM) # 建立tcp套接字
server_socket.bind(("127.0.0.1",8899)) #本机监听8899
server_socket.listen(5)
print("等待接收连接")
client_socket,client_info = server_socket.accept()
recv_data = client_socket.recv(1024)
print(f"收到的信息来自:{recv_data.decode('gbk')},来自:{client_info}")

client_socket.close()
server_socket.close()