#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket               # 导入 socket 模块
import threading, time               # 导入 threading 模块

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# s = socket.socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 12345                # 设置端口
# s.bind((host, port))        # 绑定端口

# s.listen(5)                 # 等待客户端连接
# while True:
#     c, addr = s.accept()     # 建立客户端连接。
#     print '连接地址：', addr
#     c.send('欢迎访问菜鸟教程！')
#     c.close()                # 关闭连接

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.1.107', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()