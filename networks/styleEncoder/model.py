import torch
import torch.nn as nn
import torch.nn.functional as F
from narouresearch.dataloader.dataloader import RandomPathGenerator

class StyleEncoder(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size):
        super(StyleEncoder, self).__init__()
        self.embedding = weights[0]
        self.embLinear = weights[1]
        if method == "RNN":
            self.RNN   = nn.RNN(hidden_size, hidden_size, num_layers=2, 
                                dropout=0.2, batch_first=True, bidrectional=True)
        if method == "Transformer": pass

    def forward(self, seqs, hidden=None):
        embedding = self.embedding(seqs)
        hidden = self.RNN(embedding, hidden)
        return hidden

class TimeStyleEncoder(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size):
        super(TimeStyleEncoder, self).__init__()
        self.hidden_size = hidden_size
        self.encoder = StyleEncoder(weights, method, input_size, hidden_size)
        self.mean = nn.Linear(hidden_size, output_size)
        self.std = nn.Linear(hidden_size, output_size)
        if method == "RNN":
            self.forward = self.forwardRNN

        def forwardRNN(self, batch, hidden=None):
	        for t in range(batch.shape[1]): # sirannzo
	            hidden = self.encoder(batch[:,t,:], hidden)
	        mean = self.mean(hidden)
	        std = self.std(hidden)
			return mean + std * torch.randn((self.hidden_size,))

class StyleDisperser(nn.Module):
    def __init__(self, weights, path_size, ):
        super(StyleDisperser, self).__init__()
        self.encoder = TimeStyleEncoder(weights, input_size, hidden_size, method)

    def forward(self, batch, same=32):
        ret_z = self.encoder(batch)
        true_z, random_z = ret_z[:same], ret_z[same+1:]
		true_mean = torch.mean(true_z)
		true_std = torch.std(true_z)
		loss = true_std + torch.pow((random_z-true_mean),2).sum()
		return loss
		
