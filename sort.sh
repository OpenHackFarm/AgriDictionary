cat $1 | sort | uniq > $1.2
mv $1.2 $1
git add $1
