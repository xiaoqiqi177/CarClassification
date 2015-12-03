#！/bin/bash
r_accu='0.10'
for ((a=0;a<=1000;a++))
do
  aa=$((1000-$a))
  for ((b=0;b<=$aa;b++))
  do
	bb=$(($aa-$b))
  	for ((c=0;c<=$bb;c++))
	do
	  cc=$(($bb-$c))
	  for ((d=0;d<=$cc;d++))
	  do
		e=$(($cc-$d))
		./calculate.py $a $b $c $d $e >> tmp.txt
		line=$(tail -1 tmp.txt)
		accu=${line:11}
		rm -r tmp.txt
		if [ "$accu" \> "$r_accu" ]
		then
		  	echo $accu
	  		r_accu=$accu
			r_a=$a
			r_b=$b
			r_c=$c
			r_d=$d
			r_e=$e
			echo $accu
		fi
	  done
	done
  done
done

echo $r_a
echo $r_b
echo $r_c
echo $r_d
echo $r_d
