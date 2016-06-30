for ip in 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
do
echo "ssh into 10.100.67.$ip"
sshpass -p "P@ssw0rd" ssh -o StrictHostKeyChecking=no root@10.100.67.$ip "localectl set-locale LANG=en_US.utf8"
done 

