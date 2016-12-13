#!/bin/sh
objdump -d $1 | grep -v ":    " | grep "  " | sed -e '1,$s/^[^\t]*\t//' | sed -e '1,$s/\t.*$//' | sed -e '1,$s/  .*//' > $1.bin
./hex2str.sh $(echo $(cat $1.bin ) | sed -e 's/ //g') > $1.asc
