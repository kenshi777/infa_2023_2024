#!/bin/bash
gcd ()
{
	a=$1
	b=$2
	while [[ $a -ne 0 ]] && [[ $b -ne 0 ]]
	do
		if [[ $a -gt $b ]]
		then
			let "a%=b"
       		else
			let "b%=a"
		fi
	done
	if [[ $a -eq 0 ]]
	then
		echo "GCD is $b"
	else
		echo "GCD is $a"
	fi
}

while [[ 0 -eq 0 ]]
do
	read n_1 n_2
	if [[ $n_1 == "" ]]
	then
		echo "bye"
		break
	else
		gcd n_1 n_2
	fi
done
