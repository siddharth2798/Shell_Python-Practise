input_1=$1
result=$(echo "${input_1}" | bc -l)
printf "%.3f" $result

