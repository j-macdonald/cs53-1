#!/bin/bash

export BIOASQ_DIR=datasets/QA/BioASQ
export SQUAD_VERSION=v1.1
export ALBERT_DIR=../large-albert/
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

#python create_finetuning_data.py \
#--squad_data_file=${BIOASQ_DIR}/${DFILENAME} \
#--spm_model_file=${ALBERT_DIR}/vocab/30k-clean.model  \
#--train_data_output_path=${OUTPUT_DIR}/BioASQ_6b_factoid_snippet_train.tf_record  \
#--meta_data_file_path=${OUTPUT_DIR}/bioasq_factoid_snippet_meta_data \
#--fine_tuning_task_type=squad \
#--max_seq_length=384

ls ${PREDICT_FILE}


python run_factoid.py \
--mode=train_and_predict \
--input_meta_data_path=${OUTPUT_DIR}/bioasq_factoid_snippet_meta_data \
--train_data_path=${OUTPUT_DIR}/BioASQ_6b_factoid_snippet_train.tf_record \
--predict_file=${PREDICT_FILE} \
--albert_config_file=${ALBERT_DIR}/config.json \
--init_checkpoint=${ALBERT_DIR}/tf2_model.h5 \
--spm_model_file=${ALBERT_DIR}/vocab/30k-clean.model \
--train_batch_size=8 \
--predict_batch_size=8 \
--learning_rate=1e-5 \
--num_train_epochs=2 \
--model_dir=${OUTPUT_DIR} \
--strategy_type=mirror

