#！/bin/bash

#train model
cd ~/fast-rcnn/selective_search/
matlab -nosplash -nodesktop < selective_search_train.m
mv train.mat ~/A6L_ACCORD/.
cd ../
./tools/train_net.py --gpu 0 --solver models/VGG_CNN_M_1024/solver.prototxt --weights data/imagenet_models/VGG_CNN_M_1024.v2.caffemodel --imdb a6l_accord_train
cd ~/end-to-end/

