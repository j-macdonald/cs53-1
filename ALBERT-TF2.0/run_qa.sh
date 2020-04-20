#!/bin/bash

export BIOASQ_DIR=../BioASQ-6b/train/Appended-Snippet
export SQUAD_VERSION=v1.1
export ALBERT_DIR=../large_2/
export OUTPUT_DIR=bioasq_out
mkdir $OUTPUT_DIR

export DFILENAME=BioASQ-train-factoid-6b-snippet-2sent.json
export PREDICT_FILE=../BioASQ-6b/test/Appended-Snippet/BioASQ-test-factoid-6b-snippet-1-2sent.json

setenv PYTHONPATH /home/562/sr1770/.local/lib/python3.7/site-packages
​
module load python3
​
source activate tf2

python3 create_finetuning_data.py \
--squad_data_file=${BIOASQ_DIR}/${DFILENAME} \
--spm_model_file=${ALBERT_DIR}/vocab/30k-clean.model  \
--train_data_output_path=${OUTPUT_DIR}/BioASQ_6b_factoid_snippet_train.tf_record  \
--meta_data_file_path=${OUTPUT_DIR}/bioasq_factoid_snippet_meta_data \
--fine_tuning_task_type=squad \
--max_seq_length=384

python3 run_squad.py \
--mode=train_and_predict \
--input_meta_data_path=${OUTPUT_DIR}/bioasq_factoid_snippet_meta_data \
--train_data_path=${OUTPUT_DIR}/BioASQ_6b_factoid_snippet_train.tf_record \
--predict_file=${PRREDICT_FILE} \
--albert_config_file=${ALBERT_DIR}/config.json \
--init_checkpoint=${ALBERT_DIR}/tf2_model.h5 \
--spm_model_file=${ALBERT_DIR}/vocab/30k-clean.model \
--train_batch_size=8 \
--predict_batch_size=8 \
--learning_rate=1e-5 \
--num_train_epochs=3 \
--model_dir=${OUTPUT_DIR} \
--strategy_type=mirror

