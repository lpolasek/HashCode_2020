#!/bin/bash
for f in [a-f]*.txt
do
	echo $f
	cat $f | python3 book_scanning.py > $( echo $f | cut -f 1 -d . ).out
done
