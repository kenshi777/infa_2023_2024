#!/bin/bash

read n

for ((i=1; i<=n; i++))
do
	if (($i<=9))
	then

		filename="0$i.txt"
	else
		filename="$i.txt"
	fi
	content=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
	echo $content > $filename
done
