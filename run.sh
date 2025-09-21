#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

python paragraph.py --output_dir paragraph_bert_0921
python span.py --output_dir span_bert_0921
python paragraph_test.py --model_name_or_path paragraph_bert_0921
python span_test.py --model_name_or_path span_bert_0921