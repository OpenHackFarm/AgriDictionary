#!/bin/sh

\rm count.txt
cat *.txt | sort | uniq -c | sort > count.txt
git add count.txt
git commit -m 'Update'
git push
