#-*- coding: utf-8 -*-
#!/usr/bin/python
#This script to authentication computes SSH. Computes information needs to write hostlist.txt, per line format for < user > <password> <ip>, can not have blank lines or will be error.
#Script and hostlist.txt are placed on any machine.
#Default port 22.
#The key will be renewed each time when the script runs.
############################################################################
#Need to install paramiko module
#yum install python-devel
#wget http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.tar.gz
#tar -zxvf pycrypto-2.6.tar.gz
#cd pycrypto-2.6/
#python setup.py build && python setup.py install
#wget http://www.lag.net/paramiko/download/paramiko-1.7.7.1.tar.gz
#tar xvzf paramiko-1.7.7.1.tar.gz
#cd paramiko-1.7.7.1/
#python setup.py build && python setup.py install
############################################################################
import commands
import paramiko
import os
import datetime
import threading
import time
#Create key and authentication file。ps: Please check same name in your directory (/home/create_ssh). To avoid accidentally deleted.
def Creat_ssh_key():
	commands.getoutput('rm -rf /home/create_ssh')
	commands.getoutput('mkdir /home/create_ssh')
	commands.getoutput('ssh-keygen -f /home/create_ssh/id_rsa -t rsa -N ""')
	commands.getoutput('cat /home/create_ssh/id_rsa.pub >> /home/create_ssh/authorized_keys')
#copy key and authentication file to the target host.
def Scp_ssh_key(username,password,hostname,local_dir,remote_dir):
	try:
		t=paramiko.Transport((hostname,22))
		t.connect(username=username,password=password)
		sftp=paramiko.SFTPClient.from_transport(t)
		sftp=paramiko.SFTPClient.from_transport(t)
		files=os.listdir(local_dir)
		for f in files:
			if sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f)):
				print '%s Upload file %s to %s success ' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),f,hostname)
			else:
				print '%s Upload file %s to %s error' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),f,hostname)
		t.close()
	except Exception as e:
		print e
		print "Scp file error %s" % hostname
#Target host create folder
def Mkdir_ssh(hostname,password,username):
        try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=hostname,username=username,password=password)
			stdin,stdout,stderr = ssh.exec_command('rm -rf /root/.ssh;mkdir /root/.ssh')
			ssh.close()
        except Exception as e:
			print e
			print "mkdir Connection refused %s" % hostname
#id_rsa file modify permissions to 600
def Chmod_ssh(hostname,password,username):
        try:
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(hostname=hostname,username=username,password=password)
			stdin,stdout,stderr = ssh.exec_command("chmod 600 /root/.ssh/id_rsa;echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config;/etc/init.d/ssh restart")
			ssh.close()
        except Exception as e:
			print e
			print "chmod Connection refused %s" % hostname
if __name__ == '__main__':
	Creat_ssh_key()
	with open('hostlist.txt') as f:
		for i in f.readlines():
			username,password,hostname = i.strip().split()
			mkdir = threading.Thread(target=Mkdir_ssh,args=(hostname,password,username))
			mkdir.start()
	print "Scp file Please later..."
	time.sleep(5)
	with open('hostlist.txt') as f:
		for i in f.readlines():
			username,password,hostname = i.strip().split()
			local_dir = "/home/create_ssh"
			remote_dir = "/root/.ssh"
			scp = threading.Thread(target=Scp_ssh_key,args=(username,password,hostname,local_dir,remote_dir))
			scp.start()
	time.sleep(5)
	with open('hostlist.txt') as f:
		for i in f.readlines():
			username,password,hostname = i.strip().split()
			chmod = threading.Thread(target=Chmod_ssh,args=(hostname,password,username))
			chmod.start()
