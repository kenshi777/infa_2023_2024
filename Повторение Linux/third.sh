#!/bin/bash

read target_digit

for file in *.txt;
do
	max_digit=$(grep -o '[0-9]' "$file" | sort -rn | head -n 1)
        if [ "$max_digit" = "$target_digit" ];
       	then
            mv "$file" "${file%.*}.log"
        fi
done

