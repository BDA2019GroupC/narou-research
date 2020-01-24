### 実行
#!/bin/sh
#$ -l q_node=1
#$ -cwd
#$ -l h_rt=16:00:00
#$ -N char2vec
#$ -o out_o.txt
#$ -e out_e.txt
#$ -j y
. /etc/profile.d/modules.sh
module load intel/19.0.0.117 cuda/10.1.105 nccl/2.4.2 cudnn/7.4 python/3.6.5
python -m narouresearch.jobs.char2vec.train \
 --aozora_path teamDrive/Data/aozora_length/train \
 --narou_path teamDrive/Data/narou_length/train \
 --method skipgram \
 --early_stopping 10 \
 --max_epoch 500 \
 --steps 10000 \
 --sub_steps 1000 \
 --validation_steps 1000 \
 --save_dir teamDrive/char2vecLogs