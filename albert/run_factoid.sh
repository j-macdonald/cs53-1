#!/bin/bash

mkdir -p datasets/QA

gdown --id 1-KzAQzaE-Zd4jOlZG_7k7D4odqPI3dL1 -O datasets/QA/bioasq67.zip
unzip datasets/QA/bioasq67.zip -d datasets/QA/

export BIOASQ_DIR=datasets/QA/BioASQ-6b
export SQUAD_VERSION=v2.0
export ALBERT_DIR=../large-albert
export OUTPUT_DIR=bioasq_out_factoid
mkdir -p $OUTPUT_DIR

export DFILENAME=train/Appended-Snippet/BioASQ-train-factoid-6b-snippet-2sent.json
export PREDICT_FILE=${BIOASQ_DIR}/train/Snippet-as-is/BioASQ-train-factoid-6b.json


python run_factoid.py \
       --albert_config_file=${ALBERT_DIR}/assets/albert_config.json \
       --output_dir=${OUTPUT_DIR} \
       --train_file=${BIOASQ_DIR}/${DFILENAME} \
       --predict_file=${PREDICT_FILE} \
       --vocab_file=${ALBERT_DIR}/assets/30k-clean.vocab \
       --do_train=True \
       --do_predict=True \
       --train_batch_size=8 \
       --init_checkpoint=${ALBERT_DIR}/variables/variables

