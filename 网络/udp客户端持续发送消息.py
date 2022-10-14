from socket import *

# udp的客户端发送代码
s = socket(AF_INET, SOCK_DGRAM)  # 创建udp类型的套接字
addr = ("127.0.0.1", 8888)

while True:
    data = input("请输入：")
    s.sendto(data.encode("gbk"),addr)
    if data == "88":
        print("结束")
        break

s.close()
