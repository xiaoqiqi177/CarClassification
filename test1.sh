#！/bin/bash
cd ~/Desktop/test/
i=0
for file in *.jpg
do
  mv "$file" "test-$i.jpg"
  i=$(($i+1))
done

for file in *.jpg
do
  echo ${file%.*} >> test.txt
done
mv test.txt ~/A6L_ACCORD/data/ImageSets/
cp *.jpg ~/A6L_ACCORD/data/Images/

