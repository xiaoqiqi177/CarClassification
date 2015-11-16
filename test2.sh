#！/bin/bash

#test in fast rcnn and crop
cd ~/fast-rcnn/
./tools/test_net.py --gpu 0 --def models/VGG_CNN_M_1024/test.prototxt --net output/default/train/vgg_cnn_m_1024_fast_rcnn_iter_40000.caffemodel --imdb a6l_accord_test
cd ~/end-to-end/

cd result_test
cp ~/A6L_ACCORD/results/test/*.txt .

for file in *.txt
do
  ./crop.py $file
done
cd ../
