#！/bin/bash

cp ../test_pic/* pic_annotated/
for file in ../result_test/*.txt
do
  ./draw_test.py $file 
done
