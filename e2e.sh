#! /bin/bash

file=$1
cp $file /home/qqxiao/Desktop/NEW_DATA/data/Images/
cp $file /home/qqxiao/Desktop/e2e/test_pic/
echo ${file%.*} >> test.txt
mv test.txt /home/qqxiao/Desktop/NEW_DATA/data/ImageSets/

cd /home/qqxiao/Desktop/py-faster-rcnn/
./mytest.sh

cd ../e2e/
cd result_test

mv ../../NEW_DATA/results/test/*.txt .
for part in *.txt
do
	./crop.py $part
done
cd result_pic
l_f=`ls ${I_Path} | wc -l`
if [ "$l_f" -eq "0" ]
then
	echo 'not a car'
	./home/qqxiao/Desktop/e2e/clean.sh
fi

cd ../../ #e2e
./caffetest.sh
./weightadd.py >> ans.txt
./clean.sh
