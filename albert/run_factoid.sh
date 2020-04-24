#!/bin/bash

export BIOASQ_DIR=datasets/QA/BioASQ
export SQUAD_VERSION=v1.1
export ALBERT_DIR=../large-albert
export OUTPUT_DIR=bioasq_out
mkdir -p $OUTPUT_DIR

#export DFILENAME=BioASQ-train-factoid-6b-snippet-2sent.json
export DFILENAME=BioASQ-train-factoid-4b.json
#export PREDICT_FILE=${BIOASQ_DIR}/BioASQ-train-factoid-5b.json
export PREDICT_FILE=${BIOASQ_DIR}/BioASQ-train-factoid-5b.json

# gdown --id 1xADTTjwTogFmnhNU3EPJ86slykoSL4L7 -O large.zip
# unzip large.zip

# setenv PYTHONPATH /home/562/sr1770/.local/lib/python3.7/site-packages

# module load python3
conda activate dspy

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

