
cat /home/qqxiao/Desktop/e2e/result_test/result_record/record.txt|while read line
do
	parts=($line)
	kind=${parts[2]}
	path=/home/qqxiao/Desktop/e2e/result_test/result_pic/${parts[0]}.jpg
	cd /home/qqxiao/Desktop/caffe/
	echo $kind >> /home/qqxiao/Desktop/e2e/temp.txt
	./.build_release/examples/cpp_classification/my_classification.bin vgg_whole_more/deploy.prototxt /home/models/CNN_models/vgg_$kind\_more.caffemodel  data/vgg_$kind\_8/more_imagenet_mean.binaryproto data/vgg_$kind\_8/synset.txt $path >> /home/qqxiao/Desktop/e2e/temp.txt
done
