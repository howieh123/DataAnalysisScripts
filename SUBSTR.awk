gawk -F, -v OFS=',' -v field1=$1 -v value1=$2 '{print substr($field1,1,value1),$0}'
