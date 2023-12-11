#!/bin/bash

for file in *.txt;
do
	new_content=$(cat "$file" | tr -cd '[:digit:]')
        echo "$new_content" > "$file"
done

