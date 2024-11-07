#客户端程序将放置在Windows系统的cmd命令行下运行

from socket import *
import os

serverName = '192.168.186.129'    #指定guest os的IP地址
serverPort = 12000            #指定guest os的12000端口
clientSocket = socket(AF_INET, SOCK_DGRAM)     #调用socket函数，传输层使用udp协议
filename = input('Input the file name you want to send: ')  #输入想要发送的文件名

if not os.path.isfile(filename):               #检查文件是否存在
    print(f"File{filename} does not exist.")
    clientSocket.close()                       #若文件不存在则输出语句并关闭socket进程
    exit()

with open(filename,'rb') as file:
    while True:
        bytes_read = file.read(1024) #读取文件（每次1024字节）
        if not bytes_read:
            break                    #文件读取完毕
        clientSocket.sendto(bytes_read,(serverName,serverPort)) #将读取的文件内容送往对应的guest os的IP地址和端口 

clientSocket.sendto(b'EOF',(serverName,serverPort))  #发送结束信号               
clientSocket.close()          #关闭socket进程