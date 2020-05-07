

export ALBERT_DIR=/Users/mudassar/documents/github/project/cs53-1/albert




python -m run_classifier \
  --data_dir=/Users/mudassar/documents/github/project/cs53-1/albert/datasets/RE/GAD/1 \
  --output_dir=/Users/mudassar/documents/github/project/cs53-1/albert/re_outputs_1 \
  --init_checkpoint=/Users/mudassar/documents/github/project/cs53-1/albert/models/model.ckpt-best \
  --albert_config_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/albert_config.json \
  --spm_model_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/30k-clean.model \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128

  


!python -m gs://cs53-1/RE-task/albert/albert.run_classifier \
  --data_dir=gs://cs53-1/RE-task/albert/albert/datasets/RE/GAD/1 \
  --output_dir=gs://cs53-1/RE-task/albert/albert/re_outputs_1 \
  --init_checkpoint=gs://cs53-1/RE-task/albert/albert/models/model.ckpt-best \
  --albert_config_file=gs://cs53-1/RE-task/albert//albert/models/albert_config.json \
  --spm_model_file=gs://cs53-1/RE-task/albert/albert/models/30k-clean.model \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128


  !python -m run_classifier \
  --data_dir=gs://emudria/cs53-1/albert/datasets/RE/GAD/1 \
  --output_dir=gs://emudria/cs53-1/albert/re_outputs_1 \
  --init_checkpoint=gs://emudria/cs53-1/albert/models/model.ckpt-best \
  --albert_config_file=gs://emudria/cs53-1/albert/models/albert_config.json \
  --spm_model_file=gs://emudria/cs53-1/albert/models/30k-clean.model \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name="GAD" \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128


# To be run in local terminal
python -m run_re \
  --data_dir=/Users/mudassar/documents/github/project/cs53-1/albert/datasets/RE/GAD/1 \
  --output_dir=/Users/mudassar/documents/github/project/cs53-1/albert/re_outputs_2 \
  --init_checkpoint=/Users/mudassar/documents/github/project/cs53-1/albert/models/model.ckpt-best \
  --albert_config_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/albert_config.json \
  --spm_model_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/30k-clean.model \
  --vocab_file=/Users/mudassar/documents/github/project/cs53-1/albert/models/30k-clean.vocab \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128


# To be run in local terminal
python -m run_re \
  --data_dir=/Users/mudassar/documents/github/project/cs53-1/datasets/RE/GAD/1 \
  --output_dir=/Users/mudassar/documents/github/project/cs53-1/re_outputs_2 \
  --init_checkpoint=/Users/mudassar/documents/github/project/cs53-1/models/model.ckpt-best \
  --albert_config_file=/Users/mudassar/documents/github/project/cs53-1/models/albert_config.json \
  --spm_model_file=/Users/mudassar/documents/github/project/cs53-1/models/30k-clean.model \
  --vocab_file=/Users/mudassar/documents/github/project/cs53-1/models/30k-clean.vocab \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128

 # to be run in COLAB
!python -m run_re \
  --data_dir=gs://emudria/albert/datasets/RE/GAD/1 \
  --output_dir=gs://emudria/albert/re_outputs_1 \
  --init_checkpoint=gs://emudria/albert/models/model.ckpt-best \
  --albert_config_file=gs://emudria/albert/models/albert_config.json \
  --spm_model_file=gs://emudria/albert/models/30k-clean.model \
  --vocab_file=gs://emudria/albert/models/30k-clean.vocab \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128

  # to be run in James bucket
  !python -m run_re \
  --data_dir=/content/REData/albert/REData/datasets/RE/GAD/1 \
  --output_dir=/content/REData/albert/REData/outputs/re_outputs_1 \
  --init_checkpoint=/content/REData/albert/REData/models/model.ckpt-best \
  --albert_config_file=/content/REData/albert/REData/models/albert_config.json \
  --spm_model_file=/content/REData/albert/REData/models/30k-clean.model \
  --vocab_file=/content/REData/albert/REData/models/30k-clean.vocab \
  --do_train \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name=GAD \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --save_checkpoints_steps=100 \
  --train_batch_size=128

# Working code in James gs bucket

!python -m run_re \
  --data_dir=gs://cs53-1/REData/datasets/RE/GAD/2 \
  --output_dir=gs://cs53-1/REData/outputs/re_outputs_7 \
  --init_checkpoint=gs://cs53-1/REData/models/bioalbert1.1.1_model.ckpt-best \
  --albert_config_file=gs://cs53-1/REData/models/bioalbert_config.json \
  --spm_model_file=gs://cs53-1/REData/models/30k-clean.model \
  --vocab_file=gs://cs53-1/REData/models/30k-clean.vocab \
  --do_train \
  --do_predict \
  --do_lower_case \
  --max_seq_length=128 \
  --task_name='GAD' \
  --warmup_step=1000 \
  --learning_rate=3e-5 \
  --train_step=10000 \
  --train_batch_size=32 \
  --tpu_name=$TPU_ADDRESS \
  --use_tpu=True \
  --num_train_epochs=10 \
  --save_checkpoints_steps=100 \
  --eval_steps=10