for ip in 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 50 51 52 53 54 55 56
do
echo "working on 10.100.67.$ip"
sshpass -p "P@ssw0rd" ssh -o StrictHostKeyChecking=no root@10.100.67.$ip "ip r | grep -i default"
echo ""
done 

