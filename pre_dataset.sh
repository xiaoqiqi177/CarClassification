#！/bin/bash

#deal with data and place in the right order
cd train_pic
for file in *.jpg
do
  cp $file ~/Desktop/NEW_DATA/data/Images/.
  name=${file%.*}
  echo $name >> /home/qqxiao/Desktop/NEW_DATA/data/ImageSets/train.txt
done

cd ../

for file in train_pic/*.jpg
do
  txt_file="${file%.*}.txt"

  echo "label whole"
  piclabel/piclabel.o $file whole >> $txt_file
  echo
  echo "label front"
  piclabel/piclabel.o $file front >> $txt_file
  echo
  echo "label back"
  piclabel/piclabel.o $file back >> $txt_file
  echo
  echo "label logo"
  piclabel/piclabel.o $file logo >> $txt_file
  echo
  echo "label tire"
  piclabel/piclabel.o $file tire >> $txt_file
  echo
done


for file in train_pic/*.txt
do
  name="${file%.*}"
  ./generate_xml.py $name
  #rm -r $file
  mv $name.xml ~/Desktop/NEW_DATA/data/Annotations/.
done

