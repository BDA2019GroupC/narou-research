from narouresearch.utils.io_util import get_all_path
import os
import shutil

if __name__ == "__main__":
  data_root = "teamDrive/Data/"

  # aozora_source_root = "Data/NarouProject/aozora_sentences_by_length/"
  # aozora_train_root = data_root + "aozora_length/train/"
  # aozora_test_root = data_root + "aozora_length/test/"

  # for path in get_all_path(aozora_source_root):
  #   file = "/".join(path.split("/")[-3:])
  #   if os.path.exists(aozora_test_root+file): 
  #     print("{} is in test".format(file)); continue
  #   if os.path.exists(aozora_train_root+file):
  #     print("{} is in train".format(file)); continue
  #   os.makedirs(aozora_train_root+'/'.join(file.split("/")[:-1]), exist_ok=True)
  #   shutil.copyfile(aozora_source_root+file, aozora_train_root+file)
  #   print(aozora_train_root+file)

  narou_source_root = data_root + "narou_sentences_by_length/"
  narou_train_root = data_root + "narou_length/train/"
  narou_test_root = data_root + "narou_length/test/"

  for path in get_all_path(narou_source_root):
    file = "/".join(path.split("/")[-2:])
    if os.path.exists(narou_test_root+file): 
      print("{} is in test".format(file)); continue
    if os.path.exists(narou_train_root+file):
      print("{} is in train".format(file)); continue
    os.makedirs(narou_train_root+'/'.join(file.split("/")[:-1]), exist_ok=True)
    shutil.copyfile(narou_source_root+file, narou_train_root+file)
    print(narou_train_root+file)