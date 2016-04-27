gawk -F, -v OFS=',' -v field1=$1 -v size=$2 '$field1 == size {print}'
