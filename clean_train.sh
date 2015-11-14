#！/bin/bash
cd ~/A6L_ACCORD/data
rm -r Annotations/*
rm -r Images/*
rm -r ImageSets/*
cd ../
rm -r train.mat

cd ~/fast-rcnn
rm -r data/cache/*

