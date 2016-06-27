#!/bin/bash
len=1000
file=""
for f in $(ls /etc/init -p|grep -v /)
do
	#ls "/etc/init/"$f
	lenn=$(cat "/etc/init/"$f|wc -m)
	#echo $lenn
	if [ "$lenn" -lt "$len" ]
		then
			len=$lenn
			file=$f
	fi
done
echo $len
echo "/etc/init/"$f
cat "/etc/init/"$f
