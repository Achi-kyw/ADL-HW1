#!/bin/bash

# export CUDA_VISIBLE_DEVICES=2

# python paragraph.py --output_dir paragraph_no_train
# python span.py --output_dir span_no_train

#unzip paragraph_lert.zip
#unzip span_lert.zip

python paragraph_test.py --model_name_or_path paragraph_lert --validation_file ${2} --context_file ${1} --predict_output_dir test_span.json
python span_test.py --model_name_or_path span_lert --predict_output_dir ${3} --test_file test_span.json