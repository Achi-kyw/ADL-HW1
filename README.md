# ADL-HW1

## Run

```
bash ./download.sh
bash ./run.sh /path/to/context.json /path/to/test.json /path/to/pred/prediction.csv
```

Note that download.sh does not include the unzip command due to the limitation of homework. You should unzip the file by yourself if you do not execute run.sh.

## Environment

To execute, you should create a conda environment first

```
conda create python=3.10 -n adl_hw1
conda activate adl_hw1
pip install -r requirements.txt
```

## Train

Before training, you should process data to fit `span.py`

```
python process_data.py
```
Then, you should have `context.json`, `valid.json`, `train.json`, `test.json`, `valid_span.json`, `train_span.json`

You can setup your own configuration if needed

```
python paragraph.py --output_dir paragraph_lert
python span.py --output_dir span_lert
```

## Test

```
python paragraph_test.py --model_name_or_path paragraph_lert --predict_output_dir test_span.json
python span_test.py --model_name_or_path span_lert --predict_output_dir predict.csv --test_file test_span.json
```