read x
read y

i=`expr $x + $y`
j=`expr $x - $y`
k=`expr $x \* $y`
l=`expr $x / $y`
echo "$i"
echo "$j"
echo "$k"
echo "$l"
