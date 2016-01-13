#！/bin/bash

#train model

cd /home/qqxiao/Desktop/py-faster-rcnn
./tools/train_net.py --gpu 0 --solver models/ZF/faster_rcnn_end2en2/solver.prototxt --weights data/imagenet_models/ZF.v2.caffemodel --imdb new_data_train --iters 70000 --cfg experiments/cfgs/faster_rcnn_end2end.yml
