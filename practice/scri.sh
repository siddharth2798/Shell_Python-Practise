#!/bin/bash

echo 'enter n'
read n

i=1
sumeven=0
sumodd=0

while [ $i -le $n ]
do

echo 'enter numbers'
read num

if [ `expr $num % 2` -ne 0 ]
then
sumodd=`expr $sumodd + $num`
else
sumeven=`expr $sumeven + $num`
fi

i=`expr $i + 1`

done

echo 'Sum odd is :' $sumodd
echo 'Sum even is:' $sumeven
