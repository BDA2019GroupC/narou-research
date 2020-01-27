import torch
import torch.nn as nn
import torch.nn.functional as F
from narouresearch.networks.char2vec.model import Embedding

class StyleEncoder(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size):
        super(StyleEncoder, self).__init__()
        self.output_size = output_size
        self.embedding = Embedding(input_size,128)
        # self.embedding.load_state_dict(torch.load(PATH))
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "GRU":
            self.forward = self.forwardGRU
            self.GRU = nn.GRU(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "Transformer":
            self.forward = self.forwardTransformers
            d_model = 512
            nhead = 8
            num_encoder_layers = 6
            dim_feedforward=2048
            dropout=0.1
            activation="relu"
            encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation)
            encoder_norm = nn.LayerNorm(d_model)
            self.Transformer = nn.TransformerEncoder(encoder_layer, num_encoder_layers, encoder_norm)
            self.catter = nn.Linear()

    def forwardRNN(self, seqs):
        embedding = self.embedding(seqs)
        output_, _ = self.RNN(embedding)
        output = torch.sum(output_[:,-1,:].view(output_.shape[0],self.output_size,-1), dim=2)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

    def forwardGRU(self, seqs):
        embedding = self.embedding(seqs)
        output_, _ = self.GRU(embedding)
        output = torch.sum(output_[:,-1,:].view(output_.shape[0],self.output_size,-1), dim=2)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

    def forwardTransformers(self, seqs):
        embedding = self.embedding(seqs)
        output_ = self.Transformer(embedding)
        output = output_.mean(dim=1)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

class StyleDisperser(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size, device, margin=0.7):
        super(StyleDisperser, self).__init__()
        self.encoder = StyleEncoder(weights, method, input_size, hidden_size, output_size)
        self.margin = margin
        self.device = device

    def forward(self, batch, same=32):
        ret_z = self.encoder(batch)
        true_z, random_z = ret_z[:same], ret_z[same:]
        true_mean_ = torch.mean(true_z, dim=0)
        true_mean = true_mean_/torch.norm(true_mean_)
        true_std = 1. -(torch.mv(true_z,true_mean.T)).mean()
        random_std_m = -self.margin + torch.max(torch.tensor([self.margin]).to(self.device),torch.mv(random_z,true_mean.T)).mean()
        random_std_r = 1. +(torch.mv(random_z,true_mean.T)).mean()
        return true_std, random_std_m, random_std_r

    def inference(self, x):
        return self.encoder(x)

    def cosdistance(self, x, y):
        s1 = self.encoder(x)
        s2 = self.encoder(y)
        return torch.dot(s1,s2)
