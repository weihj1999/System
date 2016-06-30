for i in `cat 11111.txt`

do

	ssh $i rpm -qa |grep gpfs|wc -l

done
