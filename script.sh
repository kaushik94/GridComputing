#python benchmarks/classifier.py
echo $1
for ((c=1;c<= $1 ; c++))
do
	echo $c
	$TERM -e "python benchmarks/classifier.py"
done

