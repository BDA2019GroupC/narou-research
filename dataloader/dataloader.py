from narouresearch.utils.io_util import get_all_path

class DataLoader:
  def __init__(self, path):
    self.path = path

  def load_sentence(self, extention=[], exception=[]):
    for path in get_all_path(self.path, extention, exception):
      with open(path) as f:
        for line in f:
          yield line
