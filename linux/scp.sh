for i in `cat 11111.txt`

do
	scp /etc/hosts root@$i:/etc/hosts
		
done

#for i in `cat 11111.txt`

#do
#	ssh $i ifconfig |grep eno1
#done
