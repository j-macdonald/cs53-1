

export ALBERT_DIR=/Users/mudassar/documents/github/project/cs53-1/albert




!python -m optimization.py \
  --data_dir=/Users/mudassar/documents/github/project/cs53-1/albert/datasets/RE/GAD/1 \
  --output_dir=/Users/mudassar/documents/github/project/cs53-1/albert/re_outputs_1 \
  --init_checkpoint=/Users/mudassar/documents/github/project/cs53-1/albert/models/model.ckpt-best \
  --albert_config_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/albert_config.json \
  --spm_model_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/30k-clean.model \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name="RE" \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128

  # In order to do the CHEMPROT data, we need to add another processor module BIOBERTChemport and then its mapping needs
  ## to be added in the dictionary


!python -m gs://cs53-1/RE-task/albert/albert.run_classifier \
  --data_dir=gs://cs53-1/RE-task/albert/albert/datasets/RE/GAD/1 \
  --output_dir=gs://cs53-1/RE-task/albert/albert/re_outputs_1 \
  --init_checkpoint=gs://cs53-1/RE-task/albert/albert/models/model.ckpt-best \
  --albert_config_file=gs://cs53-1/RE-task/albert//albert/models/albert_config.json \
  --spm_model_file=gs://cs53-1/RE-task/albert/albert/models/30k-clean.model \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name="RE" \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128