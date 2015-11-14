#！/bin/bash

cd ~/A6L_ACCORD/data/Images/
for file in a*.jpg
do
  echo ${file%.*} >> test.txt
done
mv test.txt ../ImageSets/.

cd ~/fast-rcnn/selective_search/
matlab -nosplash -nodesktop < selective_search_test.m
mv test.mat ~/A6L_ACCORD/.
cd ../
./tools/test_net.py --gpu 0 --def models/VGG_CNN_M_1024/test.prototxt --net output/default/train/vgg_cnn_m_1024_fast_rcnn_iter_40000.caffemodel --imdb a6l_accord_test
cd ~/end-to-end/

mkdir -p test_data
cd test_data
cp -r ~/A6L_ACCORD/results/test result_test
cp ~/A6L_ACCORD/data/ImageSets/test.txt .
mkdir -p test_pic
for file_i in $(cat test.txt)
do
  cp ~/A6L_ACCORD/data/Images/$file_i.jpg test_pic
done
cd ../
mkdir -p result_pic
for file in test_data/result_test/*
do
  ./crop.py $file
done
