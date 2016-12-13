#!/bin/sh
CHAINE=$*
CH=$(echo $CHAINE | tr [:upper:] [:lower:])
CH=$(echo $CH | sed -e 's/\\//g')
CH=$(echo $CH | sed -e 's/x//g')
CH=$(echo $CH | sed -e 's/ //g')
CH=$(echo $CH | sed -e 's/\(..\)/\\\\x\1/g')
python -c 'print "'$CH'",'
