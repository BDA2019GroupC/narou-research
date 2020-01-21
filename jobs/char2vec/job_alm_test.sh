python -m narouresearch.jobs.char2vec.train \
 --aozora_path Data/aozora_sentences_by_length \
 --narou_path Data/narou_sentences_by_length \
 --method skipgram \
 --early_stopping 4 \
 --max_epoch 500 \
 --steps 100 \
 --sub_steps 10 \
 --validation_steps 10 \
 --save_dir char2vecLogs_test \
 # --saved_model_dir char2vecLogs_test/20200121_082255