#!/bin/bash

N=5

for ((i=0;i<N;i++))
do
   for ((j=0;j<N;j++))
   do
      k=$((i*N + j))
      printf "%d\t" $k
   done
   printf "\n"
done
