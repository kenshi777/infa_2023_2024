#!/bin/bash
calculate ()
{
	c=0
	if [[ $2 == "+" ]]
	then
		let "c=$1+$3"
		return "$c"
	elif [[ $2 == "-" ]]
	then
		let "c=$1-$3"
		return "$c"
	elif [[ $2 == "*" ]]
	then
		let "c=$1*$3"
		return "$c"
	elif [[ $2 == "/" ]]
	then
		let "c=$1/$3"
		return "$c"
	elif [[ $2 == "%" ]]
	then
		let "c=$1%$3"
		return "$c"
	elif [[ $2 == "**" ]]
	then
		let "c=$1**$3"
		return "$c"
	fi
}

while [ True ]
do
	read n_1 n_2 n_3
	if [[ $n_1 == "exit" ]]
	then
		echo "bye"
		break
	fi
	s=`calculate $n_1 "$n_2" $n_3`
	if [[ $s == "error" ]]
	then
		echo $s
		break
	fi
done

