python -m narouresearch.jobs.char2vec.train \
 --aozora_path Data/aozora_sentences_by_length \
 --narou_path Data/narou_sentences_by_length \
 --method skipgram \
 --early_stopping 10 \
 --max_epoch 500 \
 --steps 10000 \
 --sub_steps 1000 \
 --validation_steps 1000 \
 --save_dir char2vecLogs