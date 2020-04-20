gdown --id 1xADTTjwTogFmnhNU3EPJ86slykoSL4L7 -O albert-large.zip
unzip albert-large.zip

export QA_DIR=qa_data/
export ALBERT_DIR=large_2/

export TASK_NAME=BioASQ
export OUTPUT_DIR=bioasq-processed
mkdir $OUTPUT_DIR

python albert/create_finetuning_data.py \
 --input_data_dir=${GLUE_DIR}/ \
 --spm_model_file=${ALBERT_DIR}/vocab/30k-clean.model \
 --train_data_output_path=${OUTPUT_DIR}/${TASK_NAME}_train.tf_record \
 --eval_data_output_path=${OUTPUT_DIR}/${TASK_NAME}_eval.tf_record \
 --meta_data_file_path=${OUTPUT_DIR}/${TASK_NAME}_meta_data \
 --fine_tuning_task_type=classification --max_seq_length=128 \
 --classification_task_name=${TASK_NAME}
