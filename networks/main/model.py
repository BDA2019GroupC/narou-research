import torch
import torch.nn as nn
import torch.nn.functional as F

class Embedding(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(StyleEncoder, self).__init__()
        self.embedding = nn.Embedding(input_size,128)
        self.embLinear = nn.Linear(128, hidden_size, bias=False)

    def forward(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        return emblinear

class ContentEncoder(nn.Module):
    def __init__(self, weights, method, embedding, input_size, hidden_size, output_size):
        super(StyleEncoder, self).__init__()
        self.output_size = output_size
        self.embedding = embedding
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "GRU":
            self.forward = self.forwardGRU
            self.GRU = nn.GRU(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)

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

class Decoder(nn.Module):
    def __init__(self, method, embedding, input_size, hidden_size, output_size):
        super(StyleEncoder, self).__init__()
        self.output_size = output_size
        self.embedding = embedding
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "GRU":
            self.forward = self.forwardGRU
            self.GRU = nn.GRU(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)

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
