from socket import *

# udp的服务端代码
s = socket(AF_INET, SOCK_DGRAM)  # 创建udp类型的套接字
s.bind(("127.0.0.1", 8888))  # 绑定端口，ip可以不写
print("等待接受数据！")
while True:
    recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
    recv_content = recv_data[0].decode('gbk')
    print(f"收到远程信息：{recv_content},from{recv_data[1]}")
    if recv_content == "88":
        print("结束")
        break
s.close()
