#!/bin/bash
#####################################################
#					IMPORTANT						#
# THIS IS A AUTOTEST TOOL TO AUTOTEST THE CNN MODELS#
# 													#
# ALL MODELS CHOSEN ARE ***_iter_40000.caffemodel	#
# IF YOU NEED TO MODIFY THE NAME OF EACH MODELS 	#
# PLEASE ADD AN ARRAY TO DESCRIBE IT 				#
#													#
# ZIYANG XU											#
# PKU-CECA											#
# 2015.11.28										#
#####################################################

# format of input file:
#	back_3 a6l102 back 0.697
#	back_4 a6l107 back 0.985
#	back_5 a6l108 back 0.999
#	back_6 a6l108 back 0.957


### BEGIN OF PARAMETERS

#init
number=0
not_test_num=0
correct_number=0

#number of categories
NAMELIST_NUM=5
#NAMELIST_NUM=1
NAMELIST=(new_frontLight new_backLight new_tire logo new_whole)
#NAMELIST=(logo)
SHORT_NAMELIST=(front back tire logo whole)
#SHORT_NAMELIST=(logo)

#high_probability
#NEED TO MODIFY IF NAMELIST_NUM HAS CHANGED

high_probability=0
#high_probability_correct_num=(0 0 0 0 0)
high_probability_correct_num=(0)
#high_probability_num=(0 0 0 0 0)
high_probability_num=(0)
#Environment variables
HOMEPATH=/home/qqxiao/caffe
TESTDATA=/home/qqxiao/e2e/result_test/result_pic
BINPATH=$HOMEPATH/examples/cpp_classification/classification.bin

INPUT_FILENAME=result_test/result_record/record.txt
OUTPUT_FILENAME=all_verbose_result_0.8.txt


#THRESHOLD
#total_accuracy calculated by
#total_accuracy = cnn_accuracy * rcnn_accuracy
THRESHOLD=0.8

#OTHER PARAMETERS
OUTPUT_INTERVAL=50

### END OF PARAMETERS
### BEGIN OF INIITIALIZATION
if [ -f $HOMEPATH/$OUTPUT_FILENAME ]
then
	rm $HOMEPATH/$OUTPUT_FILENAME
fi
### END OF INIITIALIZATION

### BEGIN OF MAIN PART
while read result_name father_name category accuracy
do
	#echo $category
	# PARSE father name to get the model category
	if [[ ${father_name:0:1} == 't' ]]
		then model="TEST"
	elif [[ ${father_name:0:2} == 'ac' ]]
		then model="ACCORD"
	else model="A6L"
	fi
	#echo $model
	cd $TESTDATA
	var=${result_name}.jpg

	for (( i=0; i<$NAMELIST_NUM; i++ ))
	do
	#	echo "in"
	    if [[ $category == ${SHORT_NAMELIST[i]} ]]
	    then
	        number=$[$number+1]
			NAME=${NAMELIST[i]}
	        DATA=data/$NAME
	        echo $number ':' $var ${SHORT_NAMELIST[i]}  
	        output=`$BINPATH $HOMEPATH/$NAME/deploy.prototxt $HOMEPATH/$NAME/${NAME}.caffemodel $HOMEPATH/$DATA/imagenet_mean.binaryproto $HOMEPATH/$DATA/synset.txt $var`
			prediction=`echo $output | cut -d ' ' -f 1`
			predict_accu=`echo $output | cut -d ' ' -f 2`
			probability=`echo "scale=3;$predict_accu*$accuracy"|bc|awk '{printf "%.2f", $0}'`
			echo Prediction:$prediction Actual:$model Predicite_Accu:$predict_accu Cut_Accu:$accuracy Probability: $probability
			if [[ $model != "TEST" ]]
			then
				not_test_num=$[$not_test_num+1]
				if [ $(echo "$probability >$THRESHOLD"|bc) -eq 1 ]
				then
					high_probability_num[i]=$[${high_probability_num[i]}+1]	
					high_probability=1;
				fi

				if [[ $prediction == $model ]]
				then
					echo -e "CORRECT\n"
					correct_num=$[$correct_num+1]
					if [[ $high_probability -eq 1 ]]
					then
						high_probability_correct_num[i]=$[${high_probability_correct_num[i]}+1]
					fi
				else
					echo -e  "WRONG\n"
				fi
				high_probability=0;
			else
				echo -e "TEST: DON'T KNOW RIGHT OR WRONG\n"	
			fi

		fi

	done

done<$INPUT_FILENAME >> $HOMEPATH/$OUTPUT_FILENAME
#done<$INPUT_FILENAME
### END OF MAIN PART
