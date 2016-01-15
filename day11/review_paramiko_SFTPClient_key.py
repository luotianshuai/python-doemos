#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'luo_t'
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')

transport = paramiko.Transport(('192.168.7.100',22))
transport.connect(username='root',pkey=private_key) #调用transport进行连接

sftp = paramiko.SFTPClient.from_transport(transport)#然后创建SFTPClient并基于transport连接，把他俩做个绑定!在去连接

sftp.put('testsftpfile.zip','/tmp/newtest-luotianshuai.zip') #将sftpfile.zip上传到目标机器的/tmp/sftpfile-luotianshuai.zip
sftp.get('/tmp/messages.log','shuaige.log') #下载目标服务器/tmp/messages.log 到本地的shuaige.log文件（程序执行目录中）

transport.close()