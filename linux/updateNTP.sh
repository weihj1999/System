for ip in 51 52 53 54 55 56
do
echo "working on 10.100.66.$ip"
sshpass -p "P@ssw0rd" ssh -o StrictHostKeyChecking=no root@10.100.66.$ip "sed -i 's/0.rhel.pool.ntp.org/10.100.66.111/g' /etc/ntp.conf"
echo ""
done 

