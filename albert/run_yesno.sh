#!/bin/bash

export BIOASQ_DIR=datasets/QA/BioASQ-
export SQUAD_VERSION=v1.1
export ALBERT_DIR=../large-albert
export OUTPUT_DIR=bioasq_out_yesno
rm -rf ${OUTPUT_DIR}
mkdir -p $OUTPUT_DIR

export DFILENAME=6b/train/Appended-Snippet/BioASQ-train-yesno-6b-snippet-2sent.json
export PREDICT_FILE=${BIOASQ_DIR}7b/train/Appended-Snippet/BioASQ-train-yesno-7b-snippet-2sent.json

python run_yesno.py \
       --albert_config_file=${ALBERT_DIR}/assets/albert_config.json \
       --output_dir=${OUTPUT_DIR} \
       --train_file=${BIOASQ_DIR}${DFILENAME} \
       --predict_file=${PREDICT_FILE} \
       --vocab_file=${ALBERT_DIR}/assets/30k-clean.vocab \
       --do_train=True \
       --do_predict=True \
       --train_batch_size=8 \
       --init_checkpoint=${ALBERT_DIR}/variables/variables

