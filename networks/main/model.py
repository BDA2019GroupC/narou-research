import torch
import torch.nn as nn
import torch.nn.functional as F

class Embedding(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Embedding, self).__init__()
        self.embedding = nn.Embedding(input_size,128)
        self.embLinear = nn.Linear(128, hidden_size, bias=False)

    def forward(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        return emblinear

class ContentEncoder(nn.Module):
    def __init__(self, method, hidden_size, output_size):
        super(ContentEncoder, self).__init__()
        self.output_size = output_size
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "GRU":
            self.forward = self.forwardGRU
            self.GRU = nn.GRU(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)

    def forwardRNN(self, embedding):
        output_, _ = self.RNN(embedding)
        output = torch.sum(output_[:,-1,:].view(output_.shape[0],self.output_size,-1), dim=2)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

    def forwardGRU(self, embedding):
        output_, _ = self.GRU(embedding)
        output = torch.sum(output_[:,-1,:].view(output_.shape[0],self.output_size,-1), dim=2)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

class Decoder(nn.Module):
    def __init__(self, method, hidden_size, output_size):
        super(Decoder, self).__init__()
        self.output_size = output_size
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "GRU":
            self.forward = self.forwardGRU
            self.GRU = nn.GRU(hidden_size, output_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        self.output_l = nn.Linear(hidden_size, 128, bias=False)
        self.output_b = nn.Linear(128, output_size, bias=False)

    def forwardRNN(self, seqs):
        output, _ = self.RNN(seqs)
        output = self.output_l(output)
        output = self.output_b(output)
        return score

    def forwardGRU(self, seqs):
        output_, _ = self.GRU(seqs)
        output = self.output_l(output)
        output = self.output_b(output)
        return score

class EncoderDecoder(nn.Module):
    def __init__(self, method, device, dic_size, hidden_size, output_size):
        super(EncoderDecoder, self).__init__()
        self.embedding = Embedding(dic_size, hidden_size)
        self.contentEncoder = ContentEncoder(method, hidden_size, output_size)
        self.decoder = Decoder(method, output_size, dic_size)

    def forward(self, seqs):
        out = self.embedding(seqs)
        out = self.contentEncoder(out)
        out = self.decoder(out)
        return out