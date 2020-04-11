export ALBERT_MODEL_HUB=https://tfhub.dev/google/albert_base/3
export OUTPUT_DIR="./output_files/"
export TASK="MRPC"
export TASK_DATA_DIR="glue_data"

export DOWNLOAD_PATH="./data_test"
export DOWNLOAD_PATH_TAR="$DOWNLOAD_PATH.tar.gz"

#Get the QA dataset
gdown https://drive.google.com/uc?id=150IEYrHVMprPNpIU0OX2yOfm2-fVRxk1
unzip ./BioASQ-67b-15Oct2019.zip

#Get the "glue_data" test dataset
test -d download_glue_repo || git clone https://gist.github.com/60c2bdb54d156a41194446737ce03e2e.git download_glue_repo
python download_glue_repo/download_glue_data.py --data_dir=$TASK_DATA_DIR --tasks=$TASK

#Run ALBERT on the glue test data without GPU support
!python -m albert.run_classifier \
  --data_dir="glue_data/" \
  --output_dir=$OUTPUT_DIR \
  --albert_hub_module_handle=$ALBERT_MODEL_HUB \
  --spm_model_file="from_tf_hub" \
  --do_train=True \
  --do_eval=True \
  --do_predict=False \
  --max_seq_length=512 \
  --optimizer=adamw \
  --task_name=$TASK \
  --warmup_step=200 \
  --learning_rate=2e-5 \
  --train_step=800 \
  --save_checkpoints_steps=100 \
  --train_batch_size=32 \
  --use_tpu=False
