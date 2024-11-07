#服务器端程序将放置在Linux系统的虚拟机终端下运行
#在Ubuntu的终端下编入以下代码

from socket import *

serverPort = 12000      #指定guest os的端口
serverSocket = socket(AF_INET,SOCK_DGRAM)   #调用socket函数，传输层使用udp协议
serverSocket.bind(('192.168.186.129',serverPort)) #将套接字和IP与端口绑定
print("The server is ready to receive")

while True:
    file_data = b'' #用于存储接收到的文件数据
    while True:
        data,clientAddress =serverSocket.recvfrom(1024) #接收数据
        if data == b'EOF':
            break           #接收到结束信号，break
        file_data += data   #将接收到的数据累加
    with open('received_file.txt','wb') as f:
        f.write(file_data)                #将接收到的数据依次写入文件
    print("Receive file content:")
    with open('received_file.txt','r',encoding='utf-8') as f:
        content = f.read()
        print(content)          #以文本模式读取并输出文件内容
    serverSocket.sendto('File received successfully',clientAddress)

