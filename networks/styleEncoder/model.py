import torch
import torch.nn as nn
import torch.nn.functional as F

class styleEncoder(nn.Module):
	def __init__(self, input_size, hidden_size):
