#!/bin/bash

awk -F ';' 'NR>1 {e[$1]=$3; s=s+$3} END{avg=s/(NR-1); c=0;
 for(x in e) if(e[x] <avg) c++; print c}' $1

echo "$*" 
