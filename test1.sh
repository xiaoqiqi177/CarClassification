#！/bin/bash

#place pictures, selective_search for test pictures
cd test_pic
for file in *.jpg
do
  echo ${file%.*} >> test.txt
  cp $file ~/A6L_ACCORD/data/Images/.
done
mv test.txt ~/A6L_ACCORD/data/ImageSets/.

cd ~/fast-rcnn/selective_search/
matlab -nosplash -nodesktop < selective_search_test.m
mv test.mat ~/A6L_ACCORD/.
cd ../

